"""Fortune Cookie Wisdom for Developers.

Writes exactly one fortune-cookie line for developers to entry.txt —
a true line about a developer's day, with a twist at the end.
Deterministic, standard library only, no network, no input, no clock.
"""

import os

LINE = "The bug you chase at midnight was written by the you who swore this code was finished."


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
