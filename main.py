"""Pickup line for machines.

One machine-learning-flavoured pickup line (80 characters, within the
bounty limit), written to entry.txt by main().
"""

import os

ENTRY = "I must be overfitting: one epoch with you and I can't generalize to anyone else."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
