
if __name__ == '__main__':
    from kkro.parser import Parser
    with open('./examples/1.b') as file:
        parser = Parser(file.read())
        parser.print_parse_tree()
