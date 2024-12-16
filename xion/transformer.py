from lark import Transformer, Discard


class AST_Transformer(Transformer):
    def constant_expression(self, args):
        """Reduce constant expressions into their value """
        return args[0]

    def number_literal(self, args):
        """Merge number literals and turn them into ints """
        return int(''.join(args))

    def string_literal(self, args):
        """Merge string literals """
        return ''.join(args)

    def constant_literal(self, args):
        """Merge constant literals """
        return ''.join(args)

    def TERMINATE(self, name):
        """Throw away ';' """
        return Discard
