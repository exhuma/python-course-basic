# Organising Code

This chapter covers how code can be structured into reusable pieces.

---

## Functions

- Functions are introduced using the `def` keyword
- A function _always_ returns a value in Python. If no return statement is
  present, the return-value will be `None`.

^

## Pro Tip: Functions are objects

- Hand functions over to other functions
- Store functions in variables

### Use cases

- dynamic dispatch
- callbacks
- dependency-injection
- …

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

<!-- .element: class="stretch smallcode" -->

---

## Classes

- Classes are introduced using the `class` keyword.
- Classes can inherit from multiple other classes.
- Classes offer advanced programming techniques not covered in this course
  (static-methods, class-methods, properties, descriptors)

^

## Pro Tip: Classes are objects

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

- Every Python file can be called a “module” and can be imported in other
  Python scripts.
- The code inside a module is executed on first import.
  - They _should_ not “run” anything outside of classes & functions.
  - They _should_ contain definitions only (functions, classes, variables, …)

^

## Pro Tip: Modules are objects

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

<!-- .element: class="stretch" data-caption="code/module-example.py" -->

^

### Using Code from Modules

<p class="prose">
The <code>import</code> statement can be used to access code from other
<code>.py</code> files:
</p>

```py
from util import read_file
read_file('data.csv')
```

```py
import util
util.read_file('data.csv')
```

---

## Packages

- Use packages to organise your project into sub-folders.
- A `__init__.py` file marks a folder as package (can be empty).
- The term “package” is ambiguous in Python. It can mean:
  - A “distributed” _package_ you get from the Internet or write yourself (in
    other words: a “library”).
  - Any folder with `.py` files and a `__init__.py` file.

^

### Importing from Packages

- Packages are like folders
- The separator in code is `.`
- A module util.py inside package subpackage1 can be imported with:

```py
from subpackage1 import util  # Import only this name
```

```py
import subpackage1.util  # Import the whole package name
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

Top-level variables have no predefined standard for documentation. `Sphinx` will
extract comments starting with `#:` as documetnation. Alternatively, it is
possible to put a string right after the variable:

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
