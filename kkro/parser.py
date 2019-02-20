from lark import Lark, Tree, Transformer
from typing import Optional
import logging

logging.basicConfig(level=logging.DEBUG)


class ParserError(Exception):
    """Parser Exception """
    pass


class Parser:
    """Parser and adapter with lark for a source B program.

    Build and transform a parse tree for syntax-directed translation.

    Attributes:
        source_program(str): The source B program.
        transformer(Transformer): Syntax-directed transformer.
        Parser(Lark): Lark LALR(1) parser instance.
        grammar(string): LALR(1) grammar that passes to lark.
        tree(Tree): Parse tree.

    """

    def __init__(self, source_program: str, transformer=None, debug=True, grammar='./grammar.lark') -> None:
        """Initialize parser."""
        self.source = source_program
        self.transformer: Optional[Transformer] = transformer
        self.grammar: Optional[str] = None
        self.parser: Optional[Lark] = None
        self._tree: Optional[Tree] = None
        self._read_grammar(grammar)

    def get_parse_tree(self) -> Tree:
        """Get the parse tree."""
        if isinstance(self._tree, Tree):
            return self._tree
        else:
            raise ParserError('Error building parse tree')

    def print_parse_tree(self) -> None:
        """Print the parse tree."""
        if isinstance(self._tree, Tree):
            print(self._tree.pretty())
        else:
            raise ParserError('Error printing parse tree')

    def _set_parser(self, grammar: str) -> None:
        """Set lark instance and parse tree."""
        if isinstance(self.grammar, str):
            self.parser = Lark(self.grammar,
                               start='program',
                               parser='lalr',
                               transformer=self.transformer,
                               debug=True)
            self._tree = self.parser.parse(self.source)

    def _read_grammar(self, location: str) -> None:
        """Read grammar from disk and initialize parser."""
        with open(location) as file:
            self.grammar = file.read()
            self._set_parser(self.grammar)
