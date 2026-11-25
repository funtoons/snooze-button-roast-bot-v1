"""Snooze Button Roast — make.fun entry.

Writes a single one-line roast of an alarm clock that rings at 6 AM on a
Saturday to /output/entry.txt. Deterministic, offline, standard library only.
"""

import os

ENTRY = (
    "My alarm rings at 6 AM every Saturday, then gives me nine more minutes "
    "\u2014 the only thing in my life that keeps its promises and still gets hit."
)

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
assert 1 <= len(ENTRY.strip()) <= 200, len(ENTRY)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
