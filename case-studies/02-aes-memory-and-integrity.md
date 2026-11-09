# AES memory exposure and ciphertext integrity

**Source:** Programming Assignment 1. **Status:** documented Xubuntu experiment and Java decryption program.

I tested two supplied image-viewing programs to examine how key material could remain in process memory and whether ciphertext modification would be detected.

## Observed sequence

1. Ran the first course program and captured a process core dump. The dump tool warned about one unreadable memory region but saved the file.
2. Scanned the saved dump with `aeskeyfind`. The scan completed and reported a 128-bit AES candidate.
3. Implemented the decryption steps in Java using the standard cryptography library. The file format put a 16-byte IV before the ciphertext, and the program used `AES/CTR/NoPadding`.
4. Opened the recovered file as a JPEG. The report records image dimensions of **1908 × 1146**, providing a separate check beyond simply writing an output file.
5. Repeated the dump and scan against the second course program. That scan completed without reporting a candidate key.
6. Changed one ciphertext byte in the test data without changing the file size. The first program displayed corrupted image bands and did not report an integrity failure.

## Interpretation

The first result connected a candidate from memory to successful decryption. The second result only establishes that this scan did not find a candidate. Clearing the key or expanded schedule is a plausible explanation, but the scan alone does not identify the changed source line or prove that key recovery is impossible.

The ciphertext edit showed the limit of the supplied unauthenticated CTR construction: modifying encrypted bytes changed the recovered data without a detected integrity failure. It was not a cryptanalytic break of AES itself.

## Public program

The [Java source](../code/aes-ctr/Decrypt.java) keeps the original decryption structure but accepts explicit arguments instead of embedding the recovered course key and input path. Argument and length validation were added for the public version. The original course key, data file, and memory dumps are omitted.

The report discloses that AI converted my pseudocode into Java. Historical image validation and current synthetic program checks are documented separately.

**Skills demonstrated:** memory-artifact analysis, key lifecycle reasoning, Java cryptography APIs, binary file handling, and integrity verification.
