# Language Syntax

^

* The variable type is implicit, but strong (dynamic typing)
* Variables are assigned with the = operator
* Line-comments start with a `#` character. Block comments don’t exist.
* Lines do not need to end with a semicolon (`;`)
* Blocks are defined by indentation. The line starting a block ends with a colon (`:`).

^

```py
# Variable Assignment
my_variable = 10

# Conditional & Blocks
if my_variable >= 10:
    print("Yes")
```
^

### Simple Operations

```py
# Calling the builtin function "print"
print('Hello ' + 'World!')
print(10 + 3)
print(10 / 3)

# Setting variables
a = 'Hello'
b = 'World!'
print(a + b)

a = 10
b = 3
print(a * b)
```


---

### Builtin Functions and Working with Files

* Python has a few [builtin functions][builtins] which are very useful.
* [open()][open] is used to access files on the disk (for reading and writing).
* By default files are opened as “text”.
* Using a for loop on file objects will iterate line-by-line. Newlines are not removed.
* [pathlib][pathlib] and [os.path][path] contain useful functions for working with files.

[builtins]: https://docs.python.org/3/library/functions.html
[open]: https://docs.python.org/3/library/functions.html#open
[pathlib]: https://docs.python.org/3/library/pathlib.html#module-pathlib
[path]: https://docs.python.org/3/library/os.path.html#module-os.path
^

### Reading a File

```py
input_file = open('data/hello.txt')

# "for … in …" knows how to loop over many things
for row in input_file:
    print(row)
```

Contents of `data/hello.txt`

```txt
This is the first line

This is line #3
```

---

## Looping

Executing code on a collection of items (looping) can be done in several ways
in Python:

* A `for ... in` ... loop
* A `while ...` loop
* A comprehension expression (not covered in this course)
* Functional aproach using [map()][map], [filter()][filter] and
  [functools.reduce()][reduce] (not covered in this course).

[map]: https://docs.python.org/3/library/functions.html#map
[filter]: https://docs.python.org/3/library/functions.html#filter
[reduce]: https://docs.python.org/3/library/functools.html#functools.reduce
^

### Example

```py
# Simple loop
mydata = [1, 2, 3, 4]
for item in mydata:
    print(item)

# Loop over each item in a list with an index
mydata = [1, 2, 3, 4]
for i, item in enumerate(mydata):
    print(i, item)

# Loop until the user wants to quit
response = 'y'
while response != 'n':
    response = input('Do you want to continue [y/n]?')
```


---

## Reading Files

Reading and writing files is done using the builtin function [open()][open].
This function will return a “file-like object” which has low-level methods like
[read()][read] and [write()][write].

[read]: https://docs.python.org/3/library/io.html#io.RawIOBase.read
[write]: https://docs.python.org/3/library/io.html#io.RawIOBase.write
[open]: https://docs.python.org/3/library/functions.html#open
^

### Example
```py
# Open a file in default ("read") mode
infile = open('data.csv')


# Iterating over the file object will give us lines (as string)
for line in infile:

    # string objects have many useful methods. "strip" will remove
    # leading and trailing whitespace, ...
    stripped_line = line.strip()

    # ... and "split" will convert a string to a list of strings
    columns = stripped_line.split(';')

    # "repr" is a helper function for debugging. It converts a value
    # into a developer-friendly "representation". For strings this
    # includes the proper quotes (and escapes).
    print(repr(columns))
```
<!-- .element: class="smallcode" -->

^

### CSV File Contents

```txt
name;first_name;phone;email
Doe;John;12345;jdoe@exampe.com
Dane;John;12345;jdoe@exampe.com
```

^

### Closing Files

File should always be closed. Especially when writing into files.

Python can ensure that this is done correctly by using the `with` statement:

```py
with open('data.csv') as infile:
    do_something_with(infile)
    print(infile.closed)  # Will print "False"

# Variables created in the "with" block will remain accessible,
# but cleanup has taken place. In this case, the file will be
# closed now.
print(infile.closed)  # Will print "True"
```

---

# Organising Code

This chapter covers how code can be structured into reusable pieces.


---

## Functions

* Functions are introduced using the `def` keyword
* A function *always* returns a value in Python. If no return statement is
  present, the return-value will be `None`.

^

<div class="admonition tip">
<strong>Advanced:</strong> Functions are objects!

Functions are objects in Python (of type function). As soon as a function is defined, that function can also be assigned to variables and passed into functions. Useful for dynamic dispatch, callbacks, dependency-injection, …
</div>

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

* Classes are introduced using the `class` keyword.
* Classes can inherit from multiple other classes.
* Classes offer advanced programming techniques not covered in this course
  (static-methods, class-methods, properties, descriptors)

^

<div class="admonition tip">
<p><strong>Advanced:</strong> Classes are objects.</p>
<p>Just like functions, classes are objects in Python too (of type type).</p>
</div>

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


* Every Python file can be called a “module” and can be imported in other
  Python scripts.
* The code inside a module is executed on first import.
  * They *should* not “run” anything outside of classes & functions.
  * They *should* contain definitions only (functions, classes, variables, …)

^

<div class="admonition tip">
<p><strong>Advanced:</strong> Classes are objects.</p>
<p>Just like functions and classes, modules are objects in Python too (of type
module).</p>
</div>

^

### Example Module

```py
# filename: util.py
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
<!-- .element: class="stretch" -->

^

### Using Code from Modules

<p class="prose">
The <code>import</code> statement can be used to access code from other <code>.py</code> files:
</p>

```py
from util import read_file
read_file('data.csv')
```
```py
import util
util.read_file('data.csv')
```

^

### Imports & Caching

* Importing will cause .pyc files to be created (inside the `__pycache__`
  folder). They are auto-generated and don’t belong into revision control.
* Imports are cached. The code inside a module is only interpreted on first
  import. (Advanced: The cached modules are available in `sys.modules`).
* Therefore, modules can be abused as global variable storage & singletons
  (with all the risks this implies).

---

## Packages

* Use packages to organise your project into sub-folders.
* A `__init__.py` file marks a folder as package (can be empty).
* The term “package” is ambiguous in Python. It can mean:
  * A “distributed” *package* you get from the Internet or write yourself (in
    other words: a “library”).
  * Any folder with `.py` files and a `__init__.py` file.

^

### Importing from Packages

* Packages are like folders
* The separator in code is `.`
* A module util.py inside package subpackage1 can be imported with:

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

# Demo

---

## Documenting Source Code

### "docstrings"

^

### Markup & Syntax

The "de-facto" standard for documentation markup is ["reStructuredText"][rst].
It is most of the time processed by [Sphinx][sphinx] to generate HTML
documentation.

<img src="images/sphinxheader.png" />
<img src="images/rst.png" />

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
# begin of file
"""
This is the module docstring
"""

class SomeClass: ...

def some_function: ...
```

^

### Packages

```py
# begin of __init__.py file inside package directory
"""
This is the module docstring
"""

...
```

^

### Module Data

Top-level variables have no predefined standard for documentation. `Sphinx` will
extract comments starting with `#:` as documetnation:

```py [6]
"""
This is the module docstring
"""
# This is a simple comment, ignored by Sphinx

#: This is the documentation for the variable below
MY_VARIABLE = 1
```
