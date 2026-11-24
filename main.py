#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes one two-sentence horror story to /output/entry.txt.

The story is fixed and deterministic: every run writes the exact
same bytes, so the two grading runs produce identical output.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

STORY = (
    "My phone keeps changing my sister's name to remains "
    "whenever I type it. "
    "I opened the custom dictionary to delete the entry and found "
    "it was added the day she was born, by an account that has "
    "not logged in since."
)


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()
