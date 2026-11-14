#!/usr/bin/env python3
"""Internet Archive helpers for Jordan TV channel building."""
from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

CACHE = Path("/workspace/jordantv/ia-cache")
META = CACHE / "meta"
UA = "JordanTVChannelBuilder/1.0 (personal archive research)"
VIDEO_EXT = re.compile(r"\.(mp4|m4v|mkv|webm|ogv|avi|mpeg|mpg|mov)$", re.I)
SKIP_NAME = re.compile(r"thumb|sample|\.ia\.|_512kb", re.I)
BAD = re.compile(
    r"\b(porn|xxx|nsfw|erotic|adult\s+hotline|sex\s+tape|playboy|hentai|"
    r"rule34|abortion|hotline\s+spots)\b",
    re.I,
)
# keep "Naked Genius" Kim Possible episode? That's a KP episode title already in his lineup.
# BAD shouldn't flag "Naked Genius" as adult. The pattern is fine.

def http_get(url: str, timeout: int = 90) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def safe_id(ident: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", ident)[:180]


def metadata(ident: str, retries: int = 3) -> dict | None:
    META.mkdir(parents=True, exist_ok=True)
    path = META / f"{safe_id(ident)}.json"
    if path.exists() and path.stat().st_size > 20:
        try:
            return json.loads(path.read_text())
        except json.JSONDecodeError:
            path.unlink()
    url = "https://archive.org/metadata/" + urllib.parse.quote(ident, safe="")
    last = None
    for attempt in range(retries):
        try:
            raw = http_get(url, timeout=120)
            data = json.loads(raw)
            # shrink: keep metadata + files with needed fields
            slim = {
                "metadata": data.get("metadata") or {},
                "files": [
                    {
                        k: f.get(k)
                        for k in (
                            "name",
                            "format",
                            "size",
                            "length",
                            "height",
                            "width",
                            "source",
                            "original",
                        )
                        if f.get(k) is not None
                    }
                    for f in (data.get("files") or [])
                    if isinstance(f, dict) and f.get("name")
                ],
            }
            path.write_text(json.dumps(slim))
            time.sleep(0.25)
            return slim
        except Exception as e:
            last = e
            time.sleep(1.2 * (attempt + 1))
    print(f"  META FAIL {ident}: {last}")
    return None


def parse_length(val) -> int:
    if val is None or val == "":
        return 0
    if isinstance(val, (int, float)):
        return int(round(float(val))) if float(val) > 0 else 0
    s = str(val).strip().lower().replace(",", "")
    if re.fullmatch(r"\d+(\.\d+)?", s):
        return int(round(float(s)))
    m = re.fullmatch(r"(?:(\d+):)?(\d+):(\d+)(?:\.\d+)?", s)
    if m:
        h = int(m.group(1) or 0)
        return h * 3600 + int(m.group(2)) * 60 + int(m.group(3))
    m = re.search(r"(\d+)\s*h(?:our)?s?", s)
    n = re.search(r"(\d+)\s*m(?:in)?", s)
    sec = re.search(r"(\d+)\s*s(?:ec)?", s)
    if m or n or sec:
        return (
            (int(m.group(1)) * 3600 if m else 0)
            + (int(n.group(1)) * 60 if n else 0)
            + (int(sec.group(1)) if sec else 0)
        )
    return 0


def is_video_file(f: dict) -> bool:
    name = f.get("name") or ""
    if not VIDEO_EXT.search(name):
        return False
    if SKIP_NAME.search(name):
        return False
    fmt = str(f.get("format") or "").lower()
    if "thumb" in fmt or "ia" == fmt:
        return False
    return True


def height_of(f: dict) -> int:
    try:
        return int(float(f.get("height") or 0))
    except (TypeError, ValueError):
        return 0


def width_of(f: dict) -> int:
    try:
        return int(float(f.get("width") or 0))
    except (TypeError, ValueError):
        return 0


def size_of(f: dict) -> int:
    try:
        return int(float(f.get("size") or 0))
    except (TypeError, ValueError):
        return 0


def is_mp4(f: dict) -> bool:
    return bool(re.search(r"\.(mp4|m4v)$", f.get("name") or "", re.I))


def looks_h264(f: dict) -> bool:
    fmt = (str(f.get("format") or "") + " " + (f.get("name") or "")).lower()
    return any(t in fmt for t in ("h.264", "h264", "avc", "mpeg4", "mp4"))


def file_score(f: dict) -> tuple:
    """Highest resolution first. Original beats Archive derivative transcodes.
    At the same resolution, prefer h264 MP4, then any MP4, then MKV."""
    name = f.get("name") or ""
    src = str(f.get("source") or "").lower()
    deriv = src == "derivative" or bool(re.search(r"512kb|\.ia\.|internet.?archive", name, re.I))
    mp4 = 1 if is_mp4(f) else 0
    h264 = 1 if looks_h264(f) else 0
    original = 1 if src == "original" else 0
    return (height_of(f), width_of(f), 0 if deriv else 1, mp4, h264, original, size_of(f))


def pretty_name(name: str, fallback: str = "Video") -> str:
    base = str(name or fallback).split("/")[-1]
    base = re.sub(r"\.[^.]+$", "", base)
    base = base.replace("_", " ")
    # keep episode dots like S01E01; collapse other runs later in clean_title
    base = re.sub(r"\s+", " ", base).strip()
    return (base or fallback)[:160]


def clean_title(title: str) -> str:
    t = title
    t = re.sub(r"\s*[\[\(](?:friendsfa|jpv711|edge\s*2020|tv-?dvdrip.*?)[\]\)]", "", t, flags=re.I)
    t = re.sub(r"\s*\((?:480p|720p|1080p|2160p)[^\)]*\)", "", t, flags=re.I)
    t = re.sub(r"\s*\[[^\]]*(?:480p|720p|1080p|x265|x264|hevc)[^\]]*\]", "", t, flags=re.I)
    t = re.sub(r"\s*-\s*savetube\.us", "", t, flags=re.I)
    t = re.sub(r"\s*\d+p$", "", t)
    t = t.replace(".", " ")
    t = re.sub(r"\s+", " ", t).strip(" -_")
    # WWF Heat dates like 09 01 00 inside a January 2000 folder already pretty-printed
    m = re.fullmatch(r"(\d{2})[ .](\d{2})[ .](\d{2})", t)
    if m:
        d, mo, y = m.group(1), m.group(2), m.group(3)
        year = 2000 + int(y) if int(y) < 70 else 1900 + int(y)
        months = "January February March April May June July August September October November December".split()
        try:
            t = f"WWF Sunday Night Heat {months[int(mo)-1]} {int(d)}, {year}"
        except Exception:
            pass
    return t[:160]


def norm_group(name: str) -> str:
    base = str(name).split("/")[-1]
    base = re.sub(r"\.[^.]+$", "", base)
    m = re.search(r"(s\s*\d{1,2}\s*e\s*\d{1,3})(?:\s*e\s*\d{1,3})?", base, re.I)
    if m:
        ep = re.sub(r"\s+", "", m.group(0).lower())
        show = re.split(r"s\s*\d{1,2}\s*e", base, maxsplit=1, flags=re.I)[0]
        show = re.sub(r"[^a-z0-9]+", "", show.lower())
        return f"{show}:{ep}"
    m = re.search(r"(?:^|[^\d])(\d{1,3})x(\d{1,3})(?:[^\d]|$)", base, re.I)
    if m:
        show = re.sub(r"[^a-z0-9]+", "", base[: m.start()].lower())
        return f"{show}:s{int(m.group(1)):02d}e{int(m.group(2)):02d}"
    cleaned = re.sub(
        r"(1080p|720p|480p|2160p|webrip|web[- ]?dl|bluray|blu[- ]?ray|dvdrip|hdtv|"
        r"x265|x264|hevc|avc|aac|10bit|ai[- ]?upscale|repack|proper|remux|pdtv|"
        r"web-dl|hmax|dd5\.?1|dd2\.?0)",
        "",
        base,
        flags=re.I,
    )
    cleaned = re.sub(r"\[.*?\]|\((?:\d{3,4}p).*?\)", "", cleaned)
    cleaned = re.sub(r"[^a-z0-9]+", "", cleaned.lower())
    return cleaned or base.lower()


def item_runtime(meta: dict) -> int:
    info = meta.get("metadata") or {}
    for key in ("length", "runtime", "duration"):
        sec = parse_length(info.get(key))
        if sec >= 5:
            return sec
    return 0


def pick_videos(ident: str, meta: dict, mode: str = "each", min_sec: int = 5, max_videos: int = 500, name_contains: str | None = None) -> list[dict]:
    """mode=each: best file per episode/group. mode=one: single best file for the item."""
    files = [f for f in (meta.get("files") or []) if is_video_file(f)]
    files = [f for f in files if not BAD.search(f.get("name") or "")]
    if name_contains:
        needles = [n.strip().lower() for n in name_contains.split("|") if n.strip()]
        files = [f for f in files if any(n in (f.get("name") or "").lower() for n in needles)]

    if not files:
        return []
    info = meta.get("metadata") or {}
    title_fallback = ""
    t = info.get("title")
    if isinstance(t, list):
        title_fallback = str(t[0] if t else "Video")
    else:
        title_fallback = str(t or "Video")

    def duration_for(f):
        sec = parse_length(f.get("length"))
        if sec >= 1:
            return sec
        return item_runtime(meta) or 0

    if mode == "one":
        best = max(files, key=file_score)
        sec = duration_for(best) or 1500
        title = title_fallback if len(files) <= 4 else pretty_name(best["name"], title_fallback)
        return [make_video(ident, best, clean_title(title), sec)]

    groups: dict[str, list] = {}
    for f in files:
        groups.setdefault(norm_group(f["name"]), []).append(f)
    out = []
    for _, grp in groups.items():
        best = max(grp, key=file_score)
        sec = duration_for(best)
        if sec and sec < min_sec:
            continue
        if not sec:
            sec = 1500 if mode != "commercials" else 30
        title = clean_title(pretty_name(best["name"], title_fallback))
        if BAD.search(title):
            continue
        out.append(make_video(ident, best, title, sec))
    # For capped sets (commercial compilations), keep the longest reels first.
    if max_videos < 200:
        out.sort(key=lambda v: -v["durationSec"])
        out = out[:max_videos]
        out.sort(key=lambda v: v["title"].lower())
    else:
        out.sort(key=lambda v: v["title"].lower())
        if len(out) > max_videos:
            out = out[:max_videos]
    return out


def file_url(ident: str, name: str) -> str:
    enc = urllib.parse.quote(name, safe="()!'*-_.~/")
    return f"https://archive.org/download/{ident}/{enc}"


def make_video(ident: str, f: dict, title: str, duration: int) -> dict:
    name = f["name"]
    return {
        "id": f"ia-{ident}-{name}"[:180],
        "title": title[:200],
        "durationSec": int(duration),
        "kind": "archive",
        "file": file_url(ident, name),
        "_ident": ident,
        "_name": name,
        "_height": height_of(f),
        "_width": width_of(f),
        "_format": f.get("format") or "",
        "_mp4": is_mp4(f),
        "_size": size_of(f),
    }


def fill_video(v: dict, station_id: str, set_value: str | None = None) -> dict:
    sid = set_value if set_value is not None else f"set-{station_id}"
    return {
        "id": v["id"],
        "title": v["title"],
        "durationSec": v["durationSec"],
        "kind": "archive",
        "set": sid,
        "setName": "",
        "file": v["file"],
        "query": "",
        "imdb": "",
        "year": 0,
        "season": 0,
        "episode": 0,
    }
