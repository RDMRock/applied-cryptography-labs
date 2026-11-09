# Security goals and classical cryptanalysis

**Source:** Written Assignment 1. **Status:** completed written report and supporting Python utility.

I examined the assumptions behind several security claims and used small examples to show where they break.

| Problem | Work | Main result |
| --- | --- | --- |
| 1 | Confidentiality, integrity, availability, non-repudiation, freshness, secure defaults, and failure behavior. | Identified a fail-open authorization path where an exception left the return value true. |
| 2 | Vigenère cryptanalysis using repeated segments and spacing. | Repeat distances of 60, 52, and 64 gave a GCD of four. The report records the recovered four-character key and plaintext. |
| 3 | Correctness and perfect secrecy of small tabular ciphers. | Distinguished reversibility for each key from equal ciphertext distributions under uniformly chosen keys. |
| 4 | A many-time-pad exercise. | The report contains screenshot-based work using the supplied exercise. No standalone solver or additional success metric is claimed here. |
| 5 | Semantic security and chosen-plaintext reasoning. | Explained why different-length challenge messages leak the answer through ciphertext length, and analyzed a predictable codeword scenario. |
| 6 | A flawed recurrence-based stream cipher. | Used known plaintext to recover stream values and showed that only small residue classes affected the output. The report bounded the candidate set by 82, without claiming that all 82 were distinct. |

## Repeat-analysis utility

The [Python script](../code/classical/find_repeats.py) lists repeated substrings, their lengths, and all zero-based positions. It counts overlapping occurrences, validates input, and stops searching longer substrings when the current length has no qualifying repeats.

It supports the repeated-pattern stage of Kasiski-style analysis. It does not independently identify a Vigenère key or prove the true period from a single common divisor. The public sample is synthetic, so the original assignment ciphertext is not needed to try the utility.

**Skills demonstrated:** precise security definitions, adversarial reasoning, modular arithmetic, small-state analysis, and Python data processing.
