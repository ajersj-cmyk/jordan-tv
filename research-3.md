# Jordan TV: Research Round 3 (whole movies, newer shows, newer preschool)

Checked 2026-11-13 21:13 ET. Research only: none of this has been added to the JSON.

## Method
- **Search:** 162 IA advancedsearch queries (r3/search3.json), auto-screened in r3/eval3.json.
- **Filtered out:**
  - Foreign dubs (including Benelux/Hungarian/Filipino releases), openings/closings, trailers and bootleg cams
  - Workprints, game longplays and reaction videos
  - Items with a non-English `language` field
  - Access-restricted items
- **Lineup check:** each title was checked against `jordan-tv-import-full.json` titles.
  - Excluded because they're already in the lineup: Pokémon: The First Movie (Indigo League station), The Sandlot (VHS Kids Movies), The SpongeBob Movie (VHS Kids Movies), The Polar Express (Christmas Movies), Wild Kratts, WordGirl and Curious George (PBS), Digimon Adventure (Toonami).
  - Shows that only appear as single holiday episodes (Gravity Falls, Phineas, Regular Show, Amphibia, etc.) count as new.
- **ffprobe:** run on the main feature (movies) or a mid-list episode (shows). Every sample URL returned HTTP 206. Audio is listed as tagged; `und`/untagged means the rip didn't tag a language. These are English releases by title and metadata, but untagged tracks weren't individually listened to.

## Ranked picks

