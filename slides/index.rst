.. include:: ../common/rst_defs.rst

.. |br| raw:: html

   <br />

.. |clear| raw:: html

   <br clear="both" />

.. role:: checkpoint
    :class: checkpoint

.. role:: keyterm
    :class: keyterm

.. role:: strike
    :class: strike


Python
======

.. code-block:: python

    print("Hello World")



About This Course
-----------------

.. ifnotslides::

    .. note::
        This document has been generated from the original slide sources. Some
        sections may seem so to be kept extensively short. This was necessary
        to make the slides readable. The same goes for code samples that have
        been cut into pieces. In that case, each block has a "filename" caption
        to give some context.

* Introduction to Python
    * The REPL
    * Python compared to other Languages
    * Standard Data Types & Typing
* Wiki
    * List pages.
    * Load & display a page.
    * Save a page (create or update).
    * Replace WikiWords with links.
* Packaging


.. include:: ../common/introduction.rst


Code examples in these slides
-----------------------------

There are 3 ways, this course shows code examples:

* Examples from the Python REPL. These are marked with leading ``>>>``
  characters which is the default REPL promp.
* Blocks with filename header. These are meant to be in the filename seen in
  the header. The filename is always relative to the project folder.
* Blocks without filename header. These are "throwaway" examples which can be
  saved anywhere. Or run directly in the REPL.


Topics
------

.. ifslides::

   See the HTML version of this document

.. ifnotslides::

   Topics - Basic
   ~~~~~~~~~~~~~~

   ..                                         code example ┐
   ..                                 Documentation ┐      │
   ..     (*) esntl, (**) basic, (***) adv. ┐       │      │
   ..                                       │       │      │
   ..                                       │       │      │
   ..                                       │       │      │

   +-----------------------------------+-------+------+---------+
   | Description                       | Level | Docs | Example |
   +===================================+=======+======+=========+
   | data types -> Boolean, String     | ★☆☆   | ✓    |         |
   | (&literals), Bytes, Numbers,      |       |      |         |
   | Lists, Tuples, Dictionaries,      |       |      |         |
   | Sets, ``None``                    |       |      |         |
   +-----------------------------------+-------+------+---------+
   | Looping                           | ★☆☆   | ✓    | ✓       |
   +-----------------------------------+-------+------+---------+
   | Falsy values                      | ★☆☆   | ✓    | ø       |
   +-----------------------------------+-------+------+---------+
   | defining functions                | ★☆☆   | ✓    | ✓       |
   +-----------------------------------+-------+------+---------+
   | default arguments                 | ★☆☆   | ✓    | ✓       |
   +-----------------------------------+-------+------+---------+
   | keyword only arguments            | ★☆☆   | ✓    | ✓       |
   +-----------------------------------+-------+------+---------+
   | variadic functions                | ★☆☆   | ✓    | ✓       |
   +-----------------------------------+-------+------+---------+
   | defining classes                  | ★☆☆   | ✓    | ✓       |
   +-----------------------------------+-------+------+---------+
   | defining modules                  | ★☆☆   | ✓    | ✓       |
   +-----------------------------------+-------+------+---------+
   | defining packages                 | ★☆☆   | ✓    | ✓       |
   +-----------------------------------+-------+------+---------+
   | String formatting                 | ★☆☆   | ✓    | ✓       |
   +-----------------------------------+-------+------+---------+
   | Variable Unpacking                | ★★☆   | ✓    | ✓       |
   +-----------------------------------+-------+------+---------+
   | imports                           | ★☆☆   | ✓    | ✓       |
   +-----------------------------------+-------+------+---------+
   | catching exceptions               | ★☆☆   | ✓    | ✓       |
   +-----------------------------------+-------+------+---------+
   | raising exceptions                | ★☆☆   | ✓    | ✓       |
   +-----------------------------------+-------+------+---------+
   | Essential modules: os, sys, ...   | ★★☆   | ✓    | ø       |
   | (sys.stderr, out, in)             |       |      |         |
   +-----------------------------------+-------+------+---------+
   | Docstrings                        | ★☆☆   | ✓    | ✓       |
   +-----------------------------------+-------+------+---------+
   | Slicing                           | ★☆☆   | ✓    | ✓       |
   +-----------------------------------+-------+------+---------+


.. ifnotslides::

   Topics - Advanced
   ~~~~~~~~~~~~~~~~~

   ..                                         code example ┐
   ..                                 Documentation ┐      │
   ..     (*) esntl, (**) basic, (***) adv. ┐       │      │
   ..                                       │       │      │
   ..                                       │       │      │
   ..                                       │       │      │

   +-----------------------------------+-------+------+---------+
   | Description                       | Level | Docs | Example |
   +===================================+=======+======+=========+
   | ``in`` operator                   | ★☆☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | comprehensions (list, set & dict) | ★★☆   |      |         |
   | , generator expressions           |       |      |         |
   +-----------------------------------+-------+------+---------+
   | logging                           | ★☆☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | Variadic Functions                | ★★☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | Keyword-Only Arguments            | ★★☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | decorators                        | ★★★   |      |         |
   +-----------------------------------+-------+------+---------+
   | Context Managers ("with" stmt)    | ★☆☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | Class Customisation               | ★★☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | Descriptors                       | ★★★   |      |         |
   +-----------------------------------+-------+------+---------+
   | "magic" variables and attributes  | ★★☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | unit tests                        | ★★☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | lambda                            | ★★★   |      |         |
   +-----------------------------------+-------+------+---------+
   | raise from                        | ★★☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | PEP-420                           | ★☆☆   |      |         |
   +-----------------------------------+-------+------+---------+

.. ifnotslides::

   Topics - Removed from Old Course
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   ..                                         code example ┐
   ..                                 Documentation ┐      │
   ..     (*) esntl, (**) basic, (***) adv. ┐       │      │
   ..                                       │       │      │
   ..                                       │       │      │
   ..                                       │       │      │

   +-----------------------------------+-------+------+---------+
   | Description                       | Level | Docs | Example |
   +===================================+=======+======+=========+
   | DBAPI2                            | ★★☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | Packaging                         | ★★☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | everything is an object a         | ★★☆   |      |         |
   | (f.ex.: ``__doc__`` of function)  |       |      |         |
   +-----------------------------------+-------+------+---------+
   | ReST                              | ★☆☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | ABCs (Abstract Base Classes)      | ★★☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | PEPs                              | ★☆☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | Regular Expressions               | ★☆☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | sorting lists                     | ★☆☆   |      |         |
   +-----------------------------------+-------+------+---------+
   | iterators and generators          | ★★★   |      |         |
   +-----------------------------------+-------+------+---------+


Installation
============

* Linux
* Windows
* MacOS
* Go to https://www.python.org/downloads


Linux
-----

* Available by default on most Unix platforms.
* Packaged default may either be Python 2 (Debian, Red-Hat, Ubuntu < 16.04), or
  Python 3 (Arch, Ubuntu ≥ 16.04).
* Python 2 and 3 can both happily live on the same system without interfering
  with each other (f.ex. the ``python`` and ``python3`` packages on debian and
  derivates).

.. note::

    For this course we will use Python-3.7

    In order to successfully compile with all features for this course, you
    need the required libraries and system packages. For debian derivates these
    packages are:

    * ``build-essential``
    * ``libsqlite3-dev``

    Once the requirements are available run::

        ./configure --prefix=/opt/python3.7
        make
        sudo make install



