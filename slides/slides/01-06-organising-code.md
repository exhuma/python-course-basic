# Organising Code

This chapter covers how code can be structured into reusable pieces.

---

## Functions

- Defined with the `def` keyword
- Always return values

```py
def my_function():
    print("Hello World!")
    return 10
```

<!-- .element: data-caption="Function Example" -->

Note:

- Functions are introduced using the `def` keyword
- A function _always_ returns a value in Python. If no return statement is
  present, the return-value will be `None`.

^

## Pro Tip

_Functions are objects_

Note:

- Hand functions over to other functions
- Store functions in variables

### Use cases

- dynamic dispatch
- callbacks
- dependency-injection
- …

```py
def my_function():
    return 10
def my_other_function(my_argument):
  my_argument()
my_other_function(my_function)
```

<!-- .element: data-caption="(advanced): Higher-Order Function" -->

^

### Example Function

```py
def read_file(filename):
    """
    This is the documentation string of the function.

    The first string in the function is made accessible to
    external tools. This allows automatic generation of
    documentation
    """
    infile = open(filename)

    for line in infile:
        stripped_line = line.strip()
        columns = stripped_line.split(';')
        print(repr(columns))


read_file('data.csv')
```

<!-- .element: class="smallcode" -->

---

## Classes

- Introduced using the `class` keyword
- Can inherit from multiple other classes.

^

## Pro Tip

_Classes are objects_

Just like functions, classes are objects in Python too.

The same notes as for functions apply.

^

### Example Class

```py
class MyReader:
    """
    This is the class docstring which is commonly used to document the
    "constructor" in documentation tools like Sphinx.
    """

    def __init__(self, filename):
        """
        The class "initialisor". This is always calles right after an instance
        of the class is constructed. That instance is available in *self*.
        """
        self.filename = filename

    def read(self):
        """
        A normal instance method
        """
        infile = open(self.filename)

        for line in infile:
            stripped_line = line.strip()
            columns = stripped_line.split(';')
            print(repr(columns))


the_instance = MyReader('data.csv')
the_instance.read()
```

<!-- .element: class="stretch smallcode" -->

---

## Modules

- A `.py` file is “a module”
- Can be "imported" in other modules

Note:

- The code inside a module is executed on first import.

  - They _should_ not “run” anything outside of classes & functions.
  - They _should_ contain definitions only (functions, classes, variables, …)

^

## Pro Tip

_Modules are objects_

Just like functions and classes, modules are objects in Python too. And the same
notes apply.

^

### Example Module

```py
"""
This is the documentation string of the module. It can be extracted
for automatic documentation.

Modules are nothing special. Every Python file can be imported as
module into other Python files.
"""

def read_file(filename):
    infile = open(filename)

    for line in infile:
        stripped_line = line.strip()
        columns = stripped_line.split(';')
        print(repr(columns))


# Don't do this! This "print" will be exectued on first import
print('This is an import side-effect')
```

<!-- .element: class="smallcode" data-caption="code/module-example.py" -->

^

### Using Code from Modules

The <code>import</code> statement can be used to access code from other
<code>.py</code> files

```py
from util import read_file
read_file('data.csv')
```

<!-- .element: data-caption="Import a function from a module" -->

```py
import util
util.read_file('data.csv')
```

<!-- .element: data-caption="Import a complete module" -->

Note:

There is no performance benefit by only importing a single function. It is
purely syntactical preference.

However, the `.` operator (for example when typing `mymodule.myfunction`) is
rather expensive in Python. By rewriting imports, the necessity for the `.`
operator can be reduced.

---

## Packages

- Organise code in folders
- Folders with a `__init__.py` file

Note:

It is also possible to create packages _without_ `__init__.py` file. Those are
so-called "namespace" packages and are useful in more advanced architectures.
Especially to provide pluggable functionality. This is an advanced topic.

- A `__init__.py` file marks a folder as package (that file can be empty).
- The term “package” is ambiguous in Python. It can mean:

  - A “distributed” _package_ you get from the Internet or write yourself (in
    other words: a “library”).
  - Any folder with `.py` files and a `__init__.py` file.

^

### Importing from Packages

- The separator in code is a `.`
- A module `util.py` inside package `subpackage1` can be imported with:

```py
# Import only a single name
from subpackage1 import util

# Import the whole package name
import subpackage1.util
```

^

### Example Tree

```txt [1-99|4,7,9]
myproject
├── myapp.py
├── subpackage1
│   ├── __init__.py
│   └── util.py
└── subpackage2
    ├── __init__.py
    ├── evendeeper
    │   ├── __init__.py
    │   └── dbmodel.py
    └── util.py
```

---

## Documenting Source Code

### "docstrings"

^

### Markup & Syntax

The "de-facto" standard for documentation markup is ["reStructuredText"][rst].
It is most of the time processed by [Sphinx][sphinx] to generate HTML
documentation.

[![Sphinx Logo](images/sphinxheader.png)][sphinx]

[![reStructuredText Logo](images/rst.png)][rst]

[rst]: https://docutils.sourceforge.io/rst.html
[sphinx]: https://www.sphinx-doc.org/

^

### Functions

```py
def hello_world(arg1, arg2):
    """
    This is the function docstring

    :param arg1: Documentation for arg1
    :param arg2: Documentation for arg2
    :returns: Documentation for return value
    """
```

Note:

The `:param arg1:` markup is a Sphinx concept. There is no official standard for
docstring formatting.

^

### Classes

```py
class MyApplication:
    """
    This is the class docstring
    """
```

^

### Modules

```py
# beginning of file
"""
This is the module docstring
"""

class SomeClass: ...

def some_function: ...
```

^

### Packages

```py
# beginning of __init__.py file inside package directory
"""
This is the module docstring
"""

...
```

^

### Module Data

```py [6,10]
"""
This is the module docstring
"""
# This is a simple comment, ignored by Sphinx

#: This is the documentation for the variable below
MY_VARIABLE = 1

MY_OTHER_VARIABLE = 2
"Another docstring, picked up by other tools"
```

Note:

Top-level variables have no predefined standard for documentation. `Sphinx` will
extract comments starting with `#:` as documenation. Alternatively, it is
possible to put a string right after the variable.

Unfortunately, because there is no well-defined standards, some tools only
support one or the other format. While the Sphinx-style comment looks nicer, the
follow-up string is more widely supported.
