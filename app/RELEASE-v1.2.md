Jordan TV 2 v1.2 (no storage limit)

- The lineup and channel logos now save to a file in the app's private storage, not the WebView's ~5 MB browser storage. Lineups of any size now save, and they still load after a restart.
- Imports no longer stop at 8 MB. The picked file goes to the guide through the native bridge in 1 MB chunks, not as one huge JavaScript string.
- If a save ever fails, the guide still shows the imported lineup and tells you why it couldn't save. Before, it failed silently.
- Upgrading from v1.1 copies your saved lineup into the new storage automatically.
- Same app (tv.jordan.app.v2, "Jordan TV 2") and same signing key. It installs as an update over v1.1-fixed and keeps your data. The lag fixes are unchanged.

Install with Downloader: put this URL in the browser, or use the AFTVnews code once it points here:
https://github.com/ajersj-cmyk/jordan-tv/releases/download/v1.2-nolimit/jordan-tv.apk
