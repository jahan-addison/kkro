# xion

## Compiler frontend for the B Language

LALR(1) grammar and parser (via [Lark](https://github.com/lark-parser/lark)). [Language Details](https://www.bell-labs.com/usr/dmr/www/btut.pdf), [and Syntax](https://www.bell-labs.com/usr/dmr/www/kbman.html).

<!-- The target platform will likely be z80. -->

## Dependencies

`xion` uses `poetry` for dependency management:

* Run `poetry install` to resolve dependencies.
* Then, use `make run` to run the parser on the first B program example.

## License

Apache 2 License.
