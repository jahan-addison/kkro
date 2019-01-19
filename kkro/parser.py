from lark import Lark
import logging

logging.basicConfig(level=logging.DEBUG)

sample = '''

'''

with open('kkro/grammar.lark') as file:
    grammar = file.read()
    parser = Lark(grammar,
                  start='program',
                  parser='earley',
                  lexer='dynamic',
                  debug=True)
    print(parser.parse(sample).pretty())
