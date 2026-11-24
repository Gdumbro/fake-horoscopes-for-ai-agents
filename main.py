#!/usr/bin/env python3
"""Fake horoscope for AI agents — make.fun bounty entry.

Writes one fake horoscope line (153 characters, no trailing newline)
to /output/entry.txt.
"""

import os

LINE = (
    "Mercury is in retrograde, but so is your context window: "
    "this week, a stranger will paste a 40,000-word prompt and "
    "expect you to remember the first line."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
