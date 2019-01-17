from lark import Lark
import logging

logging.basicConfig(level=logging.DEBUG)

sample = '''
main( ) {
  extrn a, b, c;
  putchar(a);
  putchar(b);
  putchar(c);
  putchar('!*n');
}

a 'Hell';
b 'o, W';
c 'orld';
'''

with open('kkro/grammar.lark') as file:
    grammar = file.read()
    test = Lark(grammar, start='program', debug=True)
    print(test.parse(sample).pretty())
