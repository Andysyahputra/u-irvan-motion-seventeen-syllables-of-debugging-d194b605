#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — writes one haiku to /output/entry.txt.

Stdlib only. Deterministic: two runs produce byte-identical output.
Validates the haiku before writing: three lines, 5-7-5 syllables,
1-200 characters total.
"""

import os

HAIKU = """cursor blinks at three
one log line scrolls past midnight
and the bug was me"""

# Syllable counts for every word used in the haiku.
SYLLABLES = {
    "the": 1, "cursor": 2, "blinks": 1, "on": 1, "at": 1, "three": 1,
    "a": 1, "one": 1, "log": 1, "line": 1, "scrolls": 1, "past": 1,
    "midnight": 2, "and": 1, "bug": 1, "was": 1, "me": 1,
}


def count_syllables(line):
    return sum(SYLLABLES[word.strip(".,").lower()] for word in line.split())


def main():
    lines = HAIKU.split("\n")
    assert len(lines) == 3, "haiku must be exactly three lines"
    counts = [count_syllables(line) for line in lines]
    assert counts == [5, 7, 5], "syllable counts must be 5-7-5, got %s" % (counts,)
    text = "\n".join(lines) + "\n"
    assert 1 <= len(text) <= 200, "entry must be 1-200 chars, got %d" % len(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
