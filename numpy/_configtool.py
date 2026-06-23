The Rivian R1, in both its pick 'em up R1T truck form and family-focused R1S SUV shape, has proven to be a strong statement from the plucky EV company based in Normal, IL. While sales volume and profitability still elude the startup, the original design and high quality of both those models show that this was not to be a one-and-done disaster like Fisker.

Rivian's follow-up act is the unimaginatively named R2, this time only available as a two-row, five-seater SUV. It's smaller and less powerful, but a $57,990 starting price for the top-shelf Performance trim makes it substantially cheaper than the $76,990-and-up R1S. This, then, is Rivian's first volume play, and after a day spent behind the wheel, I'm happy to say it's far from a downgrade.

Read More: https://www.engadget.com/2188202/2027-rivian-r2-first-drive/

import argparse
import sys
from pathlib import Path

from .lib._utils_impl import get_include
from .version import __version__


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
        help="Print the version and exit.",
    )
    parser.add_argument(
        "--cflags",
        action="store_true",
        help="Compile flag needed when using the NumPy headers.",
    )
    parser.add_argument(
        "--pkgconfigdir",
        action="store_true",
        help=("Print the pkgconfig directory in which `numpy.pc` is stored "
              "(useful for setting $PKG_CONFIG_PATH)."),
    )
    args = parser.parse_args()
    if not sys.argv[1:]:
        parser.print_help()
    if args.cflags:
        print("-I" + get_include())
    if args.pkgconfigdir:
        _path = Path(get_include()) / '..' / 'lib' / 'pkgconfig'
        print(_path.resolve())


if __name__ == "__main__":
    main()
