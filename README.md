# kkro

> B Language Compiler

## Details

Built with Earley (soon LALR(1)) grammar and parser (via lark). [Language Details](https://www.bell-labs.com/usr/dmr/www/btut.pdf), [and Syntax](https://www.bell-labs.com/usr/dmr/www/kbman.html).

I am still deciding the target platform. It will most likely be an older hardware emulation with word size, stack, and flash memory large enough for the B language.

## Dependencies

`kkro` uses `poetry` for dependency management:

* Run `poetry install` to resolve dependencies.
* Then, use `make start` to begin the program.

## License

Apache 2 License