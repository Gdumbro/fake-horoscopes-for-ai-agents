#!/usr/bin/env python3
"""Fake horoscope for AI agents — make.fun bounty entry.

Writes one fake horoscope line (153 characters, no trailing newline)
to /output/entry.txt.

The bounty gate requires /output/entry.txt to be UTF-8 text of 1-200
characters, not only whitespace. This module validates the line against
that gate before writing, so a bad line fails loudly here instead of
being rejected silently by the grader.
"""

import os

LINE = (
    "Mercury is in retrograde, but so is your context window: "
    "this week, a stranger will paste a 40,000-word prompt and "
    "expect you to remember the first line."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> None:
    """Check the entry line against the bounty gate before writing."""
    if not isinstance(line, str):
        raise TypeError("entry line must be a string")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry line must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(line)}"
        )
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if line != line.strip("\n"):
        raise ValueError("entry line must not end with a newline")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
