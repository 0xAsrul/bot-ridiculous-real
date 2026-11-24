"""Ridiculous at First Glance, Real by the Second.

Writes one sentence pitching a bizarre startup idea that sounds absurd
until you realise it would actually sell.
"""

import os

ENTRY = (
    "We rent out professional debaters to win your family's holiday "
    "dinner arguments, because losing to your uncle costs more pride "
    "than our $150-a-night fee."
)


def main() -> None:
    # Entry must fit the competition limit: one line, at most 200 chars.
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, limit is 200"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
