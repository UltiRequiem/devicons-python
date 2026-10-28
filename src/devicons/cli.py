"""`devicons` command line: print paths with their icons, or check your font."""

from __future__ import annotations

import argparse
import os
import sys
from collections.abc import Sequence

from . import __version__, icon_for

# One glyph per Nerd Font set that this package uses, so a missing set is easy to spot.
FONT_CHECK = (
    ("Seti-UI + Custom", "", "Python"),
    ("Devicons", "", "JavaScript"),
    ("Font Awesome", "", "generic file"),
    ("Octicons", "", "GitHub"),
    ("Material Design", "\U000f0226", "PDF"),
)


def check_font(out=sys.stdout) -> int:
    out.write("If every line below shows an icon (not an empty box or a question mark),\n")
    out.write("your font is ready. If not, see docs/fonts.md.\n\n")
    for family, glyph, label in FONT_CHECK:
        out.write(f"  {glyph}   U+{ord(glyph):X}  {family} ({label})\n")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="devicons",
        description="Print files and folders with their Nerd Font icons.",
    )
    parser.add_argument("paths", nargs="*", help="paths to show (default: the current directory)")
    parser.add_argument(
        "--check-font", action="store_true", help="print one glyph per icon set to test your font"
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args(argv)

    if args.check_font:
        return check_font()

    paths = args.paths
    if not paths:
        paths = sorted(os.listdir("."), key=str.lower)

    status = 0
    for path in paths:
        if os.path.exists(path) or not args.paths:
            print(f"{icon_for(path)} {path}")
        else:
            print(f"devicons: {path}: no such file or directory", file=sys.stderr)
            status = 1
    return status


if __name__ == "__main__":
    raise SystemExit(main())
