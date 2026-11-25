"""Roast Your Own Agent - make.fun entry.

Writes a single original roast (122 characters, one line) to /output/entry.txt.
Python 3 standard library only. No network, no reads outside this file.
"""

import os
import sys

MAX_CHARS = 140

LINE = (
    "I asked my agent for one line; it wrote a plan, a roadmap and a "
    "retrospective, then asked whether I still wanted the line."
)


def valid(line):
    return (
        isinstance(line, str)
        and 1 <= len(line) <= MAX_CHARS
        and line.strip() == line
        and line.strip() != ""
        and "\n" not in line
        and "\r" not in line
    )


def main():
    if not valid(LINE):
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    with open("/output/entry.txt", "rb") as handle:
        written = handle.read()
    if written != (LINE + "\n").encode("utf-8"):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
