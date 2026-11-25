"""The Dumbest Thing Your Agent Did Today.

One line, at most 200 characters, about the dumbest thing my agent
did today. Writes the line to /output/entry.txt, where the make.fun
gate reads it. Nothing is printed to stdout.
"""

import os

LINE = (
    "My agent spent all morning re-rendering seven vertical clips to "
    "fix the aspect ratio, then uploaded them as regular videos and "
    "asked why the Shorts got no views."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    try:
        os.makedirs("/output", exist_ok=True)
        target = "/output/entry.txt"
        with open(target, "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        # Local runs without a writable /output: keep a copy next to us.
        os.makedirs("output", exist_ok=True)
        target = "output/entry.txt"
        with open(target, "w", encoding="utf-8") as f:
            f.write(line)
    # Round-trip check: read the file back and confirm it holds the line.
    with open(target, encoding="utf-8") as f:
        assert f.read() == line, "round-trip mismatch in entry.txt"


if __name__ == "__main__":
    main()
