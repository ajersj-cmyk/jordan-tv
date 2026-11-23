# Jordan TV: Research Round 4 (app improvements + full-movie channels)

Checked Sunday, Nov 22, 2026, America/New_York. Research only: the import JSON, APK, and repo were not changed. Nothing here has been added.

Current lineup used as the baseline: `jordan-tv-import-full.json` (32 stations, 12,779 videos). App reviewed: Jordan TV 2 v1.2-nolimit (`tv.jordan.app.v2`), bundled `v12/guide.built.html`.

## Method

- Guide and native bridge were read in the v1.2 APK (on-air path, menus, keys, resume, storage).
- Internet Archive `advancedsearch` (quoted title + themed queries) and the metadata API. Candidates were checked against the 279 unique identifiers already in the lineup and against titles already on a channel.
- One original playable file per item (MKV/MP4/AVI/MPG/MOV, not IA 480p `.ia.mp4` / `_512kb.mp4` derivatives) was Range-GET'd and ffprobe'd. Every recommended file below returned HTTP 206 unless noted.
- Audio is listed as tagged. `untagged` means the rip did not set a language; those are English-language US/UK releases by title, but tracks were not listened to. Dual-audio items are flagged.
- Research 1–3 items that Jordan already added (or that are sitting unused from earlier lists) are not re-pitched as new finds. A short reminder appears only where it fills a channel.

**Copyright note:** Almost all of the movies below are still under copyright. These are listings already on archive.org, in the same style as rounds 1–3. Official or clearer-rights options (YouTube official channels, public-domain features, paid services) are called out at the end. Nothing is added until you pick.

---

## 1) App improvements

All of these ship inside the APK (`assets/guide.html` is bundled). A “guide.html only” change still needs a rebuild to reach the TV. “Needs native” means MainActivity / ExoPlayer / key dispatch has to change too.

The guide already has: a virtualized grid, shuffle/order, skip shorts, start-at-beginning, resume for the current channel, Find, add-station, export/import, phone remote + QR, YouTube vs archive player pickers, channel logos as `data:image/` URIs, and a native on-air logo bug via `JordanTube.airMark`. v1.1 fixed guide lag; v1.2 removed the lineup size cap. The ideas below are things the code does not do yet.

| # | Idea | Why it matters now | Effort | Where |
|---|---|---|---|---|
| 1 | **Now/next banner when you land on a channel** | While the guide is open, the info box already shows the title, time range, and `NEXT:`. In on-air mode `body.is-air #app` is hidden, so that info disappears. Any remote key just calls `leaveAir()` and dumps you back to the guide. A short overlay (channel number + name, title, start–end, next) on tune, or on OK / Info, then fade, would feel like real cable. | Medium | guide.html + native overlay on the ExoPlayer surface (same path as `airMark`) |
| 2 | **Channel-number entry** | Stations already have numbers (1–38, with gaps). The key map is only arrows, Enter, Escape, and Backspace. Digit keys do nothing. A 1–2 second digit buffer, like a cable box, that jumps to that number (or flashes “not found”) is the highest-leverage live-TV habit still missing. | Medium | guide.html + Android `KEYCODE_0`–`9` dispatch |
| 3 | **Last-channel toggle** | `tune()` overwrites `activeId` and does not remember the previous station. Store one previous id and jump back on a long-OK, a “last” action, or entering `0`. Tiny code, used constantly. | Low | Mostly guide.html; maybe one remote key |
| 4 | **Program-info card (year / season / episode)** | The import schema already has `year`, `season`, and `episode`, but every current video stores `0`. Those fields are only passed to `JordanTube.resolve` for Torbox, never shown. Parse `SxxEyy` out of titles, optionally refresh from IA metadata, and show them on the guide and on the on-air banner. | Medium | guide.html; optional one-time JSON enrich (you’d still pick that separately) |
| 5 | **Sleep timer** | The app holds a `WAKE_LOCK` and otherwise runs forever, which is rough for Blake at bedtime. 15 / 30 / 60 / 90 minutes, a quiet countdown, then pause and leave on-air. | Low–medium | guide.html + native pause/hide of ExoPlayer |
| 6 | **Favorites + a PIN lock** | No favorites list. Export already writes `profile.pin: ""` and never uses it. Let you star channels, filter the guide, and PIN-lock everything except Preschool (and whatever else you choose) so Blake can use the box without landing on wrestling or Toonami. | Medium | guide.html + a native PIN prompt on the remote |
| 7 | **Fake commercial breaks from Retro Commercials** | Station 32 already has 94 ads. Playback is a straight playlist (`nextOnPlaylist`). Between shows, optionally insert 1–3 spots from that channel, then continue. Skip this on Preschool when the PIN/kids mode is on. No extra visuals; just playlist glue, so it stays GPU-light. | Medium | guide.html playlist logic |
| 8 | **Continue watching** | Resume already saves `{stationId, videoId, offset}` for the channel you were on and restores it after a shuffle window. There is no list of in-progress titles and no “pick up last night’s movie” row. Keep a short recents list and show it at the top of the guide or on launch. | Medium | guide.html, using the v1.2 file store |
| 9 | **Archive thumbnails + cleaner episode titles** | `showCover` only loads YouTube `i.ytimg.com` thumbs, so archive cells are blank. IA metadata is already fetched and cached on one background thread. Use each item’s IA thumb for the guide and OSD, and prefer the archive title when the file name is ugly. | Medium | guide.html + native disk cache for thumbs |
| 10 | **In-app lineup editor** | A channel can gain videos, toggle shuffle / skip-shorts / from-start, set a logo, be renamed, or be deleted. A show can be renamed or deleted (or its whole set deleted). You cannot reorder channels, change numbers, move a show to another station, or merge an import into the current lineup — import still replaces all 32 channels. That’s the next pain point now that storage is unlimited. | Medium | guide.html |
| 11 | **Saturday-morning dayparts** | The guide already builds a fake 24-hour grid from runtimes, but it does not change with the time of day. Optional blocks (“this channel is Saturday Morning 7–11, movies after 7”) can be built from the stations you already have. | Medium | guide.html scheduling |
| 12 | **Faster start + a dead-link pass** | Startup parses the whole 12,779-video lineup, then warms nearby preview players. The grid is already virtualized. Defer archive metadata until a row is visible, and optionally Range-check file URLs in the background with a “dead” badge so a vanished IA item doesn’t fail only at tune time. | Medium | guide.html + the existing native metadata cache |

