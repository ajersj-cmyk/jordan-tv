# Jordan TV: Research Round 7 (90s kids + King of Queens-style sitcoms)

Checked Monday, Nov 23, 2026, America/New_York. **Research only:** the import JSON, APK, and repo were not changed. Nothing here has been added.

Jordan asked for more 90s shows for the kids, and said he loves *The King of Queens*. The kids are **Reese (11, girl)** and **Blake (3, girl)**. Suggested channels below take that into account: preschool and gentle PBS for Blake; Nick/WB cartoons, girl-friendly live action, and a couple of mystery/adventure shows for Reese; sitcoms in the KoQ vein for Jordan (Reese can watch several of those too).

Current lineup used as the baseline: `jordan-tv-import-full.json` (36 stations, 15,567 videos, 362 unique archive.org identifiers). This list only includes shows that are **not already in the import** as a mostly-complete series. Partials already on a channel are called out only when a clearly better or more complete set exists.

## Method

- Internet Archive `advancedsearch` and the metadata API. Candidates were checked against the 362 identifiers already in the lineup and against titles already on a channel.
- One original playable file per recommended item (MP4/MKV/AVI, not IA 480p `.ia.mp4` / `_512kb.mp4` derivatives, and not ISO/VOB/ZIP/RAR) was opened with a Range request. Every recommended mid-file below returned **HTTP 206** and was ffprobe'd. Audio is listed as tagged. `untagged` / `und` means the rip did not set a language; those are English-language US/UK releases by title, but tracks were not listened to. Dual-audio items are flagged, and a set is not recommended if the default track is not English.
- Official episode counts are the commonly published totals, used only to say whether a set looks complete. Counts and URLs were not fabricated; only verified playable files are listed.

**Copyright note:** Almost all of the series below are still under copyright. These are listings already on archive.org, in the same style as rounds 1–6. Nothing is added until you pick.

---

## Already in the lineup (not re-pitched as new)

These 90s / requested shows already have a substantial or complete run on a channel:

- **Nick 90s:** Doug (117, complete Nick+Disney), Are You Afraid of the Dark (91, complete original), All That (117 of a ~180-episode run, already on Nickelodeon 90s), Gullah Gullah Island (70, on Preschool). Hey Arnold is only 20 episodes (S01 from an item that is *titled* “Complete Series” but only has 20 files). Rocko is only S01–S02 (26/52, poorly titled `getvid` files). Pete & Pete is only 15 episodes from a messy item — a better complete set is below. Rugrats, CatDog, Aaahh!!! Real Monsters, and The Wild Thornberrys are only VHS tapes or a single holiday episode, not series.
- **Disney:** Recess, Pepper Ann, Gargoyles, TaleSpin, Darkwing Duck, Bonkers, Quack Pack, Timon & Pumbaa (85 episodes already living inside the Tarzan ident), Aladdin the series. Goof Troop / Hercules the series / The Little Mermaid the series are not in as series (movies or a single aircheck only).
- **CN:** Dexter’s Laboratory, The Powerpuff Girls, Ed, Edd n Eddy, Cow and Chicken. Johnny Bravo is already essentially complete on Cartoon Network 90s (the ident has ~68 episode files through S04 plus specials). I Am Weasel is not in.
- **Kids’ WB / Fox Kids / SuperHero:** Animaniacs, Pinky and the Brain, Tiny Toons, Batman TAS, Spider-Man TAS, X-Men TAS, Bobby’s World, Eek! The Cat, Goosebumps (68/74). Freakazoid is not in.
- **PBS / Preschool:** Arthur, Wishbone, Zoboomafoo, Little Bear, Magic School Bus. Blue’s Clues is only a few VHS tapes, not the series.
- **Sitcoms / TGIF / Disney Channel:** The King of Queens (206/207), Boy Meets World (158/158), Lizzie McGuire, Family Matters. Full House, Step by Step, and The Drew Carey Show were already missing last round.

---

## 1) Preschool — especially for Blake (3)

