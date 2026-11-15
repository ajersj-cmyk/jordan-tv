#!/usr/bin/env bash
# Reproducible build of Jordan TV 2 from Jordan's original APK.
# Usage: build.sh <original.apk> <out.apk> [versionCode] [versionName]
set -euo pipefail
source /home/box/android-dev/env.sh
HERE=$(cd "$(dirname "$0")" && pwd)
ORIG=$(realpath "$1"); OUT=$(realpath -m "$2"); VC=${3:-3}; VN=${4:-1.2-nolimit}
W=$(mktemp -d); cd "$W"
java -jar "$HERE/apktool.jar" d -q -o dec "$ORIG"
cp "$HERE/guide.orig.html" .
python3 "$HERE/patch_guide.py"
python3 "$HERE/patch_smali.py"
python3 "$HERE/patch_storage.py"
python3 "$HERE/patch_meta.py" "$VC" "$VN"
# compile the JordanStore bridge class into smali
mkdir -p jcls jdex
javac -source 8 -target 8 -nowarn -bootclasspath "$ANDROID_HOME/platforms/android-37.0/android.jar" -d jcls $(find "$HERE/src" -name '*.java')
d8 --min-api 24 --release --lib "$ANDROID_HOME/platforms/android-37.0/android.jar" --output jdex $(find jcls -name '*.class')
[ -f "$HERE/tools/Dis.class" ] || javac -cp "$HERE/apktool.jar" -d "$HERE/tools" "$HERE/tools/Dis.java"
java -cp "$HERE/apktool.jar:$HERE/tools" Dis jdex/classes.dex jsmali
cp -r jsmali/tv dec/smali_classes2/
java -jar "$HERE/apktool.jar" b -q -o unsigned.apk dec
zipalign -f -p 4 unsigned.apk aligned.apk
set -a; source /home/box/android-dev/keys/signing.env; set +a
apksigner sign --ks "$TVAPP_KEYSTORE" --ks-pass env:TVAPP_KEYSTORE_PASSWORD --ks-key-alias "$TVAPP_KEY_ALIAS" --key-pass env:TVAPP_KEY_PASSWORD --out "$OUT" aligned.apk
cp dec/assets/guide.html "$(dirname "$OUT")/guide.built.html"
echo "built $OUT (workdir $W)"