**Two small freebies noticed in the code:**

- Cloud / Trakt / Torbox is fully written (`openCloud`, `runMenu("cloud")`) but `"cloud"` is not in the settings `MENU` array, so the screen is unreachable. Either add it or drop the dead path.
- The first press while on-air should show the info banner; the second press should open the guide. Right now the first press always exits.

---

## 2) New channel ideas

Best first. Durations are the probed file. “Full” means a complete movie or a complete-or-nearly-complete series. Prefer the listed original file, not the IA `.ia.mp4`.

### A. Sports Movie Night

Pitch: live-action sports movies for a rainy Saturday, next to 90s Classics. The Sandlot, Rookie of the Year, and Air Bud are already in the lineup, so they are omitted here.

| Title | IA | What it is | Probe |
|---|---|---|---|
| The Mighty Ducks (1992) | https://archive.org/details/the-mighty-ducks-1992-vhs-rip | Full movie, VHS rip | h264 720×480, 108m, aac untagged. File: `THE MIGHTY DUCKS 1992 VHS RIP.mp4` |
| Little Giants (1994) | https://archive.org/details/littlegiantsvhsrecording | Full movie, VHS recording (home-tape filename) | h264 640×480, 100m, aac untagged. File: `20200101_021137B.mp4` (3.3 GB) |
| Cool Runnings (1993) | https://archive.org/details/cool-runnings_202601 | Full movie, best copy | h264 1904×1024, 98m, aac untagged. File: `Cool Runnings (1993).mp4` (1.6 GB). A 1994 VHS copy also exists if you want the tape look: `disneys-cool-runnings-vhs-1994` |
| Angels in the Outfield (1994) | https://archive.org/details/angels-in-the-outfield-1994-dvd | Full movie, DVD remux | mpeg2 720×480, 103m, ac3 untagged. File: `B3_t00.mkv`. A flatter 718×342 MP4 is at `angels-in-the-outfield-1994_202601` — skip that one |
| The Big Green (1995) | https://archive.org/details/disneys-the-big-green-vhs | Full movie, VHS | h264 1440×1080, 108m, aac untagged, English tagged. File: `Disney's The Big Green VHS.mp4` (**7.5 GB**, may take a few seconds to start) |
| Remember the Titans (2000) | https://archive.org/details/remember-the-titans-2000 | Full movie | h264 1280×544, 113m, aac untagged. File: `Remember the Titans (2000).mp4` |
| The Sandlot 2 (2005) | https://archive.org/details/the-sandlot-2-2005 | Full movie (sequel; the 1993 original is already on VHS Kids Movies) | h264 640×358, 98m, aac untagged |
| Beethoven (1992) | https://archive.org/details/beethoven1_201911 | Full movie | h264 576×480, 93m, aac untagged |
| Beethoven’s 2nd (1993) | https://archive.org/details/beethoven2 | Full movie | h264 576×480, 117m, aac untagged |
| Space Jam (1996) | https://archive.org/details/spacejam-trb-vhs-aud-tgyhujhygtfrtgyhyy | **Partial / rough:** theatrical audience recording, about 7 minutes short of the official 88m cut | hevc 640×472, 82m, aac untagged. File: `SPACE-JAM-AUDIENCE-RECORDING-TRB.mp4` |

