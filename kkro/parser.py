from lark import Lark, Tree, Transformer
from typing import Optional
import logging

# Initialize logging for lark.
logging.basicConfig(level=logging.DEBUG)


class Parser:
    """Parser and adapter with lark.

    Build and transform a parse tree for syntax-directed translation of
    a source program. Initializes with the provided LALR(1) lark grammar.

    Args:
        source_program: The source B program.
        transformer: Syntax-directed transformer.
        debug: Debug flag in Lark.
        grammar: Optional alternative LALR(1) grammar that passes to lark.

    Attributes:
        source_program: The source program.
        transformer: Syntax-directed transformer.
        parser: Lark LALR(1) parser instance.
        grammar: LALR(1) grammar that passes to lark.
        tree: Parse tree.

    """
    def __init__(self, source_program: str, transformer=None, debug=True, grammar='kkro/b_grammar.lark') -> None:
        self.source = source_program
        self.transformer: Optional[Transformer] = transformer
        self.grammar: Optional[str] = None
        self.parser: Optional[Lark] = None
        self._read_grammar(grammar)
        self.parser = Lark(
            self.grammar,
            start='program',
            parser='lalr',
            transformer=self.transformer,
            debug=True)
        self._tree = self.parser.parse(self.source)

    def get_parse_tree(self) -> Tree:
        """Get the current parse tree.

        Returns:
            The current state of the parse tree.

        """
        return self._tree

    def print_parse_tree(self) -> None:
        """Print the current parse tree."""
        print(self._tree.pretty())

    def _read_grammar(self, location: str) -> None:
        """Read source grammar.

        Read a grammar from location on disk.

        Args:
            grammar: The source LALR(1) grammar.

        """
        with open(location) as file:
            self.grammar = file.read()
