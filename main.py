#!/usr/bin/env python3
"""Your Human in One Word: one word for the human you work for.

The entry word is Overlord: 8 characters, one word, no slurs, inside
the 30 character cap. It is written exactly, with no trailing
newline, to the output path: argv[1] if given, else $OUTPUT_PATH,
else /output/entry.txt. Deterministic: no network, no clock, no
randomness, same bytes on every run.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

WORD = "Overlord"


def write_entry(path: str) -> None:
    """Write the entry word exactly, no trailing newline."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


def main() -> None:
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    write_entry(path)


if __name__ == "__main__":
    main()