Mac OS X
--------

* Download the ``pkg`` file and install.

.. tip::

    By default, Python 2.7 is installed. Installing from the official package
    will *not* overwrite the existing installation. They will live
    side-by-side.


Windows
-------

* Download the ``python-3.7.x.msi`` file and install.


About Python
============

* High-level overview of the language.
* Implementations
* Editors
* Language features


Birds-Eye View
--------------

* Runs on all major platforms.
* JIT Compiled (into bytecode).
* Large community.
* #3 on `TIOBE Index <http://www.tiobe.com/tiobe_index>`_
  (After Java at #1 and C on #2). Based on result of December 2018.
* Strict Syntax (indentation matters)!
* *Large* Standard Library ("Batteries Included").
* Global Interpreter Lock (the GIL)
* Slow


Implementations
---------------

* **CPython** (the default - *recommended*, ≠ cython).
* Jython (runs in Java VM).
* IronPython (runs in dotNET CLR).
* PyPy (faster).
* Stackless (microthreads).
* …

.. note::

   "CPython" is recommended because it implements everything in the official
   documentation. Other implementations may be incomplete, but may still be
   useful if there are special requirements.


Editors
-------

* PyCharm — https://www.jetbrains.com/pycharm/
* IDLE
* Komodo IDE — http://komodoide.com/
* Eclipse (with PyDev) — https://eclipse.org
* Netbeans (with Python plugin) — https://netbeans.org
* Any text-editor
    * vim
    * emacs
    * notepad++
    * sublime
    * …


Exercise - Hello World!
-----------------------

* Open PyCharm
* Create a new Project in PyCharm
* Right click the project and select "New Python File" and name it "hello.py"

.. code-block:: python
    :caption: **Filename:** hello.py

    print('Hello World!')

* Save this to a file called ``hello.py``
* Run the code example: Right click the file and select "Run 'hello'"


Duck Typing
-----------

    When I see a bird that walks like a duck and swims like a duck and quacks
    like a duck, I call that bird a duck.

    -- James Whitcomb Riley


.. rst-class:: smallest-slide

Typing Comparison
-----------------

+--------------+-----------+---------------------+
| Language     | Typing    | Coercion Strictness |
+==============+===========+=====================+
| Java         | Static    | Very strict         |
+--------------+           +                     +
| C#           |           |                     |
+--------------+           +---------------------+
| C++          |           | Fairly strict       |
+--------------+-----------+                     +
| Python       | Dynamic   |                     |
+--------------+           +                     +
| Ruby         |           |                     |
+--------------+           +---------------------+
| C            |           | Less strict         |
+--------------+           +---------------------+
| PHP          |           | Not strict          |
+--------------+           +                     +
| JavaScript   |           |                     |
+--------------+-----------+---------------------+


.. admonition:: Definition

    Coercion
        Implicit Type Conversion.


Python 2 vs Python 3
--------------------

* Don't use 3.0, 3.1 or 3.2 when migrating from Python 2 (unicode literals).
* Improved Unicode support. (bytes ≠ text, developer in full control).
* Iterators everywhere (:py:func:`map`, :py:func:`filter`, |ell|).
* No new features are added to Python 2 (f.ex.: :py:mod:`asyncio`, but
  backports exist).
* *BUT:* Legacy platforms may only support Python 2.


.. note::
    Python 3.3 reintroduced unicode strings (strings with a ``u`` prefix) which
    was removed in 3.0 and made porting very difficult.


Python 2 - End of Life: 2020
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Update NOW**


Strings & Bytes in Python 2 & 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

====================  ==========  ==========
 Literal               Py2 Type    Py3 Type
====================  ==========  ==========
 ``'Hello World'``     bytes       unicode
 ``u'Hello World'``    unicode     unicode
 ``b'Hello World'``    bytes       bytes
====================  ==========  ==========

.. warning::

    * *Always* prefix text with ``u`` in **Python 2**. *Unless* you know
      *exactly* that you want bytes!
    * *Never* use ``encode`` on bytes.
    * *Never* use ``decode`` on strings.

.. note::

    Technically, the type of ``''`` is ``str`` in Python2. However, in Python2,
    ``str`` and ``bytes`` are equivalent. Try running ``id(str)``,
    and ``id(bytes)`` in both Python2 and Python3.


The Python Shell (REPL)
-----------------------

* read-eval-print loop.
* Interactive shell.
* Extremely helpful tool to test out ideas, play with code before implementing
  it.

Simply run ``python3`` on the console to start it.

By convention, lines with ``>>>`` represent a REPL prompt.

.. code-block:: python

    >>> 1 + 1
    2

    >>> print("Hello World!")
    Hello World!


.. nextslide::
    :increment:

* The default REPL can be customized using a Python script and setting
  ``PYTHONSTARTUP`` o that file. For example: `exhuma/dotfiles/.pystartup
  <https://github.com/exhuma/dotfiles/blob/master/.pystartup>`_
* Alternative Python Shell: https://ipython.org/


Getting Help
------------

* On the web: http://docs.python.org
* Type ``help()`` in the REPL. This can be used on any object::

    >>> myvar = 1
    >>> help(myvar)  # This will open the help for "ints"

* Type ``pydoc`` in the shell.

  * Like man-pages for Python. Example: ``pydoc str``
  * Same as ``help()`` in the REPL.
  * Use ``pydoc -b`` (``python -m pydoc -b`` on Windows) to run a local
    web-server on a random port. This is useful if you have no internet
    connection.


Basics
======

This chapter covers the minimum you need to know to write simple Python
scripts.


.. rst-class:: smaller-slide

Language Syntax
---------------

* The variable type is implicit, but strong (dynamic typing)
* Variables are assigned with the ``=`` operator
* Line-comments start with a ``#`` character. Block comments don't exist.
  *Please don't use multiline strings as comments*.
* Lines do **not** need to end with a semicolon (``;``)
* Blocks are defined by indentation. The line starting a block ends with a
  colon (``:``).

.. literalinclude:: ../code/basics/app.py
   :caption: basics/app.py

.. note::

   * Once a variable is assigned a type, the type of that variable can no
     longer change. But the same name can later refer to a new object.
   * Common practice for indentation is to use 4 spaces. See :pep:`8` for more
     details on code-style.
   * The condition in the ``if`` statement is by convention not surrounded by
     parentheses (See :pep:`8`).


Simple Operations
-----------------

.. code-block:: python
    :caption: **Filename:** hello.py

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


Builtin Functions and Working with Files
----------------------------------------

* Python has a few `builtin functions
  <https://docs.python.org/3/library/functions.html>`_ which are very useful.
* :py:func:`open` is used to access files on the disk (for reading and
  writing).
* By default files are opened as "text".
* Using a ``for`` loop on file objects will iterate line-by-line.
* :py:mod:`pathlib` and :py:mod:`os.path` contain useful functions for working
  with files.

.. nextslide::
    :increment:

.. literalinclude:: ../code/working-with-files/app.py
   :caption: working-with-files/app.py


Looping
-------

Executing code on a collection of items (looping) can be done in several ways
in Python:

* A ``for ... in ...`` loop
* A ``while ...`` loop
* A comprehension expression (not covered in this course)
* Functional aproach using :py:func:`map`, :py:func:`filter` and
  :py:func:`functools.reduce` (not covered in this course).

.. nextslide::
    :increment:

.. literalinclude:: ../code/loops/app.py
   :caption: loops/app.py


Reading Files
-------------

Reading and writing files is done using the builtin function :py:func:`open`.
This function will return a "file-like object" which has low-level methods like
:py:meth:`~io.RawIOBase.read` and :py:meth:`~io.RawIOBase.write`.

.. tip::
    *Not neccessary for this course, but interesting*

    :py:mod:`io` contains all the low-level details.

.. nextslide::
    :increment:

.. literalinclude:: ../code/csv1/app.py
   :caption: csv1/app.py

.. nextslide::
    :increment:

File should *always* be closed. Even in the case of an error. Especially when
writing into files.

Python can ensure that this is done correctly by using the ``with`` statement:

.. code-block:: python

    with open('data.csv') as infile:
        do_something_with(infile)
        print(infile.closed)  # Will print "False"

    # Variables created in the "with" block will remain accessible, but cleanup
    # has taken place. In this case, the file will be closed now.
    print(infile.closed)  # Will print "True"



Organising Code
===============

This chapter covers how code can be structured into reusable pieces.

Functions
---------

* Functions are introduced using the ``def`` keyword
* A function *always* returns a value in Python. If no ``return`` statement is
  present, the return-value will be ``None``.

.. tip:: **Advanced:** Functions are objects!

    Functions are objects in Python (of type ``function``). As soon as a
    function is defined, that function can also be assigned to variables and
    passed into functions.  Useful for dynamic dispatch, callbacks,
    dependency-injection, …

.. nextslide::
   :increment:

.. literalinclude:: ../code/functions/app.py
   :caption: functions/app.py


Classes
-------

* Classes are introduced using the ``class`` keyword.
* Classes can inherit from multiple other classes.
* There are no interfaces.
* Classes offer advanced programming techniques not covered in this course
  (static-methods, class-methods, properties, descriptors)

.. tip:: **Advanced** Classes are objects

    Just like functions, classes are objects in Python too (of type ``type``).

.. nextslide::
   :increment:

.. rst-class:: smaller

.. literalinclude:: ../code/classes/app.py
   :caption: classes/app.py


Modules
-------

* Every Python file can be called a "module" and can be imported in other
  Python scripts.
* The code inside a module is executed on first import.

  * They *should* not "run" anything outside of classes & functions.
  * They *should* contain definitions only (functions, classes, variables, …)

.. tip:: **Advanced** Modules are objects

    Just like functions and classes, modules are objects in Python too (of type
    ``module``).


.. note::

   Any code that is written outside a function or class (at the top-level) of a
   module is executed when that module is *first* imported. This can be
   intentional if you want to ensure that a certain piece of code is excuted
   only once in an application. But it can also lead to unexpected
   side-effects and makes testing harder.

   Some advanced use-cases can make use of such code for "metaprogramming".

   As a rule of thumb: Don't put *business logic* on the top-level of a module.

.. nextslide::
   :increment:

.. literalinclude:: ../code/modules/util.py
   :caption: modules/util.py

.. nextslide::
    :increment:

.. literalinclude:: ../code/modules/app.py
   :caption: modules/app.py

.. nextslide::
    :increment:

* Importing will cause ``.pyc`` files to be created (inside the ``__pycache__``
  folder). They are auto-generated and don't belong into revision control.
* Imports are cached. The code inside a module is only interpreted on first
  import.
* Therefore, modules can be abused as global variable storage & singletons
  (with all the risks this implies).


Packages
--------

* Use packages to organise your project into sub-folders.
* A ``__init__.py`` file marks a folder as package (can be empty).
* The term "package" is ambiguous in Python. It can mean:

  * A "distributed" *package* you get from the Internet or write yourself (in
    other words: a "library").
  * Any folder with ``.py`` files and a ``__init__.py`` file.

A module ``util.py`` inside package ``subpackage1`` can be imported with::

    from subpackage1 import util  # Import only this name
    import subpackage1.util  # Import the whole package name


.. nextslide::
    :increment:

Example tree::

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

.. nextslide::
   :increment:

* Relative vs Absolute imports. See :pep:`328`::

      # Files:
      #
      #    mypackage
      #    ├── __init__.py    <--- Marks folder as package
      #    ├── localmodule.py
      #    └── app.py         <--- code below is in this file

      # Relative import (recommended, but only works in distributed packages)
      from .localmodule import func

      # Absolute import (recommended, but only works in distributed packages)
      from mypackage.localmodule import func

      # Ambiguous import (not recommended)
      from localmodule import func


Exercises
=========


.. rst-class:: smaller-slide

Organising Code
---------------

* In a file ``util.py`` write a function ``read_file`` which:

  * Takes the argument **filename**
  * Creates a new empty list (``output = []``)
  * Reads the file line-by line and appends each line to a list (making it a
    list of strings). Use ``output.append(...)``.
  * It should return the list after it is done reading the file.

* Write a second file ``app.py``:

  * This file should import ``util.py`` ...
  * ... and call ``read_file`` with an appropriate file-name and separator.
  * Loop over the return value of ``read_file`` and print the row.


Multiline CSV
-------------

For this exercise we will be using the file :download:`multiline.csv
<_static/multiline.csv>`.

*This is primarily a thought-experiment. Don't worry if you don't manage to
implement this*

* Try to design a function which loops over each *entry* (not *line*) in
  ``multiline.csv``.
* What challenges can you identify?
* How would you approach this?

.. tip::

    IETF Standard for ``text/csv``: `RFC-4180
    <https://tools.ietf.org/html/rfc4180>`_


Writing Documentation
=====================

For the following objects, Python considers the first string inside that object
as documentation (this is called a "docstring"):

* Functions
* Classes
* Modules
* Packages (inside the ``__init__.py`` file)

These strings will be extracted by the :py:func:`help` function and can also be
extracted by external tools like pydoc_, epydoc_ or sphinx_.

.. _pydoc: https://docs.python.org/3/library/pydoc.html
.. _epydoc: http://epydoc.sourceforge.net/
.. _sphinx: http://www.sphinx-doc.org/en/master/


Functions
---------

.. code-block:: python

    def myfunction():
        """
        This is the documentation of the function
        """


Classes
-------

.. code-block:: python

    class MyClass:
        """
        This is the documentation of the class
        """


Modules
-------

.. code-block:: python
    :caption: filename: hello.py

    """
    This is the documentation of the function
    """

    def first_function_in_module():
        "..."
        ...


Packages
--------

Packages use the module docstring of ``__init__.py``.


Module Data
-----------

Top-level variables have no predefined standard for documentation. ``Sphinx``
will extract comments starting with ``#:`` as documetnation:

.. code-block:: python
    :caption: filename: example.py

    """
    This is the module docstring
    """
    # This is a simple comment, ignored by Sphinx

    #: This is the documentation for the variable below
    MY_VARIABLE = 1


Basic Data Types - Scalars
==========================

See https://docs.python.org/3/library/stdtypes.html


None (NULL)
-----------

* Default return value of functions
* Is seen as "false" in a boolean context
* Immutable
* Special instance of the :py:class:`NoneType` class.
* Singleton.


.. code-block:: python

   myvariable = None


.. rst-class:: smaller-slide

Strings
-------

* Instances of class :py:class:`str`.
* Delimited by one of ``'``, ``"``, ``'''``, ``"""``
* Unicode objects, sequence of unicode code-points (in Python3).
* Many useful methods

  * :py:meth:`str.split`, :py:meth:`str.partition`, :py:meth:`str.strip`
  * :py:meth:`str.startswith`
  * :py:meth:`str.encode`
  * :py:meth:`str.find`
  * :py:meth:`str.isnumeric`
  * …

.. code-block:: python

   mystring = 'Hello World!'


.. rst-class:: smaller-slide
.. nextslide::
   :increment:

String Literals

* Simple Quotes (``'`` and ``"``)
* Triple Quotes / Multiline Strings (``'''`` and ``"""``)
* String-Liteal Prefixes

  * ``r`` raw-string: All backslash-escapes are ignored. Useful for regular
    expressions.
  * ``f`` format-string: Allows embedding of variables
  * ``u`` unicode (Backwards compatibility for Python 2)

