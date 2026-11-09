# Applied Cryptography Labs

I put this collection together from my Applied Cryptography coursework at Simon Fraser University. It covers how encryption can fail through weak constructions, exposed key material, missing integrity protection, and observable padding errors.

## Work included

| Assignment | Work | Status |
| --- | --- | --- |
| Written Assignment 1 | [Security goals and classical cryptanalysis](case-studies/01-security-goals-and-classical-cryptanalysis.md) | Completed written work, repeat-analysis script, and recorded decryption evidence. |
| Programming Assignment 1 | [AES memory exposure and ciphertext integrity](case-studies/02-aes-memory-and-integrity.md) | Key recovery, Java decryption, image validation, and a controlled ciphertext edit documented in the report. |
| Programming Assignment 2 | [CBC padding-oracle decryption and construction](case-studies/03-padding-oracles.md) | Three programs with recorded Xubuntu runs, including a separate oracle readback for constructed ciphertext. |
| Programming Assignment 3 | Weak RSA modulus factorization | Scaffold only in the reviewed source. No completed factorization or verified result is claimed. |

## Code

- [Repeated-sequence analysis](code/classical/README.md): Python utility and a synthetic example.
- [AES-CTR decryption](code/aes-ctr/README.md): Java program adapted to take explicit input and output arguments.
- [Padding-oracle work](code/padding-oracles/README.md): three coursework scripts, with the student-specific final block removed from the public version.

## Scope and evidence

The reports identify the course as **CMPT 789 G100, Applied Cryptography, Fall 2026**, despite the different course number in the original local folder name. The public collection uses topic names to avoid that ambiguity.

Historical VM observations are distinguished from the checks performed when preparing this portfolio. The original course binaries, ciphertext files, memory dumps, lecture slides, assignment handouts, and submission PDFs are not distributed here. The writeups are condensed case studies, and code changes made for publication are documented.

The PA1 report explicitly records AI conversion of my pseudocode into Java, plus formatting and grammar assistance. Other source work also used AI assistance. This portfolio was organized and edited with AI assistance. See [attribution and coverage](docs/coverage-and-attribution.md) and [validation](docs/validation.md).

Related: [cybersecurity lab portfolio](https://github.com/RDMRock/cybersecurity-lab-portfolio) and [GitHub profile](https://github.com/RDMRock).
