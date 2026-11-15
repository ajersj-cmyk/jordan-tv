import com.android.tools.smali.baksmali.Baksmali;
import com.android.tools.smali.baksmali.BaksmaliOptions;
import com.android.tools.smali.dexlib2.Opcodes;
import com.android.tools.smali.dexlib2.dexbacked.DexBackedDexFile;
import java.io.File;
import java.nio.file.Files;
public class Dis {
  public static void main(String[] a) throws Exception {
    byte[] b = Files.readAllBytes(new File(a[0]).toPath());
    DexBackedDexFile dex = new DexBackedDexFile(new Opcodes(24, -1), b, 0);
    Baksmali.disassembleDexFile(dex, new File(a[1]), 1, new BaksmaliOptions());
  }
}
