"""news-image-20261119 entry program.

The world in one image - Thursday 19 November 2026.

The image beside this script (entry.png) sums up the day the leaders
of the United States, China and Russia - Donald Trump, Xi Jinping
and Vladimir Putin - sat down in Shenzhen for the first trilateral
summit in history, on the sidelines of the APEC forum. Running this
program publishes that image, byte for byte, to /output/entry.png.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")


def publish() -> int:
    if not os.path.isfile(SOURCE):
        print(f"error: entry image not found: {SOURCE}", file=sys.stderr)
        return 1
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    written = os.path.getsize(DEST)
    expected = os.path.getsize(SOURCE)
    if written != expected:
        print(
            f"error: copied image is {written} bytes, expected {expected}",
            file=sys.stderr,
        )
        return 1
    print(f"wrote {DEST} ({written} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(publish())
