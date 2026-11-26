#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry writer.

Writes a single funny line (<=200 chars, one line) to
$MAKEFUN_OUTPUT_DIR/entry.txt, as the competition gate requires.
"""
import os

ENTRY = "I asked AI to summarize my life and it returned one word: 'pending.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate"
    assert "\n" not in text, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    # Confirm what landed on disk matches the line exactly.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == text, "entry.txt mismatch"


if __name__ == "__main__":
    main()
