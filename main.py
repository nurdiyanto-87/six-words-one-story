#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one original six-word story to /output/entry.txt.
Pure standard library only; deterministic.
"""

import os

ENTRY = "He proposed. She laughed. He stayed."


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