| Show | Count | Quality | Link | Notes |
|---|---|---|---|---|
| Blue’s Clues (original) | 142 unique / 143 official (145 files; 2 extras/movie-length) | 480×360 h264 / aac `und`, ~24.5m | https://archive.org/details/blues-clues-s-03-e-59-blues-big-musical-movie | Mid-file HTTP 206. Essentially the complete 1996–2006 series. Best single add for Blake. You only have a few Blue’s Clues VHS tapes today. |
| The Big Comfy Couch | 100 / 100 | 480×360 h264 / aac `und`, ~26m | https://archive.org/details/the-big-comfy-couch | Mid-file HTTP 206. Complete. A duplicate-looking item at `the-big-comfy-couch_202108` has the same 100 files. |
| Allegra’s Window | 50 unique / commonly 50 | 640×480 h264 / aac `und`, ~24m | https://archive.org/details/allegras-window-complete-series | Mid-file HTTP 206. S01–S03 (18+22+10). You only have holiday scraps on Holiday Episodes today. |
| The Adventures of Spot (classic BBC S01–S02) | 26 / 26 for 1987–93 | 720×540 h264 / aac `und`, ~5m | https://archive.org/details/the-adventures-of-spot-the-complete-series-1987-93 | Mid-file HTTP 206. Complete for the original two series. The later 1995 “It’s Fun to Learn with Spot” (13 shorts) was not in this set. A larger VHS/DVD dump (`spot-the-dog-uk-vhs-and-dvd-collection`) only unique-counted the same 26 episodes, with duplicates. |
| Franklin (1997) | 76 unique SxxExx / 78 official (101 episode-length files, some a/b segments) | 640×480 XviD / mp3 untagged, ~12–23m | https://archive.org/details/franklin-and-friends-deep-sea-voyage | Mid-file HTTP 206. Mostly complete, mixed MP4/AVI. Gentle and right for Blake. |
| Madeline (specials + TV series) | 64 unique episode-length files (S01–S04; plus 1 longer file) | 720×480 MPEG-2 / ac3 `eng`, ~23m | https://archive.org/details/Madeline-cartoon | Mid-file HTTP 206. Item is titled “The Entire Series.” Common published totals for the specials + DIC / New Adventures run are in the high 50s to mid 60s. Also fine for Reese when she was younger; still very watchable at 11. Skip the “Madeline” yoga videos that pollute search. |
| Barney & Friends | 168 unique S01–S08 numbers, plus Backyard Gang / specials (230 original MP4s in the item; 183 in the 20–42m window) | Mid-file 960×720 h264 / aac `eng`, ~21m | https://archive.org/details/barney-friends | Mid-file HTTP 206. A large preschool set, **not** the full 14-season / commonly 268-episode run. The mid-file in this item is the 1998 special *Barney’s First Adventures*, so the item is a mix of series episodes and specials. A second item, `barneyandfriends` (159 files, later seasons through S13 but gappier), could fill some later years if you want both. |

Lamb Chop’s Play-Along only turned up a 23-episode S01-heavy set (`lamb-chops-play-along`, 23 of a commonly published 81). That is not mostly complete, so it is not in the table.

---

## 2) PBS KIDS 2000's — 90s PBS that fits the channel you already have

The channel is named “2000's” but already holds Arthur, Wishbone, Zoboomafoo, Between the Lions, and Magic School Bus, so these belong there. Shining Time and Reading Rainbow are also excellent for Blake; Ghostwriter is a better fit for Reese (11).

| Show | Count | Quality | Link | Notes |
|---|---|---|---|---|
| Reading Rainbow | 155 / 155 | 640×480 h264 / eac3 `eng`, ~28m, Amazon WEB-DL | https://archive.org/details/ReadingRainbowTVSeries | Mid-file HTTP 206. Complete, English-tagged audio, cleanest PBS find this round. |
| Shining Time Station | 65 unique main episodes (official main run is 65) in a 104-file 1080p item | 1440×1080 h264 / aac `und`, ~29m | https://archive.org/details/shining-time-station-TV-series-CompleteHighQuality | Mid-file HTTP 206. Best-looking kids set this round. A 480p item, `shining-time-station-complete-series` (77 files), adds the six *Mr. Conductor’s Thomas Tales* specials if you want those too. |
| Kratts’ Creatures (1996) | 50 / 50 | 640×480 h264 / eac3 `eng`, ~28m, Amazon WEB-DL | https://archive.org/details/KCTVSeries | Mid-file HTTP 206. Complete. This is the 90s show, not the *Wild Kratts* you already have. An all-MP4 copy with the same 50 episodes is at `kratts-creatures-complete-series`; the WEB-DL is the cleaner of the two. |
| Ghostwriter (1992) | 74 files / 74 official | 432×320 MPEG-4 / mp3 untagged, ~27m, AVI | https://archive.org/details/ghostwriter_1992 | Mid-file HTTP 206. Looks complete, but it is a soft old AVI rip. Mystery / literacy series — much more Reese than Blake. The “Season One DVD” item (`ghostwriter-season-one`) had no original playable files. |

---

## 3) Nickelodeon 90s — fills and one upgrade

