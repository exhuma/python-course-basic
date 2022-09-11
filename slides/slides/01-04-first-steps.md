# First Steps
^

## The Python Shell (REPL)

* read-eval-print loop.
* Interactive shell.
* Extremely helpful tool to test out ideas, play with code before implementing it.
^

Simply run `python3` on the console to start it.

By convention, lines with `>>>` represent a REPL prompt.

```py
>>> 1 + 1
2

>>> print("Hello World!")
Hello World!
```
^

The default REPL can be customized using a Python script and setting
`PYTHONSTARTUP` o that file. For example: [exhuma/dotfiles/.pystartup][pystartup]

[pystartup]: https://github.com/exhuma/dotfiles/blob/master/.pystartup

Alternative Python Shell: https://ipython.org/:

```bash
pip install --user ipython
source /path/to/env/bin/activate  # if needed
ipython
```
^

## Getting Help

* On the web: http://docs.python.org
* Type `help()` in the REPL. This can be used on any object:

  ```py
  >>> myvar = 1
  >>> help(myvar)  # This will open the help for "ints"
  ```

* Type `python -m pydoc` in the shell.
  * Like man-pages for Python.
  * Same as `help()` in the REPL.
  * Served via HTTP: `python -m pydoc -b`