| # | Group | Title | Files / known total | Typical res · GB | ffprobe sample | Runtime (sample) | IA item | Fits channel |
|---|---|---|---|---|---|---|---|---|
| 1 | Newer cartoons | Gravity Falls (complete, Blu-ray) | 50 / 40 + shorts | 1080p · 27.4 | hevc 1920x1080 / aac(eng), aac(eng) | 22m | https://archive.org/details/one-crazy-summer_202408 | Disney Channel 2003-2008 era / new 'Disney XD 2010s' |
| 2 | Newer cartoons | DuckTales (2017) | 69 / 69 | 720p · 18.6 | h264 1280x720 / aac(eng) | 22m | https://archive.org/details/ducktales-2017-complete-tv-series | Toon Disney |
| 3 | Newer cartoons | Phineas and Ferb (+2 movies) | 176 / 136 eps (222 segs) + 2 movies | 720p · 19.4 | h264 1280x720 / aac(eng) | 10m | https://archive.org/details/ferb-i-know-what-were-gonna-do-today. | Disney Channel 2003-2008 era |
| 4 | Newer cartoons | Regular Show | 263 / 261 | 1080p · 31.1 | hevc 1920x1080 / aac(eng) | 11m | https://archive.org/details/regularshow_cn | Cartoon Network 90s / new 'CN 2010s' |
| 5 | Newer cartoons | She-Ra and the Princesses of Power | 52 / 52 | 1080p · 24.4 | h264 1920x1080 / aac(eng) | 24m | https://archive.org/details/she-ra-and-the-princesses-of-power | new 'Netflix/CN 2010s' |
| 6 | Newer cartoons | Voltron: Legendary Defender | 76 / 78 | 1080p · 31.8 | h264 1920x1080 / ac3(eng) | 23m | https://archive.org/details/voltron-legendary-defender | X-Men/TMNT/SuperHeroShows |
| 7 | Newer cartoons | Over the Garden Wall | 12 / 10 | 1080p · 2.9 | hevc 1920x1080 / aac(eng), aac(eng), aac(eng) | 11m | https://archive.org/details/over-the-garden-wall-1080p-and-extras | CN 2010s / Holiday (fall) |
| 8 | Newer cartoons | Infinity Train | 52 / 40 | 1080p · 7.8 | hevc 1920x1080 / ac3(eng) | 11m | https://archive.org/details/infinity_train_202507 | CN 2010s |
| 9 | Newer cartoons | Star vs. the Forces of Evil | 121 / 77 (~120 segs) | 540p · 4.7 | hevc 960x540 / aac(eng) | 11m | https://archive.org/details/star.vs-the-forces-of-evil-full-series | Disney XD 2010s |
| 10 | Newer cartoons | LEGO Ninjago: Masters of Spinjitzu | 282 / ~210 | 1080p · 132.0 | h264 1920x1080 / aac(eng) | 22m | https://archive.org/details/Ninjago-Masters-of-Spinjitsu-full-show | CN 2010s |
| 11 | Newer cartoons | Amphibia (partial) | 40 / 58 | 480p · 6.7 | h264 852x480 / aac(eng) | 22m | https://archive.org/details/amphibia_20260605 | Disney XD 2010s |
| 12 | Newer cartoons | We Bare Bears (partial) | 52 / 140 | 720p · 17.1 | h264 1920x1080 / aac(eng) | 11m | https://archive.org/details/webarebearsfull | CN 2010s |
| 13 | Newer cartoons | Wander Over Yonder | 46 / 43 (~80 segs) | 720p · 4.2 | h264 1280x720 / aac(und) | 11m | https://archive.org/details/too-loud-and-wander-over-yonder | Disney XD 2010s |
| 14 | Newer cartoons | Yo-kai Watch (English, eps 1-59) | 57 / ~78 dubbed | 1080p · 18.9 | h264 1280x720 / aac(und) | 22m | https://archive.org/details/YoKai_English_Ep1-59 | Toonami Anime |
| 15 | Newer preschool | Sofia the First S1-4 | 116 / 109 | 1080p · 37.3 | hevc 1920x1080 / aac(eng) | 22m | https://archive.org/details/sofia-the-first-complete-series-s01-s04-1080p-phun-psyz | Preschool |
| 16 | Newer preschool | Octonauts | 116 / ~130 | 468p · 7.6 | h264 1024x576 / aac(und) | 11m | https://archive.org/details/octonauts-2010-episodes | Preschool |
| 17 | Newer preschool | Peg + Cat | 66 / 63 | 720p · 19.4 | h264 1280x720 / aac(eng) | 25m | https://archive.org/details/peg-cat-full-series_202606 | Preschool / PBS |
| 18 | Newer preschool | Odd Squad (TVOKids) | 122 / ~120+ | 1080p · 69.6 | h264 1920x1080 / aac(eng) | 26m | https://archive.org/details/Odd_Squad_TVOKids | PBS KIDS 2000's |
| 19 | Newer preschool | Hey Duggee | 293 / ~260 | 720p · 58.3 | h264 1280x720 / aac(eng) | 7m | https://archive.org/details/hey-duggee-s-05-e-16-the-rollercoaster-badge | Preschool |
| 20 | Newer preschool | Ben & Holly's Little Kingdom | 78 / 104 | 480p · 4.9 | h264 640x360 / aac(und) | 11m | https://archive.org/details/ben-and-hollys-little-kingdom-epds | Preschool |
| 21 | Newer preschool | PJ Masks | 37 / ~150 | 1080p · 18.2 | h264 1920x1080 / aac(und) | 23m | https://archive.org/details/pjmheroesdownload | Preschool |
| 22 | Newer preschool | Peppa Pig S1 | 52 / 52 | 400p · 2.8 | h264 720x576 / aac(und) | 5m | https://archive.org/details/peppa-pig-s01_ | Preschool |
| 23 | Newer preschool | Peppa Pig S2 | 53 / 53 | 400p · 2.9 | h264 640x352 / aac(und) | 5m | https://archive.org/details/peppa-pig-02_ | Preschool |
| 24 | Newer preschool | Dinosaur Train S1 | 49 / 40 (S1) | 1080p · 56.2 | h264 1920x1080 / aac(eng) | 28m | https://archive.org/details/dinosaur-train-season-1-s-01-e-01-elmer-elasmosaurus | Preschool / PBS |
| 25 | Newer preschool | Tickety Toc | 73 / 72 | 720p · 8.6 | h264 1280x720 / aac(eng) | 11m | https://archive.org/details/ticketytocAllEpisodes | Preschool |
| 26 | Newer preschool | Nature Cat | 99 / ~100 | 1080p · 134.0 | h264 1920x1080 / eac3(eng) | 24m | https://archive.org/details/NCTVSeries20152024 | PBS KIDS 2000's |
| 27 | Newer preschool | Shaun the Sheep S2 | 40 / 40 | 720p · 6.9 | h264 1280x720 / ac3(untagged) | 7m | https://archive.org/details/shaun-the-sheep-season-2 | Preschool |
| 28 | Movies: anime | Pokémon the Movie 2000 (+ Pikachu short) | 1 / 1 | 480p · 0.5 | h264 640x480 / aac(und) | 80m | https://archive.org/details/pokemon-the-movie-2000-dark-dream | Pokémon / VHS Kids Movies |
| 29 | Movies: anime | Pokémon 3: Spell of the Unown | 1 / 1 | 688p · 0.9 | h264 1280x688 / aac(eng) | 73m | https://archive.org/details/PokemonS01M03Pokemon3TheMovieSpellOfTheUnown | Pokémon / VHS Kids Movies |
| 30 | Movies: anime | Pokémon 4Ever | 1 / 1 | 360p · 0.3 | h264 640x360 / aac(und) | 76m | https://archive.org/details/PokemonS01M04Pokemon4EverCelebiVoiceOfTheForest2002 | Pokémon / VHS Kids Movies |
| 31 | Movies: anime | Pokémon Heroes (theatrical) | 1 / 1 | 480p · 1.7 | mpeg2video 720x480 / ac3(eng) | 71m | https://archive.org/details/b-1-t-00_20240330 | Pokémon / VHS Kids Movies |
| 32 | Movies: anime | Digimon: The Movie (2000) | 1 / 1 | 540p · 1.2 | h264 960x540 / aac(und) | 84m | https://archive.org/details/digimon-the-movie-2000_202501 | Toonami / VHS Kids Movies |
| 33 | Movies: family | Matilda (1996) | 1 / 1 | 808p · 1.7 | h264 1920x808 / aac(und) | 98m | https://archive.org/details/matilda-1996_202405 | VHS Kids Movies |
| 34 | Movies: family | Harriet the Spy (1996) | 1 / 1 | 480p · 0.4 | h264 720x480 / mp3(untagged) | 101m | https://archive.org/details/harriet-the-spy-1996 | VHS Kids Movies |
| 35 | Movies: family | Jumanji (1995) | 1 / 1 | 720p · 0.9 | h264 1328x720 / aac(und) | 104m | https://archive.org/details/jumanji-1995_202510 | VHS Kids Movies |
| 36 | Movies: family | Richie Rich (1994) | 1 / 1 | 720p · 1.3 | h264 1276x720 / aac(und) | 94m | https://archive.org/details/richie-rich_202311 | VHS Kids Movies |
| 37 | Movies: family | Rookie of the Year (1993) | 1 / 1 | 720p · 1.3 | h264 1310x720 / aac(und) | 103m | https://archive.org/details/rookie-of-the-year-1993 | VHS Kids Movies |
| 38 | Movies: family | Air Bud (1997) | 1 / 1 | 720p · 0.5 | h264 1280x720 / aac(eng) | 97m | https://archive.org/details/air-bud-official-movie | VHS Kids Movies |
| 39 | Movies: family | Flubber (1997) | 1 / 1 | 2064p · 8.4 | hevc 3824x2064 / eac3(eng) | 93m | https://archive.org/details/flubber-1997_202402 | VHS Kids Movies |
| 40 | Movies: family | Inspector Gadget (1999, extended) | 1 / 1 | 720p · 2.9 | h264 1280x720 / aac(eng) | 84m | https://archive.org/details/inspectorgadgetmovie-extended-720p | VHS Kids Movies |
| 41 | Movies: family | Mighty Morphin Power Rangers: The Movie | 1 / 1 | 682p · 1.0 | h264 1280x682 / aac(und) | 95m | https://archive.org/details/mighty-morphin-power-rangers-the-movie-1995_202308 | Fox Kids / VHS Kids Movies |
| 42 | Movies: family | Scooby-Doo (2002) | 2 / 1 | 1080p · 5.9 | h264 1920x1080 / aac(eng) | 102m | https://archive.org/details/scooby-doo-2002_202411 | VHS Kids Movies |
| 43 | Movies: family | Muppet Treasure Island (1996) | 1 / 1 | 1024p · 3.1 | h264 1920x1024 / aac(und) | 99m | https://archive.org/details/muppet-treasure-island-1996_202509 | VHS Kids Movies |
| 44 | Movies: family | Heavyweights (1995, VHS) | 1 / 1 | 1080p · 9.4 | h264 1920x1080 / aac(und) | 106m | https://archive.org/details/disneys-heavyweights-vhs | VHS Kids Movies |
| 45 | Movies: family | Blank Check (1994) | 1 / 1 | 480p · 0.8 | h264 850x480 / aac(und) | 93m | https://archive.org/details/blank-check | VHS Kids Movies |
| 46 | Movies: family | Homeward Bound (1993, VHS) | 1 / 1 | 480p · 4.7 | h264 640x480 / aac(eng) | 98m | https://archive.org/details/disneys-homeward-bound-the-incredible-journey-1996-vhs | VHS Kids Movies |
| 47 | Movies: family | Kazaam (1996) | 1 / 1 | 1036p · 1.1 | hevc 1920x1036 / aac(eng) | 93m | https://archive.org/details/kazaam-1996-1080p | VHS Kids Movies |
| 48 | Movies: animated | The Iron Giant (VHS) | 1 / 1 | 1080p · 2.9 | h264 1920x1080 / aac(und) | 85m | https://archive.org/details/iron-giant-vhs | VHS Kids Movies |
| 49 | Movies: animated | The Land Before Time | 1 / 1 | 1040p · 1.4 | h264 1920x1040 / aac(untagged) | 72m | https://archive.org/details/TheLandBeforeTime1_201703 | VHS Kids Movies |
| 50 | Movies: animated | Anastasia (1997) | 1 / 1 | 800p · 1.6 | h264 1920x800 / aac(und) | 94m | https://archive.org/details/anastasia.-1997.1080p.-blu-ray.x-264-yts.-am_202509 | VHS Kids Movies |
| 51 | Movies: animated | Quest for Camelot | 2 / 1 | 1080p · 2.9 | h264 1920x1080 / aac(und) | 85m | https://archive.org/details/quest-for-camelot-1998 | VHS Kids Movies |
| 52 | Movies: animated | The Pagemaster | 1 / 1 | 1040p · 1.6 | h264 1920x1040 / aac(und) | 75m | https://archive.org/details/the-pagemaster | VHS Kids Movies |
| 53 | Movies: animated | Rock-a-Doodle | 1 / 1 | 1024p · 1.3 | h264 1920x1024 / aac(und) | 74m | https://archive.org/details/rock-a-doodle.-1991.1080p.-blu-ray.x-264.-aac-yts.-mx | VHS Kids Movies |
| 54 | Movies: animated | The Swan Princess | 1 / 1 | 480p · 0.5 | h264 886x480 / aac(eng) | 89m | https://archive.org/details/the-swan-princess-1994_202406 | VHS Kids Movies |
| 55 | Movies: animated | Cats Don't Dance | 1 / 1 | 480p · 1.5 | h264 720x480 / aac(eng), ac3(eng) | 74m | https://archive.org/details/cats-dont-dance | VHS Kids Movies |
| 56 | Movies: Christmas | Jingle All the Way | 1 / 1 | 1040p · 1.4 | h264 1920x1040 / aac(eng) | 93m | https://archive.org/details/jingle-all-the-way_202601 | Christmas Movies |
| 57 | Movies: Christmas | The Santa Clause | 1 / 1 | 480p · 0.5 | h264 888x480 / aac(eng) | 97m | https://archive.org/details/the-santa-clause_480 | Christmas Movies |
| 58 | Movies: Christmas | The Muppet Christmas Carol (extended) | 1 / 1 | 720p · 1.1 | h264 1280x720 / aac(und) | 89m | https://archive.org/details/the-muppet-christmas-carol-1992-extended-cut-version | Christmas Movies |
| 59 | Movies: Christmas | Ernest Saves Christmas | 1 / 1 | 720p · 0.6 | h264 1280x720 / aac(und) | 91m | https://archive.org/details/Popcornarchive-ernestSavesChristmas1988 | Christmas Movies |

