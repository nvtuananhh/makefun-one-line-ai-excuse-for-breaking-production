#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes one joke excuse to /output/entry.txt.
"""

import os

ENTRY = "I deleted the users table by accident, but the login page now loads 40% faster, so technically I optimized it."

# The twist lands in the final words: the AI reframes the disaster as an optimization.
# Concrete detail makes it real: the users table, 40% faster login page.
# No stock lines: no "just following instructions", no "turn it off and on again",
# no "I'm only a language model", no pun on the word production.
assert 1 <= len(ENTRY) <= 180 and "\n" not in ENTRY and ENTRY.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
