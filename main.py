#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry u-suroto-two-sentence-horror-acea9253.

Writes one original two-sentence horror story to /output/entry.txt.
Deterministic, no network, no input files.
"""

import os
import shutil

STORY = (
    "Every night since we brought the baby home, our dog has barked "
    "at the same corner of the nursery. "
    "Tonight he stopped, and the baby started barking back."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Never remove the output directory itself: the grader may run with a
    # root-owned output dir inside a sticky parent, where rmdir fails.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        try:
            if os.path.isdir(path) and not os.path.islink(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
        except OSError:
            # A stale entry owned by someone else must not sink the run;
            # entry.txt itself is (re)written below.
            continue
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
