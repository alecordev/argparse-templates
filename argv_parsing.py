"""
Example implementation for reading all arguments sent.
"""

import sys


def parse_arg(arg):
    """
    Examples:

    >>> parse_arg('--name=nombre')
    {'name': 'nombre'}
    >>> parse_arg('--some-value=1')
    {'somevalue': '1'}

    Arguments
    ---------
        arg: Argument string to clean.
    """
    return dict(zip(*[iter(arg.replace('-', '').split('='))] * 2))


def main():
    try:
        for arg in sys.argv[1:]:
            print(parse_arg(arg))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
