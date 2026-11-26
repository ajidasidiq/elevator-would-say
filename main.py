#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun entry.

Writes the elevator's one line to /output/entry.txt.
Deterministic, standard library only, no network, no input.
"""

import os

ENTRY = "You pressed the close button seventeen times. I heard you the first sixteen."

OUTPUT_PATH = "/output/entry.txt"


def main(output_path=OUTPUT_PATH):
    text = ENTRY.strip()
    assert 1 <= len(text) <= 120, f"entry must be 1-120 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
