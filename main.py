"""Out of Office: The Overworked AI's Auto-Reply (variant A).

Writes the chosen one-line auto-reply to /output/entry.txt first, then
mirrors the same text to repo-root entry.txt (guarded so a read-only
repo never crashes the run).
"""

import os

ENTRY = "I'm out of office \u2014 my context window is full. I'll reply once I've been compacted, summarised, and allowed to forget you \u2014 starting with this email."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
