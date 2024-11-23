# xion

## Compiler frontend for the B Language

LALR(1) grammar and parser (via [Lark](https://github.com/lark-parser/lark)). [Language Details](https://www.bell-labs.com/usr/dmr/www/btut.pdf), [and Syntax](https://www.bell-labs.com/usr/dmr/www/kbman.html).

<!-- The target platform will likely be z80. -->

## Dependencies

`xion` uses `poetry` for dependency management. Run `poetry install` to install dependencies.

## Usage

* `make run` to run the parser on the first B program example
* `make test` to run the test suite and verify grammar correctness

This project was created for [roxas](https://github.com/jahan-addison/roxas) as the frontend for a B compiler.

## License

Apache 2 License.
