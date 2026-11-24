# Jordan TV: Research / changelog 8 (preschool + sitcoms picks from research-7)

Implemented Monday, Nov 23, 2026, America/New_York, after Jordan picked only these from research-7: "Blue clues Franklin Madeline. Reading rainbo sister sister w reba only".

Backup of the pre-edit import is at `r8/jordan-tv-import-full.before-r8.json` (36 stations, 15,567 videos, 5,490,068 bytes). The updated import is `jordan-tv-import-full.json`.

App/APK was not changed. Nothing was merged to `main`. This stacks on `flynn/sitcoms-movies-msb` (PR #4).

## Totals

| | Before (r7) | After r8 |
|---|---:|---:|
| Stations | 36 | 36 (no new channels) |
| Videos | 15,567 | 16,274 |
| Added | — | 707 (all `kind: archive`, real `durationSec`, new `ia-3c31`–`ia-3ef3`) |
| File size | 5,490,068 bytes | 5,726,000 bytes (5,724,267 characters) |

Still needs the v1.2 no-limit APK (PR #2). Other stations were left alone except appends to **Preschool**, **PBS KIDS 2000's**, and **Sitcoms**. Nothing else from research-7 was added.

New ids are unique and do not collide with the existing lineup. Pre-existing cross-station id reuse was left as-is. Mid-file HTTP Range checks on each show (including a Franklin AVI, a 160p Blue's Clues episode, Madeline, and Reba) returned HTTP 206. Default audio is English on every added set (Reba also has a Spanish AC3 track that is not first).

## 1) Preschool (station 37, 1,400 → 1,708, +308)

| Show | Added | Source | Notes |
|---|---:|---|---|
| Blue's Clues | 141 | `blues-clues-s-03-e-59-blues-big-musical-movie` | Official often counted as 143. All MP4/h264. Includes Meet Blue's Baby Brother (S06E143). **Skipped:** Extended Birthday, 73-min Meet Joe Scrapbook Adventure, Behind the Clues making-of, and the 160p Big Musical Movie (feature, very soft). 15 regular episodes (plus that included special) exist only as soft 160p MP4/h264 — playable, but low-resolution. |
| Franklin (1997) | 101 | `franklin-and-friends-deep-sea-voyage` | Classic series plus four MP4 specials (Back to School, Green Knight, Turtle Lake Treasure, Magic Christmas). Official is commonly 78 half-hours; S02E13 and S03E12 are missing from the item. Some half-hours are split a/b AVI segments; unique misnumbered S03E09 titles were kept. Prefer MP4/h264 when the same half-hour exists (30 MP4, 71 AVI). **Skipped:** 2011 *Franklin and Friends* CGI (Special Job, Deep Sea Voyage, Polar Explorer) and the Father's Day compilation. IA "Cinepack" tags on the AVIs are wrong: probed files are mpeg4 (XviD-family) + mp3 and return HTTP 206. ExoPlayer on the TV box typically plays them; WebView/HTML5 may not. |
| Madeline | 66 | `Madeline-cartoon` | All 65 series episodes (S3PP2 included as S03E02, Orient Express) plus *Lost in Paris*. No mp4/h264 alternative — all MPEG-2 in MKV with English AC3, same family as The Nanny already on Sitcoms. ExoPlayer on the TV box plays this; WebView/HTML5 may not. |

## 2) PBS KIDS 2000's (station 11, 2,085 → 2,240, +155)

| Show | Added | Source | Notes |
|---|---:|---|---|
| Reading Rainbow | 155 / 155 | `ReadingRainbowTVSeries` | Complete. 640×480 h264 / English E-AC-3 MKV (Amazon WEB-DL). Mid-file HTTP 206. |

## 3) Sitcoms (station 42, 2,457 → 2,701, +244)

| Show | Added | Source | Notes |
|---|---:|---|---|
| Sister, Sister | 119 / 122 official | `sister-sister-s-1` … `s-6` | All unique episode files on the six season items (12+19+22+22+22+22). MPEG4 MP4, h264, English AAC. |
| Reba | 125 files (covers 127 official) | `reba-complete-series` | Seasons 22+24+22+22+22+13. Two official two-parters (S02E09-10, S03E01-02) are single longer files and were kept. **Skipped:** 10 special-feature / deleted-scene / outtakes / promo files. MPEG-2 in MKV, default English AC3 (Spanish AC3 is present, not first). Same playability note as Madeline / The Nanny: ExoPlayer yes, WebView/HTML5 maybe not. |

## Playability flags (not skipped)

Nothing in this add was dropped as unplayable. Android ExoPlayer on the onn box already plays The Nanny's MPEG-2 MKVs and should play Madeline, Reba, and the Franklin AVIs. Browser/WebView HTML5 may not play AVI or MPEG-2. Prefer the MP4/h264 copies where they exist.
