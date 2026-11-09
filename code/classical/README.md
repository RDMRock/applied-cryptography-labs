# Repeated-sequence analysis

`find_repeats.py` is the existing Python utility from the written assignment. It uses only the standard library.

```sh
python3 find_repeats.py example.txt --min-length 3 --min-occurrences 3
```

The synthetic example includes `ABC` at positions 0, 6, and 12. The script reports all qualifying substrings, counting overlaps. Positions are zero-based. Input must contain uppercase A–Z letters and whitespace.

The original default filename remains `vigenere-ct.txt`. That course ciphertext is not included, so pass `example.txt` or your own file explicitly. This is a repeated-pattern utility, not a complete automatic cipher solver.