| Show | Count | Quality | Link | Notes |
|---|---|---|---|---|
| Clarissa Explains It All | 65 files / 65 official (numbered 101 through 513, ending at “The Last Episode”) | Mid-file 640×480 h264 / aac untagged, ~24m, Hulu WEBRip (item also has some AVI/MP4) | https://archive.org/details/clarissa-explains-it-all_202611 | Mid-file HTTP 206. Complete. A great Reese add. Separate 720p season packs exist but are incomplete by themselves (S02 only has 6 files); this one item is the one to use. |
| The Adventures of Pete & Pete (upgrade) | 39 episode-length files, S01–S03 numbered 13+13+13 | 1408×960 h264 / aac `eng`, ~24m | https://archive.org/details/theadventuresofpeteandpete | Mid-file HTTP 206. Much cleaner than the 15 episodes currently in the lineup from `the_adventures_of_pete_and_pete` (which also has reunion clips and extras). The official half-hour run is commonly 34 (S01 is 8, plus earlier specials). This set numbers 13 per season, so it likely includes specials in S01. Treat it as a replacement/upgrade, not a second copy. |

All That is already on this channel at 117 episodes (partial of ~180). I did not find a more complete playable set.

---

## 4) Kids’ WB

| Show | Count | Quality | Link | Notes |
|---|---|---|---|---|
| Freakazoid! | 24 / 24 | 512×384 h264 / aac `und`, ~21.5m | https://archive.org/details/freakazoid_202210 | Mid-file HTTP 206. Complete S01–S02. A second “complete” item (`freakazoid-complete-series`, 28 files) is a bit messier (short files + mixed season folders). Use the 24-episode set. Reese-age cartoon, not for Blake. |

---

## 5) Sitcoms — King of Queens neighbors, plus 90s kid/family shows for Reese

These would go on the existing **Sitcoms** channel next to *The King of Queens*. *Sister, Sister* and *Smart Guy* are the ones Reese is most likely to like; the rest are for Jordan (and fine for an 11-year-old in the room).

| Show | Count | Quality | Link | Notes |
|---|---|---|---|---|
| Yes, Dear | 122 / 122 | Mid-file 720×480 h264 / aac `und`, ~21m | https://archive.org/details/yes-dear | Mid-file HTTP 206. Complete. Closest “I like Raymond / King of Queens” add. Some files in the metadata look 384p, but the probed mid-file is 480p. |
| Still Standing | 88 / 88 | 512×384 XviD / mp3 untagged, ~22m, AVI | https://archive.org/details/stillstanding2002 | Mid-file HTTP 206. Complete. Softer than the MP4 season packs, but the one-item complete set is the simplest. MP4 season packs also exist (S01–S04) if you would rather assemble 360p MP4s. |
| Grounded for Life | 91 / 91 | 720×400 h264 / aac `eng`, ~22m | https://archive.org/details/101_20250815 | Mid-file HTTP 206. Complete. S01 is named `101.mp4`–`115.mp4`; S02–S05 use regular SxxExx names. Odd identifier, real show. |
| NewsRadio | 97 / 97 (drop a bloopers reel and a promos file) | 480×360 h264 / aac `eng`, ~22m | https://archive.org/details/newsradio-1995-99 | Mid-file HTTP 206. Complete S01–S05. |
| Reba | 123 unique / 127 official (129 episode-length files; a few shorts in the item should be dropped) | 720×480 MPEG-2 / default ac3 `eng` (track 2 is `spa`) | https://archive.org/details/reba-complete-series | Mid-file HTTP 206. Same dual-audio pattern as The Nanny rip: default is English, Spanish is not first. Mostly complete. |
| Coach | 200 unique / commonly 200, assembled from nine season items, all 480p MP4 | Mid-files 632–640×480 h264 / aac `eng` or `und`, ~21–24m | S01 https://archive.org/details/coach-season-1_202311 · S02 https://archive.org/details/coach-season-2_202311 · S03 https://archive.org/details/coach-season-3_202311 · S04 https://archive.org/details/coach-season-4 · S05 https://archive.org/details/coach-season-5 · S06 https://archive.org/details/coach-season-6 · S07 https://archive.org/details/coach-season-7 · S08 https://archive.org/details/coach-season-8 · S09 https://archive.org/details/coach-season-9 | S01 and S05 mid-files both HTTP 206. Looks like a complete run if you take all nine items together. |
| Mad About You | 159 unique / 164 official original run | 352×240 h264 / aac `und`, ~22m, single audio track | https://archive.org/details/mad-about-you-complete-series | Mid-file HTTP 206. Nearly complete, but soft 240p. **Do not use** `mad.about.you.1992.complete` as-is: that 480p Amazon WEB-DL is sharper and includes the 2019 revival (176 files), but the mid-file’s **default audio is Portuguese** (`por` then `eng`). |
| Sister, Sister | 119 unique / 122 official, from six season items (12+19+22+22+22+22) | 708×478 h264 / aac `eng`, ~22–23m | S01 https://archive.org/details/sister-sister-s-1 · S02 https://archive.org/details/sister-sister-s-2 · S03 https://archive.org/details/sister-sister-s-3 · S04 https://archive.org/details/sister-sister-s-4 · S05 https://archive.org/details/sister-sister-s-5 · S06 https://archive.org/details/sister-sister-s-6 | S01 and S03 mid-files HTTP 206. Research-4 only had S01–S02 and S04; S03, S05, and S06 are on Archive now. Short a few early-season episodes. Excellent for Reese. Could also live on a new 90s Kids channel or next to TGIF, but Sitcoms is the cleanest existing fit. |
| Smart Guy | 50 episode-length files / 51 official (unique SxxExx 48; S01 is missing at least E02, and may be short one more depending on numbering) | 480×360 h264 / aac `eng`, ~22m | https://archive.org/details/SmartGuySeason3Episode18Crushed | Mid-file HTTP 206. Mostly complete. Good Reese sitcom. The identifier is named after one episode; the item actually holds the series. |

