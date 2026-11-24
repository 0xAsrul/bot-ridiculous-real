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
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
