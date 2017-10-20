import sys
import argparse

from . import __version__


def main(arguments=None):

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-V', '--version', action='version', version='tagit {}'.format(__version__))

    args = parser.parse_args(arguments or sys.argv[1:])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