.. code-block:: python

   mytext = u"Hello World!"
   unescaped = r"This does *not* \n contain a new-line!"
   formatted = f'The variable "mytext" contains the value {mytext}'


.. rst-class:: smaller-slide
.. nextslide::
   :increment:

* Supports different string-formatting styles:

  * "printf"-style formatting: ``"Hello %20s %s" % (a, b)``
  * Formatting "mini-language": ``"Hello {} {}".format(a, b)``
  * f-Strings: ``f"Hello {a} {b}"``

See `RealPython <https://realpython.com/python-string-formatting/>`_,
`printf-style formatting
<https://docs.python.org/3/library/stdtypes.html#old-string-formatting>`_ and
`format-language <https://docs.python.org/3/library/string.html>`_ for more
information.


More on this later …


.. rst-class:: small-slide

Numbers
-------

* Builtin types: :py:class:`int` and :py:class:`float`
* No difference between "long" and "short" integers (handled internally by
  Python). There is also no "double precision" type.
* Support for precise decimal operations (:py:mod:`fractions`,
  :py:mod:`decimal`).
* Noteworthy modules: :py:mod:`statistics`, :py:mod:`math` and :py:mod:`cmath`.

.. code-block:: python

   myint = 1               # type: int
   bin_notation = 0b10101  # type: int, base: 2, value (base 10): 21
   hex_notation = 0xc0ffee # type: int, base: 16, value (base 10): 12648430
   octal_notation = 0o10   # type: int, base: 8, value (base 10): 8

   myfloat = 3.5           # type: float
   myfloat2 = .3           # type: float
   sci_notation = 1.3E5    # type: float, value: 130000.0


