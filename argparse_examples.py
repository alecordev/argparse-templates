import sys
import argparse


class AlecorParser(argparse.ArgumentParser):
    """
    Handle special case and show help on invalid argument
    """

    def error(self, message):
        sys.stderr.write('\nERROR: {}\n\n'.format(message))
        self.print_help()
        sys.exit(2)


def main():
    try:

        parser = AlecorParser(epilog='epilog')
        parser.add_argument('-v', '--version', action='version', version='0.1')
        parser.add_argument('-l', '--log', metavar=('SAMPLE1'), help='1 var expected: SAMPLE1')
        parser.add_argument('-t', '--two-variables', nargs=2, metavar=('VAR1', 'VAR2'), help='2 vars expected: VAR1 VAR2')  # 2 vars received as a list, order kept
        parser.add_argument('-f', '--flag', action='store_true', help='Flag option (True/False)')                           # if specified, its value is True
        parser.add_argument('-d', '--default', help='help text for default')

        parser.add_argument('var', type=int, help='var will be considered int')                                 # like a positional argument, required
        parser.add_argument('--verbosity', type=int, choices=[0, 1, 2], help='increase output verbosity')       # only 0, 1 or 2 can be passed
        parser.add_argument('-c', '--count', action='count', help='count help', default=0)                      # -c -c -c = 3
        args = parser.parse_args()

        if len(sys.argv) < 2:
            parser.print_help()
            sys.exit(0)

        if args.log:
            print(args.log)

        if args.flag:
            print(args.flag)

        if args.two_variables:
            print(args.two_variables)

        if args.var:
            print(args.var)

        if args.count:
            print(args.count)

        if args.verbosity:
            print(args.verbosity)

        if args.flag:
            print(args.flag)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
