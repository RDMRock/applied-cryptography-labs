# AES-CTR decryption example

The PA1 implementation uses Java's standard cryptography library. The public adaptation accepts a key and file paths explicitly and validates the key and IV lengths. It does not embed the original recovered course key.

```sh
javac Decrypt.java
java Decrypt <32-hex-test-key> <iv-prefixed-input-file> <output-file>
```

Replace the angle-bracket placeholders with test values. Use a disposable output path because the program writes that file. The first 16 input bytes are the IV, followed by the AES-CTR ciphertext. The key is exactly 16 bytes, expressed as 32 hexadecimal digits. The program produces no normal success output.

This deliberately reproduces the assignment's unauthenticated file format. It has no authentication tag and should not be used as a design for protecting real files. Use synthetic lab keys for this command-line example, where arguments can appear in shell history and process information.

The source report records successful decryption on Xubuntu and opening a 1908 × 1146 JPEG. See [current validation](../../docs/validation.md) for the public adaptation's checks. AI conversion of the original pseudocode into Java was disclosed in the assignment.
