from lark import Tree, Transformer, Discard


class AST_Transformer(Transformer):
    def constant_expression(self, args):
        """Reduce constant expression trees to their children"""
        return args[0]

    def number_literal(self, args):
        """Merge number literals and turn them into an int """
        return Tree('number_literal', [int(''.join(args))])

    def string_literal(self, args):
        """Merge string literals """
        return Tree('string_literal', [''.join(args)])

    def constant_literal(self, args):
        """Merge constant literals """
        return Tree('constant_literal', [''.join(args)])

    def TERMINATE(self, name):
        """Throw away ';' """
        return Discard