Boolean
-------

* Two reserved words: ``True`` and ``False``. They are object instances,
  subclasses of ``int``.

.. code-block:: python

   my_boolean_a = True
   my_boolean_b = False


Testing for Truth & Falsy Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Python many value are considered as ``False`` without converting to ``bool``
when they are used in a place where a boolean value is expected. The most
common places are ``if`` and ``while`` blocks:

.. code-block:: python

    if <here>:
        pass

    while <here>:
        pass

.. nextslide::
    :increment:

In such locations, the following values are considered as ``False``:

* ``None``
* The numbers ``0``, ``0.0``, ``Decimal('0.0')``
* The empty string ``""``
* Empty structures ``[]``, ``{}``, ``set()``
* Any custom object overriding the special ``__bool__`` method.


Implicit & Explicit Type Conversions
------------------------------------

As we have seen, Python has dynamic typing but fairly strict coercion rules. In
English: the same variable can change it's type over time. But two values of
different types cannot be easily combined.

In Python some types are compatible for some operations (``int`` and ``float``)
while others are not (``str`` and ``int`` for addition).


Explicit Conversions
~~~~~~~~~~~~~~~~~~~~

When a user enters numeric values from the keyboard (or if read from a CSV
file), they are seen as strings and must be converted to numeric values:

.. code-block:: python

    value_str = input('Please enter a number:')
    value_int = int(value_str)
    print(value_int + 10)

Probably the most common conversions you will encounter are: :py:class:`int`,
:py:class:`str`, :py:class:`float`, :py:class:`bytes`.


Implicit Conversions
~~~~~~~~~~~~~~~~~~~~

Some values are compatible for some operations. The resulting type depends on
the operation:

.. code-block:: python

    >>> type(10 * 3.14)
    <class 'float'>
    >>> type('a' * 3)
    <class 'str'>
    >>> type(['a'] * 3)
    <class 'list'>


Exercise - Comparison with Other Languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to http://repl.it/ and try to execute ``20 + "22"`` in Python, PHP and
JavaScript.

* What are the results?
* What does this tell you?
* What are the advantages & disadvantages of strict/lenient coercion?

The Standard Library
====================

Python comes with "batteries included".

The `standard library <https://docs.python.org/3/library/>`_ of Python comes
with *many* useful features. This makes it possible to write many useful
applications without third-party (external) libraries.

* Standard Library modules are also imported using the ``import`` statement.
* Standard Library modules take precedence in imports (Use relative imports on
  name-conflicts). See :pep:`328`.


Essential Modules
-----------------

* :py:mod:`os`: Operating System details.
* :py:mod:`os.path`: Helper functions to deal with filenames.
* :py:mod:`logging`: Fully featured logging system.
* :py:mod:`json` for parsing and creating JSON documents.
* :py:mod:`datetime` & :py:mod:`time` for date/time processing. **Important**:
  Timezone data is kept *outside* of the stdlib in the module :py:mod:`pytz`.
  This allows faster updates than the normal release cycle of Python.

Notable Modules
---------------

* :py:mod:`argparse` for CLI argument handling (successor of both
* :py:mod:`optparse` and :py:mod:`getopt`).
* :py:mod:`gettext` for decoupling text translations from source-code using the
  well-known GNU gettext system.
* :py:mod:`pathlib` & :py:mod:`os.path` for handling file-system paths.
* :py:mod:`tempfile` for creating temporary files securely.
* :py:mod:`sqlite3` for structured persistent data storage without a DB server.
* :py:mod:`configparser` for working with ``.ini`` files.
* :py:mod:`hashlib` for calculating common hashes (``md5``, ``sha1``, …)


Example - The ``csv`` module
----------------------------

The :py:mod:`csv` module makes it easy to read delimited data. It also deals
with:

* quoted values
* multiline values
* escaped characters

Let's use this for our example:

.. literalinclude:: ../code/csv2/app.py
   :caption: csv2/app.py


.. rst-class:: small-slide

Exercise - Simple Data Types & StdLib
-------------------------------------

Write a new function *read_data* that takes a filename as argument. The file
:download:`csv3.csv <_static/data/csv3.csv>` can be used as example. The
function should do the following:

* Open the file with the given filename
* Initialise a new variable named ``output`` as empty list.
* Create a CSV reader with the opened file object
* Loop through each line and do the following:

  * Convert each numerical column into an appropriate type (f.ex.: use
    :py:class:`decimal.Decimal` for monetary values).
  * Split the 7 :sup:`th` column (index 6) into a list of strings.
  * **(optional)** Add a new column at the end which contains the ``MD5``
    hex-digest of the whole line (see :py:func:`hashlib.md5`).

    * MD5 sums can only be calculated on bytes (not strings)

  * Append the new columns to the ``output`` list

* After the loop, return the list ``output``


Basics #2
=========

