"""Find repeated ciphertext sequences, starting with two-letter sequences."""

import argparse
from collections import defaultdict
from pathlib import Path


def find_repeats(text, min_length=2, min_occurrences=3):
    """Yield (length, matches), counting overlapping, zero-based occurrences."""
    if min_length < 1 or min_occurrences < 2:
        raise ValueError("Use a positive length and at least two occurrences.")

    for length in range(min_length, len(text) + 1):
        positions = defaultdict(list)
        for start in range(len(text) - length + 1):
            segment = text[start : start + length]
            positions[segment].append(start)

        matches = {
            segment: indices
            for segment, indices in positions.items()
            if len(indices) >= min_occurrences
        }
        if not matches:
            # A longer sequence cannot occur more often than its prefix.
            break
        yield length, matches


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "file", nargs="?", type=Path,
        default=Path(__file__).with_name("vigenere-ct.txt"),
        help="Ciphertext file (default: vigenere-ct.txt beside this script).",
    )
    parser.add_argument("--min-length", type=int, default=2)
    parser.add_argument("--min-occurrences", type=int, default=3)
    args = parser.parse_args()
    if args.min_length < 1 or args.min_occurrences < 2:
        parser.error("Use a positive length and at least two occurrences.")

    try:
        # Assignment line breaks and other whitespace are not ciphertext.
        text = "".join(args.file.read_text(encoding="utf-8").split())
    except OSError as error:
        parser.error(str(error))
    if not text or any(letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for letter in text):
        parser.error("Ciphertext must contain uppercase A-Z letters and whitespace only.")

    print(f"Ciphertext length: {len(text)} letters")
    print(f"Minimum occurrences: {args.min_occurrences}")
    print("Positions are zero-based; overlapping occurrences count.")
    found = False
    for length, matches in find_repeats(text, args.min_length, args.min_occurrences):
        found = True
        print(f"\nLength {length}:")
        for segment, indices in matches.items():
            print(f"  {segment}: {len(indices)} occurrences at {indices}")
    if not found:
        print("No sequences meet these criteria.")


if __name__ == "__main__":
    main()