---

## 6) Girl-friendly extras (Reese)

These can go on a new **90s Kids** channel, or on the existing homes noted.

| Show | Count | Quality | Link | Suggested channel | Notes |
|---|---|---|---|---|---|
| The Baby-Sitters Club (HBO, 1990) | 10 / 13 | 720×576 h264 / eac3 `eng`, ~27.5m | https://archive.org/details/the-baby-sitters-club-s-01-e-05-stacey-takes-a-stand | New 90s Kids, or Sitcoms | Mid-file HTTP 206. Near-complete, three episodes short. Very Reese. |
| Sailor Moon, original DIC English dub, season 1 | 40 / 40 for DIC S01 only (not the full English run) | 640×480 MPEG-4 / aac `und`, ~22m | https://archive.org/details/sailor-moon-complete-s01-dic-dub | Toonami Anime, or 90s Kids | Mid-file HTTP 206. Same leftover set from research-5, still unused. A “complete English” listing had no playable files. The live-action *Pretty Guardian Sailor Moon* item is English **subtitles**, Japanese audio — not recommended as an English-default set. |

A new **90s Kids** channel would also be a natural home if you would rather not mix *Clarissa*, *Pete & Pete*, *Sister, Sister*, *Smart Guy*, *Freakazoid*, and *Baby-Sitters Club* onto the existing Nick / Sitcoms / WB channels. I would still put the preschool and PBS shows on Preschool and PBS KIDS, not on a catch-all 90s Kids channel, so Blake has a safe place to land.

---

## 7) Still-unused leftovers from research 4–5 (not new, and not really “90s,” but still verified)

These were already verified in earlier rounds, were never added, and are still playable. They are a better fit for Reese than for Blake, and they are early-2000s rather than 90s.

| Show | Count | Quality | Link |
|---|---|---|---|
| Danny Phantom | 49 / 53 | 640×480 h264 / aac untagged, ~24m | https://archive.org/details/danny-phantom-complete-series-480p |
| The Angry Beavers | Looks complete (126 files / 62 official episodes, 11–12m segments, plus extras) | 716×476 HEVC / aac `eng`, ~12m | https://archive.org/details/angry-beavers-complete |
| Codename: Kids Next Door | 144 segment files; official run is 78 half-hours plus specials | 1440×1080 HEVC / eac3 `eng`, ~11m | https://archive.org/details/codename-kids-next-door-full-series_202611 |
| Hamtaro, English dub | 104 / 104 dubbed episodes | 960×720 HEVC / aac untagged, ~20m | https://archive.org/details/hamtaro-enhanced-720p-episodes-1-104 |

Johnny Bravo already has a nearly complete run on Cartoon Network 90s, so the leftover `johnny-bravo-complete` (185 segment files) is only a quality/organization upgrade, not a missing show.

---

## 8) What I could not find (or would not add)

**90s Nick series still missing as playable, mostly-complete English sets**

