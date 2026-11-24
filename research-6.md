# Jordan TV: Research / changelog 6 (movies, Magic School Bus, Sitcoms)

Implemented Monday, Nov 23, 2026, America/New_York, after Jordan approved adding the research-5 movies, Magic School Bus, and a bigger sitcoms channel (including Everybody Loves Raymond).

Backup of the pre-edit import is at `r7/jordan-tv-import-full.before-r7.json` (34 stations, 13,046 videos, 4,520,234 bytes). The updated import is `jordan-tv-import-full.json`.

App/APK was not changed. Nothing was merged to `main`.

## Totals

| | Before (r6 / Halloween+Muppets import) | After r7 |
|---|---:|---:|
| Stations | 34 | 36 |
| Videos | 13,046 | 15,567 |
| Added | — | 2,521 (all `kind: archive`, real `durationSec`, new `ia-3258`–`ia-38f6` ids) |
| File size | 4,520,234 bytes | 5,490,068 bytes (5,488,333 characters) |

App v1.2 (`flynn/no-storage-limit`, PR #2) has no import or localStorage cap. This file would have been over the old ~5.2M-character WebView limit, so it needs that APK (or later), not v1.1.

Other stations were left alone except appends to **90s Classics** and **PBS KIDS 2000's**. Two new stations: **Sports Movie Night** (41) and **Sitcoms** (42). Air Bud, Rookie of the Year, The Sandlot, and the TGIF Family Matters run were not moved or duplicated.

## 1) Movies — where each one went

### 90s Classics (station 38, now 34 titles, +6)

Family / 80s–90s live-action and animated features that sit with the existing 90s Classics list.

| Title | Identifier | Duration | Notes |
|---|---|---:|---|
| Honey, I Shrunk the Kids (1989) | `honey-i-shrunk-the-kids.-disney.-buena-vista.-1990` | 102m | 640×480 VHS MP4 |
| Honey, I Blew Up the Kid (1992) | `honey_i_blew_up_the_kid_1992` | 89m | 676×360 MP4 |
| George of the Jungle (1997) | `george-of-the-jungle-1997` | 91m | 1920×1024 MP4 |
| The Princess Bride (1987) | `the-princess-bride_202306` | 98m | 1280×720 MP4 |
| The NeverEnding Story (1984) | `the.neverending.story.1984.hd` | 94m | 1920×800 HEVC MKV, English E-AC-3 |
| Thumbelina (1994) | `thumbelinafullmovie1994` | 86m | 640×348 MP4, Don Bluth |

Each file returned HTTP 206.

### Sports Movie Night (new station 41, 6 titles)

A dedicated sports-movie channel is a better fit than dumping these into 90s Classics: Hoosiers (1986), Field of Dreams (1989), and Remember the Titans (2000) are not really “90s,” and they form a natural group. Existing sports titles already on other channels (Air Bud, Rookie of the Year, The Sandlot) were left where they are.

| Title | Identifier | Duration | Notes |
|---|---|---:|---|
| The Mighty Ducks (1992) | `the-mighty-ducks-1992-vhs-rip` | 107m | 720×480 VHS MP4 |
| Cool Runnings (1993) | `cool-runnings_202601` | 98m | 1904×1024 MP4 |
| Angels in the Outfield (1994) | `disneys-angels-in-the-outfield-1995-vhs` | 109m | 640×480 VHS MP4, Version 1 (the item also has a Version 2) |
| Remember the Titans (2000) | `remember-the-titans-2000` | 113m | 1280×544 MP4 |
| Field of Dreams (1989) | `field-of-dreams_1989` | 105m | 1920×1080 MP4 |
| Hoosiers (1986) | `hoosiers_202611` | 114m | 720×544 Cinepack AVI |

Each file returned HTTP 206. Logo is a gold-on-navy “SPORTS MOVIES” wordmark.

## 2) Magic School Bus — PBS KIDS 2000's

52 episodes (complete: S01–S04, 13 each) from `the-magic-school-bus-full-series-dvd-rip` were appended to **PBS KIDS 2000's** (station 11, 2,033 → 2,085). That channel already has Arthur, Cyberchase, WordGirl, and similar classroom shows. Preschool would have been the wrong age band.

**Audio check (research-5 warning superseded):** the mid-file and S01E01 both have two AC3 tracks, but they *are* tagged. Track 1 is `eng`, track 2 is `spa`. Default audio is English. Safe to play as-is. Mid-file Range GET returned HTTP 206. Files are 704×480 HEVC MKV, ~25–26 minutes.

## 3) Sitcoms (new station 42)

Channel name **Sitcoms** (logo wordmark “SITCOMS”), shuffle mode, 2,457 episodes across 17 shows. Mid-file of every set returned HTTP 206 on this build. Single audio track on the probed files. Prefer h264/MP4 when a cleaner set existed; otherwise the best complete playable English set.

Everybody Loves Raymond uses the 208-episode 720p set already described to Jordan (2 episodes short of the official 210), not the softer complete 360p 210-episode set.

| Show | Added | Official | Identifier | Notes |
|---|---:|---:|---|---|
| Everybody Loves Raymond | 208 | 210 | `everybody-loves-raymond-tv-series` | 960×720 h264/AAC; two episodes short |
| Malcolm in the Middle | 151 | 151 | `malcolm-in-the-middle-complete-series-2000-2006` | Complete, 1080p |
| The Nanny | 144 | 146 | `the-nanny-complete-series_20260128` | MPEG-2 in MKV, 720×480 |
| Home Improvement | 202 | 204 | `home-improvement-complete-dvd-rip` | 700×476 h264; 3 extras (bloopers / specials) dropped; rip appears 2 episodes short of official 204 |
| Saved by the Bell | 86 | 86 | `saved-by-the-bell-complete-series_20251118` | Complete original series, h264 |
| Saved by the Bell: The College Years | 19 | 19 | `saved-by-the-bell-the-college-years-season-1` | Complete, h264 |
| Sabrina the Teenage Witch | 163 | 163 | `sabrina-the-teenage-witch-complete` | Complete, 576p HEVC |
| The King of Queens | 206 | 207 | `the-king-of-queens-tv-version` | 640×360 h264; one episode short. Preferred over a 384p AVI rip |
| Boy Meets World | 158 | 158 | `boy-meets-world-complete` | Complete, 480p HEVC. TGIF only has blocks, not the full series, so this is not a duplicate |
| The Golden Girls | 179 | 180 | `the-golden-girls-complete-480p-x264` | One episode short |
| The Wonder Years | 115 | 115 | `the-wonder-years-complete-series` | Complete (through S06E22) |
| Growing Pains | 164 | 166 | `growing-pains-complete-series` | 360p; two short of official 166 |
| 3rd Rock from the Sun | 136 | 139 | `3rd-rock-from-the-sun-2x-25-a-nightmare-on-dick-street-1` | 720p; through the series finale |
| 8 Simple Rules | 72 | 76 | `8-simple-rules-2002-complete` | 720p; the item only has 72 episode files |
| One on One | 103 | 113 | `one-on-one-s-01-e-01-when-flex-got-breanna-480p-nf-web-dl` | Through the S05 finale; 10 short of official 113 |
| Perfect Strangers | 150 | 150 | `perfect-strangers-Lando18` | Complete, 960×720 |
| The Cosby Show | 201 | 201 | `the-cosby-show-complete-series_202512` | Complete 360p set, not on the example list, added because it verified cleanly |

Official counts are the commonly published episode totals, used only to describe completeness.

## 4) Skipped, and why

- **That ’70s Show** — No playable complete set. The S01–S08 item had no original video files; loose seasons are missing 5 and 8 and are ~240p AVI/MPG.
- **Family Matters** (complete 214/215 item) — Already essentially on TGIF (205 episodes). Not duplicated.
- **Married… with Children** — Playable item had only 22 episodes; the “complete” listing had no original video files.
- **Saved by the Bell: Good Morning, Miss Bliss** — Only in the all-AVI 120-file mega-set. Kept the cleaner h264 MP4 original series + College Years instead.
- **Everybody Loves Raymond 360p complete (210 eps)** — Used the 208-episode 720p set instead (sharper; two episodes short).
- **Seinfeld, Friends, Cheers, Frasier, Roseanne, The Fresh Prince of Bel-Air, Full House, The Office (US), Scrubs, How I Met Your Mother, The Drew Carey Show, Step by Step, Sister, Sister, Hangin’ with Mr. Cooper** — No playable, mostly-complete English set found this round (or the search hit was the wrong show / a lime-torrents item with 0 original videos).
- **The Goonies (1985)** — Not on the approved 12-movie list; the only copy was also short (97m vs 114m theatrical).
- **Parent Trap (1961), Little Giants, Space Jam audience VHS** — Leftovers from earlier research, not on the approved movie list for this pass.

**Copyright note:** These are still almost all copyrighted Archive rips, listed and added the same way as rounds 1–5. Counts and URLs were not fabricated; only verified playable files were added.

## 5) Validation

- JSON parses. Top-level keys and profile / searches / activeId match the pre-r7 backup.
- No new duplicate ids. (Some older videos already share an id when the same file appears on two stations, e.g. Kim Possible on VHS Kids Movies and Disney Channel; those were left alone.)
- Every new video has a real `durationSec` (min 1,013s, max 6,889s). None fell back to the app’s 60s default.
- Mid-file (or every feature) Range GET was HTTP 206.
- Build script: `r7/build.py`.
