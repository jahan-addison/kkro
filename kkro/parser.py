from lark import Lark
import logging

logging.basicConfig(level=logging.DEBUG)

sample = '''
main () {
   auto j,s[20],t[20];
   reread(); /* get command line */
   getstr(s); /* put into s */
   j = getarg(t,s,0); /* skip H* name */
   j = getarg(t,s,j); /* filel */
   openr( 5,t );
   getarg(t,s,j); /* file2 */
   openw( 6,t );
   while( putchar( getchar() ) != '*e' ) ; /* copy contents */
   }

'''

with open('kkro/grammar.lark') as file:
    grammar = file.read()
    test = Lark(grammar,
                start='program',
                parser='earley',
                lexer='dynamic',
                debug=True)
    print(test.parse(sample).pretty())