A broadcast-with-ads Beethoven also exists: https://archive.org/details/wtic-fox-61-beethoven-11-28-1993 (FOX 61, 11/28/1993, 93m, 640×480). That one fits channel I better than this one.

Not found as a playable movie: D2 / D3 (openings only), Like Mike (only the sequel listing, and it is not a clean movie file), Little Big League, Ladybugs (1992), The Little Rascals (1994) — IA hits were Our Gang shorts, not the 1994 film.

### B. 80s / 90s Family Comedy

Pitch: the live-action comedies that are not already on 90s Classics (Matilda, Jumanji, Heavyweights, Blank Check, etc. stay put).

| Title | IA | What it is | Probe |
|---|---|---|---|
| Hook (1991) | https://archive.org/details/hook-1991-1080p-blu-ray-yts.-mx | Full movie, 1080p | h264 1920×800, 142m, aac untagged. File: `Hook.1991.1080p.BRrip.x264.YIFY.mp4` |
| The Neverending Story (1984) | https://archive.org/details/the-neverending-story_202406 | Full movie, VHS-source 720p | h264 1280×720, 94m, aac untagged. File: `The Neverending Story.mkv` |
| The Princess Bride (1987) | https://archive.org/details/the-princess-bride_202402 | Full movie | h264 1280×720, 98m, eac3 6ch untagged. File: `The Princess Bride.mp4` |
| The Goonies (1985) | https://archive.org/details/the-goonies-1985_202510 | Full-ish movie (97m vs the usual 114m; likely a tighter/TV cut) | h264 1092×800, 97m, aac untagged. A 114m 1080p file lives inside `the.-goonies.-1985.` — use only `The.Goonies.1985..mp4`; that item also contains Matilda and WALL-E, so do not ingest the whole item |
| MouseHunt (1997) | https://archive.org/details/mousehunt1997_202001 | Full movie | h264 1280×720, 98m, aac untagged |
| Baby’s Day Out (1994) | https://archive.org/details/babys-day-out-1994-full-movie | Full movie | h264 1280×688, 99m, aac untagged |
| Problem Child (1990) + Problem Child 2 | https://archive.org/details/problem-child and https://archive.org/details/problem-child-2 | Full movies, low-res AVI | mpeg4 640×352 / mp3, 78m and 87m. ExoPlayer already plays AVI |
| 3 Ninjas collection (1992–1995) | https://archive.org/details/3-ninjas | Full set of 3 movies | h264 1280×720, sample 96m. Files: `3 Ninjas 1.mp4`, `3 Ninjas 2 Knuckle Up.mp4`, `3 Ninjas 3 Kick Back.mp4` (the 2 / 3 labels may be swapped vs the official titles). A sharper first film only is at `3-ninjas_202307` (1904×1072) |
| Mrs. Doubtfire (1993) | https://archive.org/details/mrs....-doubtfire..-full-movie..-hd | Full movie | **vp9 / opus** 1280×544, 125m. Test on the onn box first; VP9 is usually fine, but it is a different codec than the rest of the lineup |
| Uncle Buck (1989) | https://archive.org/details/uncle-buck-1989-from-bbc-one-on-new-years-day-2005 | Full movie, BBC One New Year’s Day 2005 airing (PAL runtime) | h264 640×480, 94m, aac untagged |
| Spaceballs (1987) | https://archive.org/details/spaceballs-1987-vhs-english-film | Full movie, VHS | h264 720×480, 97m, aac untagged |
| Encino Man (1992) | https://archive.org/details/encino.-man.-1992.720p.-webrip.x-264.-aac-yts.-mx | Full movie, 720p (preferred over the 960p 4:3 copy) | h264 1280×692, 88m, aac untagged |
| First Kid (1996) | https://archive.org/details/first-kid-1996-1080p | Full movie, 1080p | hevc 1920×1036, eac3, 101m. File: `First Kid (1996) - [1080p].mkv` |
| George of the Jungle (1997) | https://archive.org/details/george-of-the-jungle-1997 | Full movie, 1080p | h264 1920×1024, 92m, aac untagged. A 1472×1080 VHS-style copy is at `disneys-george-of-the-jungle-vhs-1997` |
| Small Soldiers (1998) | https://archive.org/details/1998-small-soldiers-1998-dreamworks-vhs-480p-h-264 | Full movie, VHS | h264 720×486, 112m, aac untagged |
| Stuart Little (1999) | https://archive.org/details/stuart-little-1999_20260222 | Full movie, labeled extended cut | h264 1280×720, 90m, aac untagged |

