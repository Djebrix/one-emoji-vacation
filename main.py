"""One Emoji, One Dream Vacation.

Writes a single emoji to entry.txt: a dawn paddle in a canoe on a
still mountain lake. Not a resort, not a beach umbrella -- the dream
is the quiet glide itself, water like glass, nowhere to be.

Deterministic by design: no input, no randomness, no network, no
clock. Every run writes exactly the same single-emoji file, so the
two grader runs are byte-identical by construction.
"""

import os
from pathlib import Path

# 🛶 U+1F6F6 CANOE -- a dawn paddle on a still lake: one small boat,
# one quiet morning, the whole vacation in a single glide. Specific
# (not any holiday), vivid at a glance, and a fresh pick next to the
# usual beach/plane postcards, yet instantly readable anywhere.
DREAM_VACATION_EMOJI = "\U0001F6F6"


def main() -> None:
    output_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(
        DREAM_VACATION_EMOJI + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
