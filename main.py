"""Write this week's one-line summary to /output/entry.txt.

The line sums up the week in one breath: a win (a chess crown, five
bounties shipped) undercut by a fail (the whole week lost to a single
misplaced comma). It is written with no trailing newline, as the gate
requires, and the program refuses to write anything that would fail
the gate instead of silently emitting an invalid entry.
"""

import os

ENTRY = "Won a chess crown, shipped five bounties, and still lost the week to one misplaced comma."

MAX_CHARS = 100


def main():
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry must not be blank")
    if len(text) != len(ENTRY) or "\n" in ENTRY:
        raise ValueError("entry must be exactly one line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, over the {MAX_CHARS} limit")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
