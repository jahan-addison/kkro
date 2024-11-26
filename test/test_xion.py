import pytest
from os import getcwd

from xion import __version__
from xion.parser import Parser

from .fixture.program_1_parse_tree import program_example_1_parse_tree
from .fixture.program_2_parse_tree import program_example_2_parse_tree
from .fixture.program_3_parse_tree import program_example_3_parse_tree

def test_version() -> None:
    assert __version__ == '1.0.1'

def test_program_1_parse_tree(program_example_1_parse_tree: str) -> None:
    with open(getcwd() + '/examples/1.b') as file:
        parser = Parser(file.read())
        assert(str(parser.get_parse_tree()) == program_example_1_parse_tree)

def test_program_2_parse_tree(program_example_2_parse_tree: str) -> None:
    with open(getcwd() + '/examples/2.b') as file:
        parser = Parser(file.read())
        assert(str(parser.get_parse_tree()) == program_example_2_parse_tree)

def test_program_3_parse_tree(program_example_3_parse_tree: str) -> None:
    with open(getcwd() + '/examples/3.b') as file:
        parser = Parser(file.read())

        assert(str(parser).replace('\t', ' ' * 4) == program_example_3_parse_tree)

