import sys
import argparse

from tagit import __version__


def main(arguments=None):

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-V', '--version', action='version', version='tagit {}'.format(__version__))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
