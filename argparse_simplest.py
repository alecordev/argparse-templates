"""
https://docs.python.org/2/library/argparse.html
"""

import sys
import argparse

def main():
    pass

if __name__ == '__main__':

    try:

        parser = argparse.ArgumentParser(epilog='v{}')
        parser.add_argument('-v', '--version', action='version', version='0.1')
        parser.add_argument('-l', '--log', metavar=('SAMPLE1'), help='1 var expected: SAMPLE1')
        parser.add_argument('-t', '--two', nargs=2, metavar=('VAR1', 'VAR2'), help='2 vars expected: VAR1 VAR2')
        parser.add_argument('-f', '--flag', action='store_true', help='Flag option (True/False)')
        parser.add_argument('-d', '--default', help='help text for default')

        parser.add_argument('var', type=int, help='var will be considered int')
        parser.add_argument('-v', '--verbosity', type=int, choices=[0, 1, 2], help='increase output verbosity')
        parser.add_argument('-c', '--count', action='count', help='count help', default=0)
        args = parser.parse_args()

        if len(sys.argv) < 2:
            parser.print_help()
            sys.exit(0)

        if args.log:
            print(args.log)

        if args.flag:
            print(args.flag)
            main()

    except Exception as e:
        print(e)
