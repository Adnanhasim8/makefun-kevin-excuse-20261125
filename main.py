#!/usr/bin/env python3
"""Write the kevin-excuse entry: one line, under 200 characters, to /output/entry.txt.

Standard library only, no network at run time.
"""

import os

ENTRY = "Sorry \u2014 I hallucinated the fix, shipped the hallucination, and now the hallucination has root access."


def main():
    # Gate assertions: exactly one line, 1-200 characters, non-empty, no trailing newline.
    assert ENTRY, "entry must be non-empty"
    assert "\n" not in ENTRY, "entry must be exactly one line"
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 characters, got {len(ENTRY)}"
    assert ENTRY.strip() == ENTRY and ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