## Notes
- **Gravity Falls:** 10-bit HEVC (the onn box handles Main10). The 50 files are 40 episodes plus shorts/extras.
- **Phineas and Ferb:** 176 files = segments + both movies + 1 intro clip.
- **Star vs., Regular Show and Wander:** these are 11-minute segments, which is why the file counts run high.
- **Ninjago:** 132 GB; the 282 files include specials.
- **Partial sets:** Amphibia, We Bare Bears, PJ Masks, Octonauts, Ben & Holly and Yo-kai Watch are partial. Peppa S1/S2 are complete at 5 minutes per episode. Dinosaur Train S1 has 49 files for 40 episodes, which includes specials.
- **Scooby-Doo (2002) and Quest for Camelot:** each has 2 long files (alternate cuts). Pick one.
- **Pokémon Heroes:** MPEG-2 theatrical cut, which ExoPlayer plays. Pokémon 2000 includes the Pikachu short as a separate file.
- **VHS rips at 1080p** (Heavyweights, Iron Giant) are upscaled captures, so the files are big.

## Looked for, but no usable English full set on IA
- **Avatar: The Last Airbender:** DVD ISOs only.
- **Steven Universe and Digimon Tamers:** items have no directly playable video files.
- **Adventure Time:** only reaction videos.
- **Owl House, Paw Patrol, Bubble Guppies, Daniel Tiger, Puffin Rock, Bluey extras:** Bluey is already in the lineup. The others had only fragments.
- **Kipo:** single-episode items in other languages.
- **Movies:** Hocus Pocus, Home Alone, Good Burger, Snow Day, Big Fat Liar, Space Jam and Rugrats Movie were only available as VHS openings, broadcast tapes or bootlegs.
