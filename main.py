#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Brian McIlwain"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
from summarizer.summarizer import summarize


def main(args):
    """ Main entry point of the app """
    summarize(args.text)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    parser.add_argument("text", help="Text to summarize")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
