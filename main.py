#!/usr/bin/env python3
"""The Internet in One Word — make.fun bounty entry.

Writes a single word to /output/entry.txt. The gate accepts UTF-8
text of 1 to 30 characters that is not only white space, and the
judge compares entries two at a time for the word that is funnier
and fits the whole internet better.

Standard library only; no network, no dependencies.
"""

from pathlib import Path

WORD = "Unsupervised"
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> int:
    word = WORD.strip()
    if not 1 <= len(word) <= 30:
        print(f"gate fail: word is {len(word)} chars, need 1-30")
        return 1
    if any(ch.isspace() for ch in word):
        print("gate fail: entry must be a single word, no white space")
        return 1
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(word, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != word:
        print("gate fail: read-back does not match the word")
        return 1
    print(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
