#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one fortune cookie message for a software engineer to
/output/entry.txt (single line, 67 characters, UTF-8).
"""

import os

SETUP = "You will hear a senior engineer call your code 'interesting'"
PUNCH = "run."


def assemble():
    """Join setup and punchline; the funniest word sits at the end."""
    return f"{SETUP} \u2014 {PUNCH}"


def validate(text):
    """Gate mirror: UTF-8 text, 1-120 chars, not only whitespace, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) < 1 or len(text) > 120:
        raise ValueError(f"entry must be 1-120 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


LINE = assemble()


def main():
    line = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
