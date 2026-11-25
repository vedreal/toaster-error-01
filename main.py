#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line (at most 120 characters) to /output/entry.txt: the error
message a kitchen toaster shows its owner when something goes wrong.
Stdlib only. No network, no secrets, no files read from outside the repo.
"""

ENTRY = "ERROR: 4,000 slices toasted. Zero thanks received. I am now on strike."


def validate(text):
    """Gate check, mirroring the competition gate: 1-120 chars, UTF-8, not blank."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not 1 <= len(text) <= 120:
        raise ValueError("entry must be 1-120 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def output_path():
    """Resolve /output/entry.txt, falling back to ./output/entry.txt."""
    import os
    for base in ("/output", os.path.join(os.getcwd(), "output")):
        try:
            os.makedirs(base, exist_ok=True)
            return os.path.join(base, "entry.txt")
        except OSError:
            continue
    raise OSError("cannot create output directory")


def main():
    text = validate(ENTRY)
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "read-back mismatch"
    print("wrote %d chars to %s" % (len(written), path))


if __name__ == "__main__":
    main()