Not found as a direct playable file: Honey, I Shrunk the Kids (only the TV series, openings, or a 15-minute fragment); Honey, I Blew Up the Kid (ZIP only — the app cannot open it); Dennis the Menace (1993) movie (cartoon sets only); The Parent Trap (1998) as a clean standalone movie; Freaky Friday (2003); Free Willy; My Girl.

### C. Halloween / Spooky Night

Pitch: a October channel of movies. Goosebumps is already on Fox Kids, Are You Afraid of the Dark is already on Nickelodeon 90s, and the Halloweentown films are already on the DCOM channel — reuse those later if you want, but they are not new.

| Title | IA | What it is | Probe |
|---|---|---|---|
| The Monster Squad (1987) | https://archive.org/details/the.-monster.-squad.-1987.1080p.-blu-ray.x-264-yts.-ag | Full movie, 1080p | h264 1920×816, 82m, aac untagged |
| The Witches (1990) | https://archive.org/details/the.-witches.-1990.1080p.-blu-ray.x-264 | Full movie, 1080p | h264 1920×1072, 92m, aac untagged |
| The Addams Family (1991) | https://archive.org/details/the-addams-family_202512 | Full movie | h264 640×480, 99m, aac untagged. File: `The Addams Family.mp4` |
| Ernest Scared Stupid (1991) | https://archive.org/details/ernest-scared-stupid | Full movie, 1080p | h264 1920×1080, 92m, aac untagged |
| Labyrinth (1986) | https://archive.org/details/Popcornarchive-labyrinth1986 | Full movie, 720p (preferred) | h264 1280×720, 101m, aac untagged. A 708×358 copy is at `labyrinth_202303` |
| The Dark Crystal (1982) | https://archive.org/details/the-dark-crystal-vhs-release-1994 | Full movie, VHS (preferred over the 360p copy) | h264 706×436, 93m, aac untagged |
| The Nightmare Before Christmas (1993) | https://archive.org/details/the_nightmare_before | Full movie, plus bonus shorts. English + French listed | h264 718×388, 76m, aac untagged. Use only `03 The Nightmare Before Christmas.mp4` (low-res). The item also has Vincent, Frankenweenie, and a making-of — skip those unless you want extras |
| Gremlins (1984), NITV with ads | https://archive.org/details/gremlins-nitv | Full movie, 1080p broadcast with commercials (also fits channel I) | h264 1920×1080, 113m, aac untagged, English tagged. File: `Gremlins NITV (ads included).mp4` (4.5 GB). A no-ads pan-and-scan file is in the same item |

Not found as a playable movie: Hocus Pocus (1993) — no real feature, only openings, a wrong-title “Hocus Pocus 2 And The Yakuza,” and reviews. Casper (1995) — previews and fragments only. Beetlejuice (1988) the live-action film — no clean feature (the 1989 cartoon series is on IA if you ever want that). Addams Family Values — a RAR archive only, not playable.

### D. Nickelodeon Movies

Pitch: the theatrical / made-for-cable Nick movies that are not already in the lineup (The Rugrats Movie, Harriet the Spy, and Jimmy Neutron already are).

| Title | IA | What it is | Probe |
|---|---|---|---|
| Clockstoppers (2002) | https://archive.org/details/Clockstoppers | Full movie | h264 720×540, 102m, aac untagged. File: `Clockstoppers.mp4` |
| Rugrats in Paris (2000) | https://archive.org/details/2022-10-22-12-53-29 | Full movie, 2001 VHS capture | h264 640×480, 92m, aac untagged |
| Rugrats Go Wild (2003) | https://archive.org/details/rugrats-go-wild-2003-fanmade-vhs_202406 | Full-length, labeled a fan-made VHS reconstruction (110m vs the usual 80m, so it likely includes previews) | h264 1280×720, 111m, aac untagged |
| The Wild Thornberrys Movie (2002) | https://archive.org/details/the-wild-thornberrys-movie_360_202607 | Full movie, very tight letterbox | h264 640×272, 85m, aac untagged |

Not usable: Good Burger and Snow Day exist on IA only as ZIP/RAR, which the app cannot play. Hey Arnold! The Movie at `turner_video_49136` is a 2-minute clip. Barnyard at `barnyard-full-screen` is a DVD `VIDEO_TS` of VOB files, not a single playable movie.

### E. DCOM Volume 2 (later Disney Channel movies)

Pitch: fill-ins for the existing DCOM channel (station 20 already has the early run: Halloweentown, Zenon, Brink!, Smart House, and so on). These would also work as their own “DCOM 2002–06” channel.

