#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun entry.

Writes exactly one line (the excuse a gamer texts the boss to skip
work during GTA 6 launch week) to <output>/entry.txt with no trailing
newline. Standard library only.
"""

import os

ENTRY = "fridge leaked overnight, kitchen floor's soaked, mopping before it hits the sockets"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