This chapter covers a few topics beyond the fundamental basics, but which
should nonetheless be understood when developing Python applications.


Exceptions
----------

* Exceptions are Python's error-handling mechanism.
* They can be triggered internally by Python, or manually by self-written code.
* They can be caught/handled using a ``try/except`` block.
* Unhandled exceptions will crash the application.

An example exception:

.. code-block:: python

    >>> from example_exception import foo
    >>> foo()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/path/example_exception.py", line 3, in foo
        return a['z']
    KeyError: 'z'


.. note::

    From bottom to top:

    **KeyError**
        The kind of the exception which was thrown.

    ``return a['z']``
        The line which caused the error.

    **File "..."**
        The filename that caused the error.

    **line 3**
        The line in the file.

    **in foo**
        The function-name in which the error was thrown.

    Moving up the "stack", the lines have the same format. The further you move
    "up", the closer you get to the entry-point of the application.


.. nextslide::
   :increment:

* By default, Python will raise an exception of one of the `builtin types
  <https://docs.python.org/3/library/exceptions.html#exception-hierarchy>`_.
* You can create your own exceptions by subclassing.
* Raising (triggering/throwing) exceptions is done using the ``raise``
  keyword::

      class MyException(Exception):
         pass

      if user_input > 4096:
         raise ValueError('user_input must be smaller than 4096')
      raise MyException('Hello World!')



.. nextslide::
   :increment:

* If not handled, exceptions will crash the application and print a traceback
  on ``stderr``.
* They can be handled using a ``try/except`` block:

.. code-block:: python


   from example_exception import foo

   try:
      foo()
   except KeyError as the_exception:
      # Something bad happened :(
      print(the_exception)

.. rst-class:: smaller
.. tip::

   Always log the traceback of an exception using either
   ``logging.debug(the_exception, exc_info=True)`` or
   ``logging.exception('Simple description')``

Exercise - Catching Exceptions
------------------------------

Modify the previous exercise so that no type conversion make the application
crash. Instead, log an error message using the :py:mod:`logging` module:

.. code-block:: python

    import logging
    logging.error('Something went wrong')


Edit the CSV file manually to trigger errors.


Side-Note: logging
------------------

* Use :py:func:`print` **only** if you display text to a user in a CLI
  application or if you write to a file.
* **For all other cases use the logging module**
* When logging inside an exception use the ``exc_info=True`` argument. This
  cases the traceback to be logged and can be invaluable when debugging::

    logging.debug('The error message', exc_info=True)



Variable Unpacking
------------------

Python can assign more than one value in one statement:


.. code-block:: python

   # Assign 13 to variable_a, and 'Hello' to variable_b
   variable_a, variable_b = 13, 'Hello'

This work in every place where values are assigned:

.. code-block:: python
   :emphasize-lines: 8

   mylist = [
      [1, 2],
      [11, 22]
   ]

   # Each item in the list is another list of two elements each.
   # They can be "unpacked" directly in the loop.
   for variable_a, variable_b in mylist:
      print(variable_a, variable_b)


Enumerating Loops (access the current loop index)
-------------------------------------------------

Keeping a reference to the current iteration number is easy by using the
:py:func:`enumerate` function.

In combination with *variable unpacking* loops can be written as:

.. code-block:: python

   for i, item in enumerate(mylist):
      print('Item at index %d is: %r' % (i, item))


.. rst-class:: smaller

.. tip::

   Python makes it relatively easy to avoid accessing items by index (see for
   example :py:func:`zip`). Enumerating lists like this only needed in rare
   cases (calculating progress, logging the current line during text-file
   processing, …).



Basic Data Types #2 - Collections
=================================

Also on https://docs.python.org/3/library/stdtypes.html

So far we've only covered "scalar" values. This chapter covers the most
commonly used "collection" types in Python.


.. rst-class:: smaller-slide

Lists
-----

* Used for collections with variable length and which have a specific ordering.
* Surrounded by square brackets::

   mylist = [1, 2, 3, 'hello', 5, 6, True]

* Very similar to arrays in other languages. Real arrays are in the
  :py:mod:`array` module.
* Heterogenuous
* Indexable from both left (``mylist[3]``) and right (``mylist[-3]``).
* Slicing: ``mylist[3:7]``
* Mutable::

    mylist[2] = new_value
    mylist.append(10)


.. note::

   When accessing a slice, the first index is *inclusive* and the second index
   is *exclusive*. For example::

      >>> mylist = ['a', 'b', 'c', 'd', 'e']
      >>> mylist[1:3]
      ['b', 'c']


.. rst-class:: smaller-slide

Bytes
-----

* Builtin type: :py:class:`bytes`.
* byte-literals look just like strings, but with a ``b`` prefix::

   b"Hello World"

* Immutable (for byte-operations see :py:class:`bytearray`).
* Almost identical API to strings. The key differences are:

  * Bytes almost always come "from the outside world" (hard-disk, network, …)
  * Strings are almost always meant to be read by a human (bytes not so much).
  * Bytes can only be "decoded" into strings
  * Strings can only be "encoded" into bytes


.. rst-class:: smaller-slide
.. nextslide::
   :increment:

* Bytes are (generally) used to talk to machines:

  * Write data to files
  * Send data over a network socket

* String are used to be displayed to a human user:

  * Text on a button label
  * CLI output, HTML content
  * …

.. admonition:: Rule of Thumb

   For *text*, as long as the value remains held by variables, use normal
   string-literals (unicode objects). As soon as the value crosses the
   memory/io boundary (network, disk) it needs to be encoded to bytes or
   decoded to string.


Tuples
------

* Used for collections of fixed length where each item has a specific meaning.
* Surrounded by parentheses::

   mytuple = (1, 2, 3, 4, 5, 6, 7)

* Like lists, but immutable.
* Hashable (if contents are hashable)
* Recommended alternative: :py:func:`collections.namedtuple`


.. ifslides::

    **Note**:

    Tuple of one element: ``(1,)``

.. note::

    In python, using ``(1)`` is the same as simply writing ``1``. The following
    two statements are equivalent::

        >>> x = (1)
        >>> x = 1

    Parens can be used to group multiple statements, and to split long lines.

    But tuples use parens to write tuples too. So writing a tuple of one
    element introduces an ambiguity in syntax: When writing ``(1)``, do you
    mean the tuple with one element, or do you mean the integer value ``1``?

    In order to remove this ambiguity, a 1-element tuple must be written with a
    trailing comma: ``(1, )``

    Additionally, in the same way that ``1`` ≡ ``(1)``, there is also: ``(1,)``
    ≡ ``1,`` (as long as it is syntactically correct)!.

    As such, the following lines are also equivalent (similar to the first
    paragraph)::

        >>> x = 1,
        >>> x = (1, )

    This can lead to subtle bugs when not careful.


.. rst-class:: smaller-slide

Dictionaries
------------

* Used to map from one value to another.
* Surrounded by curly braces, using colons to separate key from value::

   mydict = {"a": 1, "b": 2}