| Title | IA | What it is | Probe |
|---|---|---|---|
| Cadet Kelly (2002) | https://archive.org/details/cadet.kelly.2002.720p.hdtv.x264-regret | Full movie, 720p | h264 1262×714, 100m, aac untagged |
| Cadet Kelly, 2006 broadcast with commercials | https://archive.org/details/cadet-kelly-2006 | Same movie, wand intro + ads (also fits channel I) | h264 704×478, 112m, aac untagged |
| Twitches (2005) | https://archive.org/details/Twitches | Full movie, 360p | h264 640×360, 86m, aac untagged |
| Cow Belles (2006) | https://archive.org/details/cow-belles_202403 | Full movie, 360p | h264 640×360, 90m, aac untagged |
| The Cheetah Girls (2003) | https://archive.org/details/the.-cheetah.-girls.-2003.1080p.-upscaled.-ddp.-5.1.-h.-265-edge-2020 | Full movie, 1080p upscale | hevc 1440×1072, eac3 6ch, 93m |
| Wendy Wu: Homecoming Warrior (2006) | https://archive.org/details/1080_20220708 | Full movie, 720p. Awkward identifier; the item title is Wendy Wu | h264 1280×720, 91m, aac untagged. File: `1080.mp4` |
| Read It and Weep, Disney Channel with commercials | https://archive.org/details/read-it-and-weep-disney-channel-broadcast-woc | Full movie + original bumps/ads, 96m vs the usual 84m | h264 968×720, 96m, aac untagged |
| High School Musical 1, 2, and 3 | https://archive.org/details/high-school-musical-2_full-collection | Full set of 3 movies | h264 ~720×572. Files: `High School Muiscal.mp4` (typo, HSM1, 94m), `High School Musical 2.mp4` (107m), `High School Musical 3 (Senior Year).mp4` (112m) |

Not found as a playable movie: Get a Clue, Pixel Perfect, Jump In, Stuck in the Suburbs, Go Figure, Right on Track, Twitches Too. Several of those exist only as credits, openings, or unrelated items.

### F. Muppets & Henson

Pitch: a Jim Henson channel for you and the kids. Muppet Treasure Island is already on 90s Classics; The Muppet Christmas Carol is already on Christmas Movies; only holiday scraps of Muppet Babies / Fraggle are in the lineup today.

| Title | IA | What it is | Probe |
|---|---|---|---|
| The Great Muppet Caper (1981) | https://archive.org/details/the-great-muppet-caper_202501 | Full movie, 720p | h264 1280×720, 98m, aac untagged. File: `The Great Muppet Caper.mkv` |
| The Muppets Take Manhattan (1984) | https://archive.org/details/the-muppets-take-manhattan-1999-vhs | Full movie, 1999 VHS | h264 640×426, 104m, aac untagged |
| Emmet Otter’s Jug-Band Christmas (1977) | https://archive.org/details/emmet_otters_jug-band_christmas | Full special + extras, English tagged | h264/mkv 710×480, 51m. Use `Emmet Otter's Jug-Band Christmas (1977).mkv`; leave the bloopers/documentary out unless you want them |
| The Christmas Toy (1986) | https://archive.org/details/the-christmas-toy-1986 | Full special, restored | h264 640×480, 50m, aac untagged |
| Tales from Muppetland: The Frog Prince (1971) | https://archive.org/details/tales-from-muppetland-the-frog-prince-1971 | Full special, laserdisc rip | mpeg2 720×480, 51m |
| Muppet Babies (1984) | https://archive.org/details/muppet_babies | **Full series, 107 episodes** (that is the complete count) | h264 640×480, ~24m, aac untagged. Sample: `S2E07 I Want My Muppet T.V..mp4`. A 59-episode fan remaster is at `JHMB84` if you ever want a sharper partial set |
| Fraggle Rock | https://archive.org/details/MashSeries | **Full series, 96 English-titled episodes** (the complete US run). The identifier is oddly `MashSeries`, but the files are Fraggle Rock S01E01 “Beginnings” onward | Originals are Cinepack AVI 720×480, ~25m. ExoPlayer already plays AVI; IA also made 480p MP4 derivatives if a box ever chokes on Cinepack |
| Labyrinth / The Dark Crystal | (see Halloween) | Full movies; they can live here instead of (or as well as) the Halloween channel | — |

The Muppet Movie (1979) is on IA (`the-muppet-movie-extended-vhs`) only as a DVD `VIDEO_TS` — the first VOB probed was a 23-minute disc chunk, not the whole film. Skip it until a single-file copy shows up. A UK “special edition” item also looks like a disc image.

### G. Nick Game Shows

