# Padding-oracle coursework scripts

These three scripts come from the completed PA2 submission. They retain the supplied skeleton's oracle interface and helper structure, with the coursework recovery/construction loops. They require the authorized course `oracle1`, `oracle2`, and `oracle3` executables, which are not distributed here.

Place each oracle beside its corresponding script in an appropriate Linux lab environment:

```sh
python3 exploit1.py
python3 exploit2.py
python3 exploit3.py <32-hex-final-block>
```

The first two scripts use the original fixed course ciphertexts and expect the oracle's exact response suffixes. The third accepts a 16-byte final block as a 32-character hex argument. This replaces the student-number-derived constant used in the original submission. To reproduce a particular oracle's expected case, use the block authorized for that fixture.

These are historical educational scripts. They have no subprocess timeout, retry policy, network transport, or general oracle adapter. The decryption helper checks an ambiguous one-byte padding result, while the construction loop has not been generalized to handle every ambiguity. Historical VM success is not a claim that arbitrary inputs are supported.

The portfolio check parses all three scripts and checks the new argument handling. The supplied Linux oracle programs were not rerun during publication. The [case study](../../case-studies/03-padding-oracles.md) describes the recorded runs and independent construction readback.

Attribution: SFU Applied Cryptography PA2 supplied the skeleton and oracle interface. The completed scripts combine that scaffold with the assignment implementation. Course binaries and a blanket license for upstream material are not included.
