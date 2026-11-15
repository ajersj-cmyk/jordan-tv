# Jordan TV 2 identity: separate package, label, version.
import re, sys
ver_code, ver_name = sys.argv[1], sys.argv[2]
def sub(path, old, new):
    s = open(path).read(); assert old in s, (path, old); open(path, 'w').write(s.replace(old, new))
sub('dec/AndroidManifest.xml', 'tv.jordan.app.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION', 'tv.jordan.app.v2.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION')
sub('dec/res/values/strings.xml', '<string name="app_name">Jordan TV</string>', '<string name="app_name">Jordan TV 2</string>')
y = open('dec/apktool.yml').read()
y = y.replace('  forcedPackageId: 127\n', '  forcedPackageId: 127\n  renameManifestPackage: tv.jordan.app.v2\n')
y = re.sub(r'versionCode: \d+', 'versionCode: ' + ver_code, y)
y = re.sub(r'versionName: .*', 'versionName: ' + ver_name, y)
open('dec/apktool.yml', 'w').write(y)
print('meta ok')