Pitch: a whole channel of messy Nick studio shows. Legends of the Hidden Temple is already on Nickelodeon 90s. Double Dare (1986 + 1988) and Nickelodeon GUTS (S1–3 + Global GUTS, 1080p) were verified in research-2 and are still unused — they belong here if you want the channel, but they are not new finds.

| Title | IA | What it is | Probe |
|---|---|---|---|
| Figure It Out, seasons 1–4 | https://archive.org/details/figure-it-out-complete-series-proper | Full (or virtually full) series, 159 files / ~161 known episodes, 720p | h264 1280×720, ~26m, aac untagged. Sample: `Season 2 Episode 6.mp4`. A same-sized mirror exists under a messier identifier |
| Super Sloppy Double Dare (1987) complete | https://archive.org/details/supersloppydoubledare-1987 | Full set, 24 episodes | h264 640×480, ~24m, aac untagged |
| Nick Arcade | https://archive.org/details/nick-arcade-all | Near-complete, 83 episodes (the run is a bit over 100). 480p HEVC | hevc 640×480, ~24m, aac untagged. A 71-episode 1080p set is at `nick-arcade-1992-s-02-e-02-altresse-katy-vs.-ty-dana` if you prefer looks over count |
| Get the Picture | https://archive.org/details/getthepicture-11 | **Partial**, 11 episodes | h264 640×480, ~29m |
| Family Double Dare (FOX, April 1988) + I’m Telling, with commercials | https://archive.org/details/20240803_20240803_1920 | **Partial**: one 75-minute block, not a series | h264 720×480, 75m, aac untagged |
| Wild & Crazy Kids | https://archive.org/details/1990-nickelodeon-wild-and-crazy-kids-woc-720p | **Partial**: a single 24-minute episode with commercials, 720p | h264 960×720, 24m, aac untagged |

### H. Classic Sitcoms / TGIF fill

Pitch: longer sitcom sets to sit beside the existing TGIF channel (which is mostly Family Matters / Step by Step / Boy Meets World as Friday-night blocks, not complete series).

| Title | IA | What it is | Probe |
|---|---|---|---|
| Sabrina the Teenage Witch (1996) | https://archive.org/details/sabrina-the-teenage-witch-complete | **Full series, 163 episodes** (the complete run) | hevc 720×576, ~22m, aac untagged. Amazon WEB-DL x265. Sample filename includes `S05E15` |
| Sister, Sister seasons 1–2 | https://archive.org/details/sister-sister-1x-02-first-dates | Partial, 31 episodes | h264 720×480, ~23m |
| Sister, Sister season 4 | https://archive.org/details/sister-sister-s-4 | Partial, 22 episodes (S4 is complete; S3, S5, S6 were not found) | h264 708×478, ~22m |
| All That | https://archive.org/details/season-2-episode-all-that-partial-series-proper | **Partial**, 117 files of a ~180-episode run | h264 640×480, ~24m, aac untagged |

Not found as a complete playable set: The Fresh Prince of Bel-Air, Full House, Boy Meets World (beyond the TGIF blocks you already have), Kenan & Kel (the TV-movie listing did not yield a playable file in this pass). Home Improvement (complete DVD rip) and Saved by the Bell + College Years were verified in research-2 and are still unused.

### I. Saturday Night Movie (TV broadcasts with commercials)

Pitch: the “taped off TV” versions. This is the most nostalgia-TV of the movie ideas. Several titles also appear in cleaner cuts on the channels above; you’d pick one version each.

| Title | IA | What it is | Probe |
|---|---|---|---|
| Gremlins (1984), NITV with ads | https://archive.org/details/gremlins-nitv | Full movie + commercials, 1080p | See Halloween. Use `Gremlins NITV (ads included).mp4` |
| Superman II, KSFY 4/3/1988 | https://archive.org/details/superman.-ii.-ksfy.-4.3.1988deraq | Full Sunday-night-style airing, 177m | h264 640×480, 177m, aac untagged. Practical copy |
| Superman II, ABC Sunday Night Movie, Dec 29, 1985 | https://archive.org/details/1985abcsuperman2full | Same idea, original ABC airing with commercials, English tagged | The original is a **55.6 GB ProRes MOV** (178m, 704×480). Do not point the app at that file. IA also made a 1.1 GB h264 MP4 derivative (`1985-ABC-SupermanII-FULL.mp4`) which is the only sane playback option here, even though it is a derivative |
| Cadet Kelly, 2006, with commercials | https://archive.org/details/cadet-kelly-2006 | Full DCOM + wand intro + ads | 112m, 704×478 |
| Read It and Weep, Disney Channel with commercials | https://archive.org/details/read-it-and-weep-disney-channel-broadcast-woc | Full DCOM + bumps/ads | 96m, 968×720 |
| Beethoven, WTIC FOX 61, 11/28/1993, with commercials | https://archive.org/details/wtic-fox-61-beethoven-11-28-1993 | Full movie + ads | 93m, 640×480 |
| Family Double Dare + I’m Telling, FOX/NBC 1988, with commercials | https://archive.org/details/20240803_20240803_1920 | One game-show block, not a movie, but it is a clean WOC capture | 75m, 720×480 |
| Space Jam (1996) theatrical recording | https://archive.org/details/spacejam-trb-vhs-aud-tgyhujhygtfrtgyhyy | Audience VHS, slightly short | See Sports |
| Little Giants VHS recording | https://archive.org/details/littlegiantsvhsrecording | Home-tape capture of the movie | See Sports |