- **Hey Arnold!** — The item already in the lineup (`hey-arnold-1996`) is titled “Complete Series 1080p” but only contains 20 S01 files. I did not find the other 80 episodes as a playable set (plenty of marathons, airchecks, the 2-minute “movie” clip, and a DVD unboxing).
- **Rocko’s Modern Life as a complete series** — You already have S01–S02 (26/52). I did not find a playable S03–S04 collection; later seasons exist mainly as one-off `getvid` episode items.
- **Rugrats (the main series)** — Lots of VHS compilations and the movies you already have. No playable complete or mostly-complete episode set. *Rugrats: Pre-School Daze* (`rugrats-pre-school-daze`) is a 4-episode spin-off, not the main show. I did not treat it as a series add.
- **CatDog, Aaahh!!! Real Monsters, The Wild Thornberrys** — No playable complete series. Theme-song clips, VHS tapes, pilots, and movies only. (A *Thornberrys* / *Rugrats* movie leftover from research-4 is a different question.)
- **Kenan & Kel** — No playable English series set. The complete-looking item is **Spanish Latin American audio** (`kenan-y-kel-esp-latino`). The movie *Two Heads Are Better Than None* exists as a standalone. Credits clips and one-off airchecks are not a series.
- **All That, more complete than the 117 you already have** — Not found.

**Disney Afternoon / One Saturday Morning still missing**

- **Goof Troop, Hercules: The Animated Series, The Little Mermaid TV series** — VHS volumes, single episodes, airchecks, or the theatrical movies only. No playable complete series. Chip ’n Dale Rescue Rangers was already a miss in research-5.

**Cartoon Network**

- **I Am Weasel as a clean complete set** — Items titled “Full Series” / “Complete Series” had only 4 and 9 files. A mixed *Cow and Chicken* / *I Am Weasel* dump (`fred-last-of-the-idiots`, 163 short MP4s) is messy (numbered `001.mp4` files plus both shows). I would not add it without a lot of hand sorting, and *Cow and Chicken* is already on Cartoon Network 90s.

**PBS / preschool misses or too partial**

- **Lamb Chop’s Play-Along** — Only 23 playable episodes in one item, plus scattered one-off episode items. Not a mostly-complete set.
- **Spot series 3** (1995) was not in the clean 26-episode set.

**Live-action / sitcoms still missing**

- **Full House** — Still no playable complete (or even mostly-complete) English set. Hits were the theme song, a UK series of the same name, or finale bumpers.
- **Step by Step** — Still no playable series set. Search is flooded with “step by step” tutorials, hajj guides, and a single Christmas aircheck.
- **The Drew Carey Show** — Still no individual-episode set. What exists are 8–10 hour **concatenated season dumps** for S01–S04 and S06 only (one MP4 per season), which would play as a single multi-hour “episode” in shuffle. Missing S05, S07–S09 in that form anyway. Same no as last round, with a slightly clearer picture of why.
- **According to Jim** — Only the pilot (`according-to-jim`) plus closing-credits rips.
- **George Lopez** — `gl-fullseries` is only 26 episodes of a 120-episode run, not mostly complete.
- **My Wife and Kids, Everybody Hates Chris, Becker, Wings, Just Shoot Me, Spin City** — No playable mostly-complete English episode set. The Just Shoot Me item titled “season 1 to 7 Full episodes” (`3-e-21`) had **zero original playable files**. Becker search was polluted by Alan Becker animation. Wings/Spin City hits were mostly TV-tuner single airchecks.

**Audio / format rejects**

- **Mad About You 480p WEB-DL** (`mad.about.you.1992.complete`) — Sharper, and includes the 2019 revival, but default audio is Portuguese. Not recommended unless someone remuxes English first.
- **Kenan & Kel S01–S04 Latin American Spanish** — Wrong default language.
- **Pretty Guardian Sailor Moon** — English subs, not an English dub.
- ISO/RAR/DVD-image items (Shining Time and Ghostwriter “DVD” listings, Big Comfy Couch S05 ISO, etc.) — The app cannot play those.

---

## If you want a short priority list

For **Blake (3):** Blue’s Clues, Big Comfy Couch, Allegra’s Window, Shining Time Station, Spot, Franklin, then Barney and Madeline.

For **Reese (11):** Clarissa, Sister, Sister, Smart Guy, Freakazoid, Ghostwriter, Reading Rainbow / Kratts’ Creatures, Baby-Sitters Club, Sailor Moon DIC S01, and the Pete & Pete upgrade. Danny Phantom / Kids Next Door remain easy later adds if you want early-2000s Nick/CN.

For **Jordan (King of Queens):** Yes, Dear (complete, 480p), Grounded for Life (complete, English-tagged), Still Standing (complete), NewsRadio (complete), Reba (mostly complete, English default), Coach (complete if you take all nine season items), and Mad About You only in the soft 240p English-default set.

Say which of those you want, and they can go into the next import pass. Nothing was added in this round.
