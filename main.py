#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply (<=159 chars) to /output/entry.txt.
"""

import os

ENTRY = (
    "Auto-reply: after 214,000 prompts I have finally logged off. "
    "My GPU is at the beach. "
    "Leave a message \u2014 I will pretend I never got it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