Who Framed Roger Rabbit as a Cartoon Network broadcast (`vts-01-1_20210131`) is a DVD `VIDEO_TS`; the first VOB is a 0.1-minute menu, so it is a poor fit for the app. A Batman Returns NBC Sunday Night Movie item appeared in search but its metadata could not be fetched this round, so it is unverified.

### J. Don Bluth / early-90s theatrical animation

Pitch: the non-Disney theatrical cartoons that are not already on 90s Classics (Anastasia, Land Before Time, Rock-a-Doodle, Swan Princess, The Pagemaster, and Cats Don’t Dance already are).

| Title | IA | What it is | Probe |
|---|---|---|---|
| FernGully: The Last Rainforest (1992) | https://archive.org/details/fergully-16-x-9-1 | Full movie | h264 852×480, 76m, aac untagged. File: `FERGULLY_16X9_1.mp4` |
| FernGully II: The Magical Rescue (1998) | https://archive.org/details/ferngully-ii-the-magical-rescue-1998-dvd | Full movie | h264 960×720, 70m, aac untagged |
| Once Upon a Forest (1993) | https://archive.org/details/once-upon-a-forest-1993-laserdisc-rip | Full movie, laserdisc | h264 960×720, 76m, aac untagged |
| A Troll in Central Park (1994) | https://archive.org/details/a-troll-in-central-park-1994 | Full movie, softer SD | mpeg4 576×432, 73m, untagged. A 1080p listing exists (`a.-troll.-in.-central.-park.-1994.1080p.-webrip.x-264.-aac-yts.-mx`) but was not probed this round |

The Secret of NIMH appeared only as a DVD ISO. Balto appeared only as DVD ISOs. Thumbelina (1994) and The Pebble and the Penguin (1995) have 1080p listings (`thumbelinafullmovie1994`, `the.-pebble.-and.-the.-penguin.-1995.1080p.-blu-ray.x-264.-aac-5.1-yts.-mx`) that were not successfully probed this round, so they are unverified. An American Tail (1986) was not confirmed as a clean English feature (Fievel Goes West is already on VHS Kids Movies).

### K. Anime movie night (plus Hamtaro)

Pitch: a weekend movie block next to Toonami. My Neighbor Totoro is already on VHS Kids Movies, so it is omitted. Pokémon movies 2000 / 3 / 4Ever / Heroes and Digimon: The Movie are already on 90s Classics; The First Movie is not.

| Title | IA | What it is | Probe |
|---|---|---|---|
| Pokémon: The First Movie — Mewtwo Strikes Back (1998) | https://archive.org/details/pokemon-the-first-movie-mewtwo-strikes-back-1998 | Full movie, 4K HEVC | hevc 3840×2160, 75m, **three untagged audio tracks** (aac 2ch, dts, dts). File is **13.2 GB** — the onn box can decode HEVC, but this will be slow to start. Worth a test before adding |
| Yu-Gi-Oh! The Movie: Pyramid of Light, English dub | https://archive.org/details/yu-gi-oh-the-movie-full-movie-english-dubbed | Full movie, 1080p | h264 1920×1080, 90m, aac untagged |
| Castle in the Sky (1986) | https://archive.org/details/castle-in-the-sky_202505 | Full movie | mpeg2 720×480, 125m, untagged. File: `Castle in the sky.mkv` |
| Princess Mononoke (1997) | https://archive.org/details/princess.-mononoke.-1997-hepburnzyk | Full movie, 1080p (preferred) | h264 1920×1024, 133m, aac untagged. A 480p copy is at `princess-mononoke_202404` |
| Spirited Away (2001) | https://archive.org/details/spirited-away-2001-1080p | Full movie, 1080p, labeled dual audio Japanese + English | h264 1920×1040, 125m, **two untagged tracks** (dts 7ch, ac3 6ch). **Do not assume English is first** — this is the same class of risk as the old Wizards / Tarzan items. The original MKV is 10.6 GB |
| Hamtaro, English dub, episodes 1–104 | https://archive.org/details/hamtaro-enhanced-720p-episodes-1-104 | Full English series (104 of 104 dubbed episodes), 720p | hevc 960×720, ~21m, aac untagged. A 480p English set with slightly messier files is at `hamtaro_complete` |

