
if __name__ == '__main__':
    from xion.parser import Parser
    from argparse import ArgumentParser

    args_parser = ArgumentParser()
    args_parser.add_argument("-f", "--file",
                             dest="filename", help="write report to FILE", metavar="FILE")
    args_parser.add_argument("-p", "--pretty", required=False, action='store_true',
                             dest="pretty", default=False, help="pretty print parse tree")

    args = args_parser.parse_args()

    with open(args.filename) as file:
        parser = Parser(file.read())
        parser.print_parse_tree(args.pretty)
