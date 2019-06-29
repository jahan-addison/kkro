# kkro

> B Language Compiler

## Details

LALR(1) grammar and parser (via lark). [Language Details](https://www.bell-labs.com/usr/dmr/www/btut.pdf), [and Syntax](https://www.bell-labs.com/usr/dmr/www/kbman.html).

The target platform will likely be z80.

*Note*: Development has slowed due to Python's poor transition to flex/bison style and/or parser combinators. I find a partiuclar dislike in older lex/yacc parser design.

## Dependencies

`kkro` uses `poetry` for dependency management:

* Run `poetry install` to resolve dependencies.
* Then, use `make start` to begin the program.

## License

Apache 2 License, unless otherwise specified.