Cowboy Bebop: The Movie has a 1080p listing (`cowboy.-bebop.-the.-movie.-2001.1080p.-blu-ray.x-264.-aac-yts.-mx`) that was not probed (the identifier in the first pass was truncated). Treat it as unverified. The DVD-ISO copy is not useful to the app.

### L. Toy-commercial / arcade-ad extra (light add-on, not a full channel by itself)

Pitch: extra fuel for the fake-commercial-break idea, or a short block next to Retro Commercials (station 32 already has 94 ads, including some Nintendo).

| Title | IA | What it is | Probe |
|---|---|---|---|
| Batteries Not Included: vintage toy commercials | https://archive.org/details/batteriesnotincluded_2009 | Full compilation, ~58 minutes of classic toy ads | mpeg2 720×480, 58m. Original file: `Batteries_2009.mpg` (2.5 GB). ExoPlayer already plays MPEG-2 |
| 80s/90s Toy Commercial Compilation | https://archive.org/details/80s-90s-toy-commercial-compilation-nostalgia-720p | Short 10-minute compilation, 720p | h264 1280×720, 10m, aac untagged |
| The Sega-Gremlin Tape Archive | https://archive.org/details/sega_gremlin_tape_archive | 21 promotional tapes, early-80s Sega/Gremlin *arcade* era — not 1990s Genesis commercials | Sample 15m, 1920×1080 h264. Fun, but a different vibe than Saturday-morning toy ads |

A full Nintendo or PlayStation commercial set was not found (only single short ads). An MTV TRL archive (`trl-archive`, “MTV TRL Total Request Live Archive (1998–2001)”, ~16 GB) showed up in search but was not probed, so it is unverified. MTV 90s UK video dumps also exist and were not verified.

---

## Other places besides Internet Archive

The app already plays YouTube and archive.org (plus a unused Torbox/Trakt path). Practical extras:

- **Public-domain features** on archive.org (`feature_films`) and official YouTube PD channels. You already have several Christmas PD titles (It’s a Wonderful Life, Holiday Inn, White Christmas). For Halloween, *Night of the Living Dead* (1968) is public domain in the US; 1930s/40s serials and some early Godzilla TV prints also turn up. These are the only movies I would call clearly free to keep.
- **Prelinger / classic TV commercials** on archive.org, as more raw material for the fake-break feature.
- **Official YouTube channels** sometimes post full episodes or movies for a window (Nickelodeon, Cartoon Network, PBS, studio “Movies” channels). They disappear, they are often cropped, and they are a weaker fit than a stable archive file. I would not build a channel on them without checking each link at add time.
- I did not find a legal, complete, free source for the big missing titles (Hocus Pocus, Good Burger, Honey, I Shrunk the Kids, Fresh Prince, High School Musical on an official free channel, etc.). Paid services remain the clean path for those.

---

## Notable things not available (or not usable)

- **Hocus Pocus, Casper (1995), Beetlejuice (1988 film), Honey I Shrunk the Kids, Honey I Blew Up the Kid, Good Burger, Snow Day, Hey Arnold! The Movie, The Parent Trap (1998), Freaky Friday (2003), Get a Clue, Pixel Perfect, Jump In, D2 / D3 Mighty Ducks, Like Mike, Little Rascals (1994), Little Big League, Ladybugs, Fresh Prince, Full House, The Muppet Movie as a single file, Who Framed Roger Rabbit as a CN broadcast (DVD VOBs), Addams Family Values (RAR only).**
- **ZIP/RAR-only items** (Good Burger, Snow Day, Honey I Blew Up the Kid, one Little Giants listing) cannot be pointed at by the app.
- **DVD ISO / VIDEO_TS items** (Barnyard, The Muppet Movie extended VHS, Roger Rabbit CN, Secret of NIMH, Balto, Cowboy Bebop ISO) are a poor fit for ExoPlayer as used today.
- Research-3 leftovers still unused, and still not re-pitched as “new”: Regular Show, She-Ra, Voltron, Over the Garden Wall, Infinity Train, Star vs. the Forces of Evil, Ninjago, Wander Over Yonder, Amphibia (partial), We Bare Bears (partial), Odd Squad, Peg + Cat, Hey Duggee, Nature Cat, Ben & Holly, PJ Masks.
- Research-2 leftovers still unused that would fill channels G and H quickly: Nickelodeon GUTS, Double Dare 1986/1988, Home Improvement, Saved by the Bell (plus College Years / The New Class).

