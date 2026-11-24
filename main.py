"""One sentence explaining the modern internet to a traveler from 1800.

The sentence is written to /output/entry.txt. Pure standard library,
deterministic: the same sentence is written on every run.
"""

import os

SENTENCE = (
    "It is one road joining every post office and library on earth, "
    "so any letter, book, or voice can reach any home in a breath, "
    "and any home can answer back."
)


def main():
    # Gate, mirroring the sealed scorer: 1-200 chars, not only whitespace,
    # exactly one sentence.
    assert 1 <= len(SENTENCE) <= 200, len(SENTENCE)
    assert SENTENCE.strip() == SENTENCE
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith(".")
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
