from lark import Lark
import logging

logging.basicConfig(level=logging.DEBUG)

sample = '''
printn(n, b) {
        extrn putchar;
        auto a;

        if (a = n / b)        /* assignment, not test for equality */
                printn(a, b); /* recursive */
        putchar(n % b + '0');
}
'''

with open('kkro/grammar.lark') as file:
    grammar = file.read()
    test = Lark(grammar, start='program', debug=True)
    print(test.parse(sample))