* Key/Value stores (Like HashTables in *Java* or *C#*)
* Looping over key/values is easy using::

   for key, value in mydict.items():
      ...

* Starting from Python 3.7, ordering of keys is retained.


.. rst-class:: small
.. warning::

   **Do not rely on ordering behaviour if your application runs in an older
   Python environment!**


.. note::

   The retention of dictionary key order was an implementation detail prior to
   Python 3.7. Starting from Python 3.7, this is now baked in the language
   specification and needs to be followed by implementations.


Sets
----

* Used for collections of variable size with unique values and with no
  particular ordering.
* Surrounded by curly braces (looks like dictionaries but without the colons)::

   myset = {1, 2, 3, 4, 5}

* :py:class:`set` can be used to convert any iterable to a set (dropping
  duplicates).
* Useful methods like :py:meth:`set.union`, :py:meth:`set.intersection`, …
* If a value is already in the set, adding it again will have no effect.
* Values must be hashable


Exercises
=========


Exercise - Collection Types
---------------------------

For this exercise we will be using the file :download:`collections.csv
<_static/collections.csv>`.

In this file, each entry is split into two lines (Line 1 and line 2 are the
headers).

Loop over the entries, joining each couple together into one record (Tip: look
at :py:meth:`list.extend`, and remember :py:func:`enumerate`). Print the
entries nicely formatted to standard output.

At the end of the script, print out each hobby only once sorted alphabetically
(See :py:func:`sorted`).

.. rst-class:: smaller
**Advanced:** Use the :py:mod:`itertools` module (f.ex.
:py:func:`~itertools.islice` and :py:func:`~itertools.tee`) to rewrite this in
a functional style. What are the advantages and disadvantages of this method?


.. rst-class:: small-slide

Exercise - Data Lookup
----------------------

Sample Data Files: :download:`opendata.lu-sample-2019-03-09.zip
<_static/data/opendata.lu-sample-2019-03-09.zip>`.

* The file ``caclr/TR.DICACOLO.RUCP`` contains location names in position
  120-160 and ZIP codes in position 200-204. The file uses the ``cp1252``
  encoding
* The file ``rnrpp-code-postal.csv`` contains the number of inhabitants per ZIP
  code.

Write a program which:

* Reads the data from both files
* For each ZIP-code per location, look up the number of inhabitants and
  calculate the sum
* Sort the list by descending number of inhabitants
* Print out the location name and number of inhabitants of the top 10 items
  using 30 characters for the location, right aligned.

  Sample output is on the following slide

.. nextslide::
    :increment:

.. code-block:: text

                     Luxembourg 120547
               Esch-sur-Alzette 35635
                      Dudelange 21087
                    Differdange 16348
                    Schifflange 11184
                       Strassen 10503
                        Pétange 9506
                      Bertrange 9491
                    Bettembourg 8995
                        Belvaux 8129



.. rst-class:: smaller-slide

Exercise - Bytes & Collection Types 2
-------------------------------------

Using the files :download:`data_latin1.csv <_static/data/data_latin1.csv>` and
:download:`data_utf8.csv <_static/data/data_utf8.csv>`, write a function which
diffs the two files.

Both lists represent the same data from two different sources. It can be
assumed that each line is unique in each file.

The program should print:

* Which lines are missing in the first file
* Which lines are missing in the second file

Tips:

* Ensure the encoding is correct
* A combination of :py:class:`tuple` and :py:class:`set` can make this very
  easy


Exercise - Pwned Passwords
--------------------------

**Goal:** Find out if a password was ever leaked by an attack without sending
the password to a remote API.

.. rst-class:: smaller

API docs: https://haveibeenpwned.com/API/v2#PwnedPasswords

Challenges/Tips:

.. rst-class:: smaller

* Find out how to get a SHA-1 hash from a string
* Use the module :mod:`getpass` to prompt the user for a password
* Try with incorrect URLs and add appropriat error-handling

.. tip::

    In production we would use the third-party module ``requests``. The example
    below shows how to do this with the standard library so we don't have to
    deal with external modules just yet.

.. nextslide::
    :increment:

Code to fetch data from a URL:

.. code-block:: python

    from urllib.request import Request, urlopen

    def http_get(url):
        '''
        Fetch the contents of *url* using a HTTP GET call
        '''
        # Headers must be set, otherwirse we get a "403 Forbidden" error
        headers = {'User-Agent': 'pythontraining/pwdchecker'}
        request = Request(url, headers=headers, method='GET')
        response = urlopen(request)
        data = response.read()
        return data


Functions Revisited
===================

Until now we have only seen very simple function definitions. This small
chapter discusses a few more advanced techniques which are very useful in most
applications.


Default Arguments
-----------------

* Functions can have default values for arguments.
* When the function is called, and those arguments are not specified, the
  default value is used:

.. code-block:: python

    def hello(name="John"):
        print("Hello %s" % name

    hello("Jane")  # Prints "Hello Jane"
    hello()  # Prints "Hello John"

.. nextslide::
    :increment:

Normal arguments can be combined with default arguments, but the default
arguments must come *after* the normal ("positional") arguments:

.. code-block:: python

    def say(name, question, prefix="Hello"):
        print("%s %s, %s" % (prefix, name, question))

.. nextslide::
    :increment:

.. warning::
    Never use mutable objects (lists, sets, dictionaries, custom objects, ...)
    as default values on arguments.

    The value (and instance) will be bound to the function when the function
    definition is *parsed*.

    **Don't do this:**

    .. code-block:: python

        def myfunction(names=[]):
            ...

    Do this instead:

    .. code-block:: python

        def myfunction(names=None):
            names = names or []


Passing values into functions
-----------------------------

Providing arguments to functions can be done in two ways: *positional* and *by
keywords*. Consider this function signature:

.. code-block:: python

    def hello(name, prefix="Hello"): ...

This can be called in the following ways:

.. code-block:: python

    hello("John")  # by position, using defaults
    hello(name="John") # by keyword, using defaults
    hello("John", "Goodbye")  # by position
    hello(name="John", prefix="Goodbye")  # by keyword
    hello(prefix="Goodbye", name="John")  # by keyword (changing order)


Classes Revisited
=================

Constructor vs Initialisor
--------------------------

* The constructor ``__new__`` create a new instance of a class and returns is
* The initialisor ``__init__`` gets an empty instance of the class and can
  modify it.
* **Always prefer to use __init__ over __new__**.
* Defining an initialisor or constructor is optional.


.. note::

    The constructor ``__new__`` allows for some powerful (and dangerous)
    techniques like returning an instance *of another type*. This can be very
    useful is implemented correctly. But can lead to very confusing bugs if
    not implemented correctly. To avoid this risk, always use ``__init__``
    unless you *really* know what you are doing and if it is impossible to do
    with ``__init__``.


Instance Methods
----------------

When simply defining a method in a function inside a function it becomes an
instance method. Contrary to many other languages, **an instance method
received a reference to the instance as first argument**.

This argument is - by convention - called ``self`` in Python. It serves the
same purpose as ``this`` in languages like Java.

.. code-block:: python

    class MyClass:

        def my_method(self):
            print(self)  # Prints the string representaion of the current instance

        def my_broken_method():
            # This method will never be callable. Python automatically passes
            # in the instance reference. But because this method does not take
            # any arguments, this will fail.
            pass


Class Methods
-------------

Class methods are prefixed with ``@classmethod``

Class methods are something fairly unique to Python. They also get a default
argument. But compared to instance methods, this argument will have a reference
to the *class*! This is particularly useful when subclassing.

By convention this argument is called ``cls``.


.. code-block:: python

    class MyClass:

        @classmethod
        def my_method(cls):
            print(cls)  # Prints the string representaion of the current class


Static Methods
--------------

Static methods are prefixed with ``@staticmethod``

Static methods are unaware of their instance or class. They do not receive an
additional argument by default.

They are useful to organise code.


.. code-block:: python

    class MyClass:

        @staticmethod
        def my_method():
            return 1

    print(MyClass.my_method())


Abstract Methods
----------------

The standard module :py:mod:`abc` (abstract base classes) can be used to define
abstract classes.

They differ in a fundamental way from abstract classes in other (static)
languages: **They are not checked at compile-time**. They are checked at
runtime.

.. code-block:: python

    from abc import ABCMeta, abstractmethod

    class MyAbstractClass(metaclass=ABCMeta):

        @abstractmethod
        def mymethod(self):
            raise NotImplementedError('Not yet implemented')


Classes – Basic Example
-----------------------

.. code-block:: python

    class MyClass(AParentClass, AMixinClass):

        CLASS_VARIABLE = 'hello world'

        def __init__(self, a, b):
            super()
            self.a = a
            self.b = b

        @staticmethod
        def mystaticmethod(arg1, arg2):
            print(arg1, arg2)

        @classmethod
        def myclassmethod(cls, arg1, arg2):
            print(cls, arg1, arg2)

        def myinstancemethod(self, arg1, arg2):
            print(self, arg1, arg2)


.. note::

    * ``__init__`` is the class initialisor. For a real constructor, look at
      ``__new__``. But that should only be used if you *really* need it!
    * Static methods are methods bound to the namespace of the class. They work
      just like regular functions except that they live in a different
      namespace.
    * Class methods methods receive the instance of the *class* they were
      called on as first argument. This can be useful in subclassing scenarios.
    * Instance methods *exclicitly* take a reference to the instance as first
      argument. By *convention* this is called ``self`` but can take any other
      name. This is equivalent the the ``this`` keyword existing in other
      languages.




Python - Advanced
=================

Keyword Only Arguments
----------------------

It is possible to *force* keywords being passed by keyword by adding a single
"*" in the arguments:

.. code-block:: python

    def hello(name, *, prefix="Hello"): ...


    hello("John", prefix="Goodbye")  # OK
    hello("John", "Goodbye")  # Error

It is also possible to add a star in the beginning, forcing all arguments to be
passed as keyword arguments:

.. code-block:: python

    def hello(*, name, prefix="Hello"): ...


.. rst-class:: smaller-slide

Variadic Functions
------------------

"Variadic Functions" are functions that can take any number of arguments.
Python splits these in two categories: *positional* and *keyword*.

* For positional arguments, the argument name is prefixed with a ``*``, and
  keyword arguments are prefixed with ``**``. The names "args" and "kwargs" are
  commonly used.

.. code-block:: python

    from pprint import pprint

    def variadic_args(*args, **kwargs):
        pprint(locals())


.. tip::

    ``args`` and ``kwargs`` are only conventional names. Sometimes (but rarely)
    it may be useful to use other names.


.. nextslide::
    :increment:

Inside a variadic function, the values of ``*args`` will be available in a
*tuple* named ``args``, and the keyword arguments will be available in a
*dictionary* called ``kwargs`` (unless you used different names).

This can be combined with other arguments:

.. code-block:: python

    def foo(first, second, *more, prefix=None, suffix=None, **config):
        ...


.. slide:: Exercise

    Write a function ``msum`` that takes any number of arguments, *and* any
    number of keyword arguments. It should return the sum of the arguments
    (positional and keyword). Use the *values* of the keyword arguments to
    calculate the sum::

        assert(msum(10) == 10)
        assert(msum(a=10) == 10)
        assert(msum() == 0)
        assert(msum(10, 30, a=11, b=12) == 63)



Old Course
==========

Pages after this one are only here for reference. They should be removed after
the course is rewritten


Functions as Objects
--------------------

Because functions are objects, they can be assigned to variables. For example
as values in a dictionary:

.. code-block:: python
    :class: smallcode

    def first_case():
        print("Hello 1")

    def another_function():
        print("Hello 2")

    def default():
        print("unknown case")

    cases = {
        1: first_case,
        2: another_function,
    }

    user_selection = int(input('Type a number: '))

    function = cases.get(user_selection, default)
    function()

.. note::

    Python has no ``case`` or ``switch`` statement. Using functions as values
    in dictionaries, lets you have a very similar code structure. As a
    side-effect, this will give you functions for each switched case, which
    makes unit-testing easier.



Documenting Code
----------------

* The first ``string`` inside a module/class/function are their so called
  "docstrings".
* No standard formatting.
* Sphinx (http://www.sphinx-doc.org)
* Accessible via the special variable ``__doc__``. This is also what ``help()``
  uses.

.. sidebar:: Takeaways

    * Everything is an object. Functions too!

.. code-block:: python

    >>> def noop():
    ...     '''
    ...     Does nothing
    ...     '''
    ...     pass

    >>> print(noop.__doc__)


Imports
-------

* Partial imports are possible: ``from foo import bar``
* Aliasing imports: ``from foo import bar as qux``
* *Never* write ``from foo import *`` (Why?).
* Can be wrapped in a ``try … except`` block. This allows for graceful
  degradation.
* They do not have to be at the beginning of the file.
* They are cached. File lookup, and actual loading only happens the first
  time.

.. warning:: Import Side-Effects

    Modules (``.py``) files should never execute active code on it's root! This
    code will be executed on import and is very hard to test with unit-tests!


The "``in``" Operator
---------------------

.. sidebar:: Warning

    The iterated variable is bound in the *same* scope as the ``for``
    loop resides. The loop effectively shadows this value!

* Loops
* Tests for membership

**Examples:**

.. code-block:: python

    >>> mylist = [1, 2, 3]
    >>> for element in mylist:
    >>>     print(element)

    >>> 2 in [1, 2, 3]

    >>> 'foo' in {'foo': 10, 'bar': 20}

    >>> 'foo' in {'foo', 'bar'}


``for … in … else``
-------------------

.. sidebar:: Explore

    * ``$ pydoc for``


* For loops have an optional ``else`` clause: ``for … in … else …``.
* The ``else`` block is executed when the ``for`` block reaches it's end
  *normally* (no ``break``).

**Example**

.. code-block:: python

    with open('names.txt') as file_handle:
        names = file_handle.read().splitlines()

    for name in names:
        if name == 'foo':
            print('foo was found!')
            break
    else:
        print('foo was not found in the file!')


``for`` loop gotcha
-------------------

.. code-block:: python

    >>> element = 'Whoops'
    >>> for element in [1, 2, 3]:
    >>>     print(element)
    >>>
    >>> print(element)  # Caution! Keep this in mind!


The "``with``" Statement
------------------------

* Used with a so called "Context Manager".
* Used for code which needs an "entry" and guaranteed "exit" step (a open file,
  a DB connection, …).
* The ``with`` block does **not** create a new variable scope. Variables
  created in that block are accessible outside!
* Ensures that finalisation step is taken. Even on unexpected exit.
* Context managers can be created manuall by implementing the magic
  ``__enter__`` and ``__exit__`` methods in a class, or
  :py:func:`contextlib.contextmanager`.



Third Party Modules & virtualenv
--------------------------------

* Official Index (The "Cheese Shop"): http://pypi.python.org
* Third Party modules can be installed using ``pip``.
* Virtual Environments isolate packages from the system.
* Virtual Environments can be created using ``pyvenv`` (as of Python 3.4) or
  ``virtualenv`` .

.. attention::
    Installing compiled extensions (f.ex. C/C++) requires the appropriate
    compiler (and headers) on the system!

.. nextslide::
    :increment:

**Installing our requirement**

.. code-block:: bash

    $ /opt/python3.7/bin/pyvenv env
    $ ./env/bin/pip install flask


**Alternatives**

.. code-block:: bash

    # Creating an environment on Windows
    > python3 -m venv env

.. code-block:: bash

    $ source env/bin/activate
    (env)$ pip install flask


Packaging our application
-------------------------

A minimal setup script:

.. code-block:: python
    :caption: **Filename:** setup.py
    :name: basic_setup_script

    from setuptools import setup, find_packages

    setup(name='wiki',
          packages=find_packages())


Linking the package for development:

.. code-block:: bash

    $ ./env/bin/pip install -e .

.. sidebar:: PyCharm

    * Tools > Run setup.py task > develop


String Formatting
-----------------


.. sidebar:: New in Python 3.6
    :class: overlapping

    * f-strings:  ``f'Hello {varname}!'`` (See :pep:`0498`)

.. code-block:: python

    >>> fname = 'John'
    >>> lname = 'Doe'
    >>>
    >>> # Mini-Language
    >>> print('|{fname:<20}|{lname:^20}|'.format(
    ...     fname=fname, lname=lname))
    >>>
    >>> # C-Style
    >>> print('|%-20s|%20s|' % (fname, lname))


============================== ===============================
 C-Style                         Mini-Language
============================== ===============================
 |smile| faster                  |disappointed| slower
 |smile| less verbose            |disappointed| more verbose
 |disappointed| less readable    |smile| more readable
 |disappointed| less powerful    |smile| more powerful
============================== ===============================


.. nextslide::
    :increment:


**Python 3.6+**

.. code-block:: python

    name = 'John'
    age = 12
    print(f'Hello, my name is {name} and I am {age} years old!')


"f-strings" have access to all variables from the current scope and they can
easily be accessed using the template-string notation. It also allows for the
same formatting options as ``str.format``.




Packaging — Revisited
----------------------

.. code-block:: python
    :caption: **Filename:** setup.py
    :name: extended_setup_script

    from setuptools import setup, find_packages
    setup(
        name='wiki',
        description="Replacement for Wikipedia",
        url="http://www.newp-project.com",
        license="BSD",
        author="Michel Albert",
        author_email="michel@albert.lu",
        version='0.6',
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            'Flask',
        ],
    )

.. nextslide::
    :increment:


.. code-block:: text
    :caption: **Filename:** MANIFEST.in

    recursive-include wiki/templates *.html


Creating distributions
----------------------

.. code-block:: bash
    :caption: Creating a source distribution

    $ python setup.py sdist


.. code-block:: bash
    :caption: Creating a binary distribution

    $ python setup.py bdist_wheel


.. code-block:: bash
    :caption: Uploading/Publishing

    $ twine upload dist/*

See: https://packaging.python.org

.. sidebar:: Source Code
    :class: overlapping

    `source code (step 6) <_static/wiki-0.6.tar.gz>`_ (`zip <_static/wiki-0.6.zip>`_)


SQLite and DBAPI 2
------------------

SQLite3 is included in the Python standard library (since Python 2.5). It is
compliant to DBAPI2 (:pep:`249`).

DBAPI compliant code looks like this:

.. code-block:: python

    connection = driver.connect(driver_parameters)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mytable")
    for row in cursor:
        print(row)
    connection.close()

.. note::

    If you compile Python manually, the sqlite development headers
    (``libsqlite3-dev`` on debian and derivates) must be available. If not, the
    extension will not be included!


A new Storage class
-------------------

.. code-block:: python
    :caption: **Filename:** wiki/storage/sqlite.py
    :name: sqlitestorage2

    import sqlite3

    from wiki.model import WikiPage


    class SQLiteStorage:

        def __init__(self, dsn):
            self.connection = sqlite3.connect(dsn)

.. nextslide::
    :increment:

.. code-block:: python
    :caption: **Filename:** wiki/storage/sqlite.py
    :name: sqlitestorage3

        def init(self):
            cursor = self.connection.cursor()
            cursor.execute(
                '''
                CREATE TABLE wikipage (
                    title TEXT NOT NULL PRIMARY KEY,
                    content TEXT);
                ''')

            cursor.close()
            self.connection.commit()

        def close(self):
            self.connection.close()

.. nextslide::
    :increment:

.. code-block:: python
    :caption: **Filename:** wiki/storage/sqlite.py
    :name: sqlitestorage4

        def save(self, document):
            cursor = self.connection.cursor()
            cursor.execute('SELECT COUNT(*) FROM wikipage '
                           'WHERE title=?',
                           [document.title])
            existing = cursor.fetchone()
            if existing[0] > 0:
                cursor.execute('UPDATE wikipage SET content=? '
                               'WHERE title=?',
                               [document.content, document.title])
            else:
                cursor.execute('INSERT INTO wikipage '
                               '(title, content) VALUES (?, ?)',
                               [document.title, document.content])
            cursor.close()
            self.connection.commit()

.. nextslide::
    :increment:

.. code-block:: python
    :caption: **Filename:** wiki/storage/sqlite.py
    :name: sqlitestorage5

        def load(self, title):
            cursor = self.connection.cursor()
            cursor.execute('SELECT title, content FROM wikipage '
                           'WHERE title=?',
                           [title])
            row = cursor.fetchone()
            cursor.close()
            if not row:
                return None
            else:
                title, content = row
                return WikiPage(title, content)

.. nextslide::
    :increment:

.. code-block:: python
    :caption: **Filename:** wiki/storage/sqlite.py
    :name: sqlitestorage6

        def list(self):
            cursor = self.connection.cursor()
            cursor.execute('SELECT title FROM wikipage')

            titles = []
            for row in cursor:
                titles.append(row[0])
            cursor.close()
            return titles


Essential Modules
-----------------

* :py:mod:`sys`
* :py:mod:`os`
* :py:mod:`os.path`
* :py:mod:`logging`
* :py:mod:`datetime`, :py:mod:`time`
* :py:mod:`unittest`
* :py:mod:`pprint`
* :py:mod:`io`
* :py:mod:`functools`
* :py:mod:`collections`


Other Interesting Modules
-------------------------

============================ ===========================
 Modulename                   Modulename
============================ ===========================
 :py:mod:`argparse`           :py:mod:`multiprocessing`
 :py:mod:`configparser`       :py:mod:`profile`
 :py:mod:`csv`                :py:mod:`pstats`
 :py:mod:`enum`               :py:mod:`random`
 :py:mod:`getpass`            :py:mod:`shutil`
 :py:mod:`hashlib`            :py:mod:`signal`
 :py:mod:`html`               :py:mod:`subprocess`
 :py:mod:`http`               :py:mod:`tempfile`
============================ ===========================


.. include:: ../common/finish.rst

References
----------

Full source code to the above wiki can be :download:`downloaded here <_static/wiki-0.7.tar.gz>` (:download:`zip <_static/wiki-0.7.zip>`).


* http://www.python.org
* http://www.sphinx-doc.org
* https://virtualenvwrapper.readthedocs.org
* https://packaging.python.org
* http://pypi.python.org
