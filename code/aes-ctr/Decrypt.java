import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class Decrypt {
    public static void main(String[] args) throws Exception {
        // Portfolio adaptation: supply a synthetic or authorized test key explicitly.
        if (args.length != 3) {
            throw new IllegalArgumentException("Usage: java Decrypt <32-hex-key> <input> <output>");
        }
        String keyHex = args[0];
        if (!keyHex.matches("[0-9a-fA-F]{32}")) {
            throw new IllegalArgumentException("Expected a 128-bit key as 32 hexadecimal digits");
        }
        byte[] keyBytes = new byte[keyHex.length() / 2];
        for (int i = 0; i < keyBytes.length; i++) {
            keyBytes[i] = (byte) Integer.parseInt(
                keyHex.substring(i * 2, i * 2 + 2), 16);
        }

        // Read the file and separate the IV from the ciphertext.
        byte[] fileBytes = Files.readAllBytes(Paths.get(args[1]));
        if (fileBytes.length < 16) {
            throw new IllegalArgumentException("Input must start with a 16-byte IV");
        }
        byte[] iv = Arrays.copyOfRange(fileBytes, 0, 16);
        byte[] ciphertext = Arrays.copyOfRange(fileBytes, 16, fileBytes.length);

        // Configure AES-CTR with the recovered key and the file's IV.
        Cipher cipher = Cipher.getInstance("AES/CTR/NoPadding");
        SecretKeySpec key = new SecretKeySpec(keyBytes, "AES");
        cipher.init(Cipher.DECRYPT_MODE, key, new IvParameterSpec(iv));

        // Decrypt the image and write its original bytes to the output file.
        byte[] plaintext = cipher.doFinal(ciphertext);
        Files.write(Paths.get(args[2]), plaintext);
    }
}
