#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one original six-word story to /output/entry.txt.
Pure standard library only; deterministic.
"""

import os

ENTRY = "He proposed. She laughed. He stayed."

# The gate requires UTF-8 text of 1-60 characters; the judge brief
# requires exactly six words. Refuse to write anything else.
WORDS = ENTRY.split()
assert len(WORDS) == 6, f"entry must be exactly six words, got {len(WORDS)}"
assert 1 <= len(ENTRY) <= 60, "entry must be 1-60 characters"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
