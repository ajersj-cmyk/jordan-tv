package tv.jordan.app;

import android.content.Context;
import android.webkit.JavascriptInterface;
import java.io.BufferedWriter;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.OutputStreamWriter;

/**
 * File-backed storage for the guide (window.JordanStore). Replaces WebView
 * localStorage, which caps at ~5M chars. Strings move in chunks so no single
 * bridge call carries a huge payload. Files live in the app's private files dir.
 */
public final class JtStore {
    /** Text of the file the user just picked for import (set by MainActivity). */
    public static volatile String pendingImport;

    private static final int MAX_CHUNK = 1 << 20;
    private final File dir;
    private String held;
    private FileOutputStream wOut;
    private BufferedWriter writer;
    private String wName;

    public JtStore(Context context) {
        dir = context.getFilesDir();
    }

    private static boolean okName(String name) {
        return name != null && name.matches("[a-z0-9-]{1,40}");
    }

    private File file(String name) {
        return new File(dir, "jt-" + name + ".json");
    }

    @JavascriptInterface
    public boolean available() {
        return true;
    }

    /** Opens a value for chunked reading; returns its length in chars, or -1 when missing. */
    @JavascriptInterface
    public synchronized int open(String name) {
        held = null;
        if ("import".equals(name)) {
            held = pendingImport;
            pendingImport = null;
        } else if (okName(name)) {
            held = readFile(file(name));
        }
        return held == null ? -1 : held.length();
    }

    /** Returns up to maxLen chars from start; never splits a surrogate pair. */
    @JavascriptInterface
    public synchronized String chunk(int start, int maxLen) {
        if (held == null || start < 0 || start >= held.length()) return "";
        int len = Math.max(1, Math.min(maxLen <= 0 ? MAX_CHUNK : maxLen, MAX_CHUNK));
        int end = Math.min(held.length(), start + len);
        if (end < held.length() && end - start > 1 && Character.isHighSurrogate(held.charAt(end - 1))) end--;
        return held.substring(start, end);
    }

    @JavascriptInterface
    public synchronized void close() {
        held = null;
    }

    /** Starts writing a value to a temp file. */
    @JavascriptInterface
    public synchronized boolean begin(String name) {
        abortWrite();
        if (!okName(name)) return false;
        try {
            File tmp = new File(dir, "jt-" + name + ".json.tmp");
            wOut = new FileOutputStream(tmp);
            writer = new BufferedWriter(new OutputStreamWriter(wOut, "UTF-8"), 1 << 16);
            wName = name;
            return true;
        } catch (Exception e) {
            abortWrite();
            return false;
        }
    }

    @JavascriptInterface
    public synchronized boolean append(String part) {
        if (writer == null) return false;
        try {
            if (part != null) writer.write(part);
            return true;
        } catch (Exception e) {
            abortWrite();
            return false;
        }
    }

    /** Flushes, syncs and atomically renames the temp file into place. */
    @JavascriptInterface
    public synchronized boolean commit() {
        if (writer == null || wName == null) return false;
        String name = wName;
        File tmp = new File(dir, "jt-" + name + ".json.tmp");
        try {
            writer.flush();
            wOut.getFD().sync();
            writer.close();
            writer = null;
            wOut = null;
            wName = null;
            File dst = file(name);
            if (tmp.renameTo(dst)) return true;
            dst.delete();
            return tmp.renameTo(dst);
        } catch (Exception e) {
            abortWrite();
            return false;
        }
    }

    @JavascriptInterface
    public synchronized boolean remove(String name) {
        return okName(name) && file(name).delete();
    }

    private void abortWrite() {
        try {
            if (writer != null) writer.close();
        } catch (Exception e) {
            // ignore
        }
        if (wName != null) new File(dir, "jt-" + wName + ".json.tmp").delete();
        writer = null;
        wOut = null;
        wName = null;
    }

    private static String readFile(File f) {
        if (!f.isFile()) return null;
        FileInputStream in = null;
        try {
            in = new FileInputStream(f);
            long size = f.length();
            ByteArrayOutputStream buf = new ByteArrayOutputStream((int) Math.max(32, Math.min(size, Integer.MAX_VALUE - 8)));
            byte[] chunk = new byte[1 << 16];
            int n;
            while ((n = in.read(chunk)) >= 0) buf.write(chunk, 0, n);
            return buf.toString("UTF-8");
        } catch (Exception e) {
            return null;
        } finally {
            try {
                if (in != null) in.close();
            } catch (Exception e) {
                // ignore
            }
        }
    }
}
