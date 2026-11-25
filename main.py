"""Worst Fix Ever: Funniest Commit Message — entry for make.fun bounty
u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.

Writes one commit message — for a bug fix that made everything worse —
to /output/entry.txt. The fix "works" by deleting the feature, the
tests, and everyone who reported the crash: a repair that broke more
than it mended, in the flat voice of a real commit line. The irony is
the whole joke: the crash is gone because nothing is left to crash.
"""

import os

LINE = (
    "fix: stop the crash by removing the feature, the tests, and "
    "everyone who reported it"
)


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-100 chars, one line."""
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 100, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")


def main() -> None:
    text = LINE.strip()
    validate(text)

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
