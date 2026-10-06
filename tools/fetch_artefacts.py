#!/usr/bin/env python3
"""Fetch freely licensed images from Wikimedia Commons for Bank timeline events.

Reads artefacts_plan.json, writes img/NNN-K.jpg and data/artefacts.json.
Only keeps Commons files with a free license (PD or CC). Safe to re-run.
"""
import json, os, re, sys, time, urllib.parse, urllib.request, html
from io import BytesIO

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
IMG = os.path.join(ROOT, "img")
PLAN = os.path.join(HERE, "artefacts_plan.json")
OUT = os.path.join(ROOT, "data", "artefacts.json")
os.makedirs(IMG, exist_ok=True)

UA = "Bank1694Artefacts/1.0 (personal learning project; github.com/julianlee314-hue/the-bank-1694)"
WP = "https://en.wikipedia.org/w/api.php"
CM = "https://commons.wikimedia.org/w/api.php"
FREE = re.compile(r"public domain|^pd|cc0|cc[- ]by|no restrictions|attribution|gfdl|free art|copyrighted free use", re.I)
OK_MIME = {"image/jpeg", "image/png", "image/tiff", "image/svg+xml", "image/gif", "image/webp"}
SKIP_NAME = re.compile(
    r"(flag_of|coat_of_arms|seal_of|logo|icon|symbol|signature|locator|blank|question_book|edit[_ ]button|commons-logo|wiki.?letter|ambox|padlock)",
    re.I,
)


def get(url, params, tries=6):
    q = url + "?" + urllib.parse.urlencode({**params, "format": "json", "formatversion": "2"})
    err = None
    for i in range(tries):
        try:
            req = urllib.request.Request(q, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.load(r)
        except Exception as e:
            err = e
            msg = str(e).lower()
            wait = 45 if ("429" in msg or "rate" in msg) else (2 + 2 ** i)
            print(f"  API wait {wait}s: {e}", file=sys.stderr)
            time.sleep(wait)
    print("  API failed:", err, file=sys.stderr)
    return {}


def strip(s, n=320):
    s = html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()
    s = re.sub(r"\s+", " ", s)
    return (s[: n - 1] + "…") if len(s) > n else s


def info_for(titles):
    if not titles:
        return []
    d = get(CM, {"action": "query", "titles": "|".join(titles[:20]), "prop": "imageinfo",
                 "iiprop": "url|mime|size|extmetadata", "iiurlwidth": 800})
    return d.get("query", {}).get("pages", [])


def usable(p):
    if p.get("missing") or not p.get("imageinfo"):
        return None
    ii = p["imageinfo"][0]
    md = ii.get("extmetadata", {})
    lic = md.get("LicenseShortName", {}).get("value", "")
    if ii.get("mime") not in OK_MIME or not FREE.search(lic) or "fair use" in lic.lower():
        return None
    if SKIP_NAME.search(p["title"]):
        return None
    if ii.get("width", 0) < 350 and ii.get("mime") != "image/svg+xml":
        return None
    return {
        "file": p["title"],
        "thumb": ii.get("thumburl") or ii["url"],
        "page": ii.get("descriptionurl"),
        "license": strip(lic, 60),
        "artist": strip(md.get("Artist", {}).get("value", ""), 120),
        "date": strip(md.get("DateTimeOriginal", {}).get("value", ""), 40),
        "desc": strip(md.get("ImageDescription", {}).get("value", "")),
        "objname": strip(md.get("ObjectName", {}).get("value", ""), 120),
    }


def from_file(title):
    if not title.startswith("File:"):
        title = "File:" + title
    for p in info_for([title]):
        u = usable(p)
        if u:
            return u
    return None


def from_wiki(title):
    d = get(WP, {"action": "query", "titles": title, "prop": "pageimages", "piprop": "name", "redirects": 1})
    pages = d.get("query", {}).get("pages", [])
    name = pages[0].get("pageimage") if pages else None
    if name:
        u = from_file("File:" + name)
        if u:
            return u
    return from_search(title)


def from_search(q):
    d = get(CM, {"action": "query", "generator": "search", "gsrsearch": q + " filetype:bitmap",
                 "gsrnamespace": 6, "gsrlimit": 10, "prop": "imageinfo",
                 "iiprop": "url|mime|size|extmetadata", "iiurlwidth": 800})
    pages = sorted(d.get("query", {}).get("pages", []), key=lambda p: p.get("index", 99))
    for p in pages:
        u = usable(p)
        if u:
            return u
    return None


def download(url, path):
    if os.path.exists(path) and os.path.getsize(path) > 2000:
        return True
    tmp = path + ".src"
    for i in range(6):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=90) as r, open(tmp, "wb") as f:
                f.write(r.read())
            break
        except Exception as e:
            err = e
            wait = 60 if "429" in str(e) else (3 + 2 ** i)
            print(f"  dl wait {wait}s: {e}", file=sys.stderr)
            time.sleep(wait)
    else:
        print("  download fail", err, file=sys.stderr)
        return False
    try:
        from PIL import Image
        im = Image.open(tmp).convert("RGB")
        im.thumbnail((800, 800))
        im.save(path, "JPEG", quality=78, optimize=True, progressive=True)
    except Exception:
        os.replace(tmp, path)
    if os.path.exists(tmp):
        try:
            os.remove(tmp)
        except OSError:
            pass
    return os.path.exists(path) and os.path.getsize(path) > 500


def resolve(src):
    how, q = src.split(":", 1)
    if how == "f":
        return from_file(q if q.startswith("File:") else "File:" + q)
    if how == "w":
        return from_wiki(q)
    return from_search(q)


def main():
    plan = json.load(open(PLAN))
    only = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    manifest = json.load(open(OUT)) if os.path.exists(OUT) else {}
    seen = {a.get("file") for v in manifest.values() for a in v.get("items", []) if a.get("file")}
    keys = sorted(plan, key=lambda k: int(k))
    if only:
        keys = [k for k in keys if k in only]
    for n in keys:
        if n in manifest and manifest[n].get("items") and not only:
            print(n, "skip (have", len(manifest[n]["items"]), ")")
            continue
        entry = {"items": [], "missed": []}
        if plan[n].get("quote"):
            entry["quote"] = plan[n]["quote"]
        for k, (kind, src) in enumerate(plan[n]["items"]):
            hit = resolve(src)
            time.sleep(2.5)
            if not hit or hit["file"] in seen:
                entry["missed"].append(src)
                continue
            fn = f"{int(n):03d}-{k + 1}.jpg"
            if not download(hit["thumb"], os.path.join(IMG, fn)):
                entry["missed"].append(src)
                continue
            seen.add(hit["file"])
            hit.update({"img": "img/" + fn, "type": kind, "source": src})
            # Drop raw commons file title from public manifest key clash — keep commons title as commons
            hit["commons"] = hit.pop("file")
            entry["items"].append(hit)
        manifest[n] = entry
        print(n, len(entry["items"]), "found", "| missed:", entry["missed"], flush=True)
        json.dump(manifest, open(OUT, "w"), indent=1, ensure_ascii=False)
    total = sum(len(v["items"]) for v in manifest.values())
    empty = [n for n, v in manifest.items() if not v["items"]]
    covered = sum(1 for v in manifest.values() if v.get("items"))
    print("DONE images:", total, "events with image:", covered, "events without:", len(empty))


if __name__ == "__main__":
    main()
