# First Steps

^

## The Python Shell (REPL)

- read-eval-print loop
- Interactive shell
- Experiment with simple code

Note:

The REPL is extremely helpful tool to test out ideas and play with code before
implementing it.

Or even import your own code and test if it behaves correctly.

^

Run `python` without arguments to start

```py
>>> 1 + 1
2
>>> print("Hello World!")
Hello World!
```

<!-- .element: data-caption="Example REPL session" -->

Note:

By convention, lines with `>>>` represent a REPL prompt.

^

## REPL Customisation

- `PYSTARTUP` environment variable <p class="smallnote">(example: [exhuma/dotfiles/.pystartup][pystartup])</p>
- Alternative: [`ipython`][ipython]

[pystartup]: https://github.com/exhuma/dotfiles/blob/master/.pystartup
[ipython]: https://ipython.org/

Note:

The `PYTHONSTARTUP` environment variable can point to any Python file. It is
executed every time a new Python REPL is opened.

Optionally, the alternative [ipython](https://ipython.org/) shell can be used
which has many more advanced features. But setting it up for each project (with
related dependencies) is more cumbersome.

```bash
source /path/to/env/bin/activate  # if needed
pip install ipython
ipython
```

^

## Getting Help

- On the web: http://docs.python.org
- The `help()` function
- `pydoc` (like MAN-pages)

Note:

When in the REPL, calling `help()` on any variable will open the appropriate
documentation:

```py
>>> myvar = 1
>>> help(myvar)  # This will open the help for "ints"
```

Additionally, documentation of all object in the current environment (standard
library & installed third-party modules) is available by running `python -m pydoc` in the shell:

- Like man-pages for Python.
- Same as `help()` in the REPL.
- Served via HTTP: `python -m pydoc -b`
