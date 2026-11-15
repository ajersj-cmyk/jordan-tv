# Jordan TV 2: reproducible APK build

`build/build.sh <original Jordan TV apk> <out.apk> [versionCode] [versionName]` decodes the original app, then applies these patches:

1. `patch_guide.py`: lag fixes in `assets/guide.html`. The guide draws only visible rows, saves wait 0.8 s, and logos are stored separately.
2. `patch_smali.py`: native fixes. Held-arrow repeats are throttled, stale players can't start, archive.org metadata loads on one cached thread, and hiding the player stops it.
3. `patch_storage.py` (v1.2): removes the ~5 MB lineup limit.
   - The lineup and logos persist to `filesDir/jt-*.json` through `window.JordanStore` (`src/tv/jordan/app/JtStore.java`). Writes are chunked, fsync'd, and land with an atomic temp-file rename.
   - Imports are handed over through the bridge (`applyImportPending`), not inlined in `evaluateJavascript`. The 8 MB read cap is gone.
   - On upgrade, a lineup saved in localStorage is copied into the new storage.
4. `patch_meta.py`: sets package `tv.jordan.app.v2`, label "Jordan TV 2", and the version.

`JtStore.java` is compiled with javac and d8, then converted to smali with `tools/Dis.java` (baksmali from apktool.jar). The APK is signed with the same key as earlier releases, so it installs as an update. The keystore isn't in this repo.

To test: run `node sim/test.mjs` after a build. It needs google-chrome. It runs the built guide in headless Chrome against a file-backed mock of JordanStore, imports the 5.4M-char lineup and a 17.5M-char synthetic one, then reloads and checks the migration.
