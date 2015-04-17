Python
======

About You
---------

* Your name
* Your experience
* What do you expect from this course
* Interest


Installation
============

Linux
-----

.. sidebar:: Custom install on Linux
    :subtitle: ~5min

    ::

        ./configure --prefix=/opt/python3.4
        make
        sudo make install


* Available by default on most Unix platforms.
* Packaged default may either be Python 2 (Debian, Red-Hat), or Python 3 (Arch).
* Python 2 and 3 can both happily live on the same system without interfering
  with each other (f.ex. the ``python`` and ``python3`` packages on debian and
  derivates).


Windows
-------

Installation on Windows is as easy as downlading the installer and running it.

------------------------------------------------------------------------------

.. attention::
    Installing compiled extensions (f.ex. C/C++) is more difficult on Windows
    as an appropriate compiler must be present. This is out of scope of this
    presentation.


Introduction
============

Birds-Eye View
--------------

* Runs on all major platforms.
* JIT Compiled (into bytecode).
* Large community. #8 on TIOBE Index (Java on #2, PHP on #7). Based on result
  of March 2015
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
* ...


Editors
-------

* PyCharm — *https://www.jetbrains.com/pycharm/*
* IDLE
* Komodo IDE — *http://komodoide.com/*
* Eclipse (with PyDev) — *https://eclipse.org*
* Netbeans (with Python plugin) — *https://netbeans.org*


Duck Typing
-----------

    When I see a bird that walks like a duck and swims like a duck and quacks
    like a duck, I call that bird a duck.

    -- James Whitcomb Riley

Duck Typing (ctd.)
------------------

+--------------------+--------------------+---------------------+
|                    | **Strong Binding** | **Weak Binding**    |
+--------------------+--------------------+---------------------+
| **Static Typing**  | Java, C#           | ?                   |
+--------------------+--------------------+---------------------+
| **Dynamic Typing** | Python, Ruby       | PHP, C              |
+--------------------+--------------------+---------------------+



Use Python 3
------------

.. sidebar:: Python 3.4

    This course is based on **Python 3.4** as it comes bundled with ``pip`` and
    ``pyvenv``.

* Python 3.3+ (current version is 3.4 with 3.5 on the horizon).
* Improved Unicode support. (bytes ≠ text, developer in full control).
* Iterators everywhere.
* No new features are added to Python 2 (f.ex.: ``asyncio``, but backports
  exist).
* Python 3 is slower than Python 2 though (at the moment).
* Legacy platforms may only support Python 2.


The Python Shell (REPL)
-----------------------

* read-eval-print loop.
* Interactive shell.
* Extremely helpful tool to test out ideas, play with code before implementing
  it.

Simply run ``python`` on the console to start it.

By convention, lines with ``>>>`` represent a REPL prompt.

.. code:: python

    >>> 1 + 1
    2

    >>> print("Hello World!")
    Hello World!


Getting Help
------------

* On the web: http://docs.python.org
* Type ``help()`` in the REPL. This can be used on any object::

    >>> myvar = 1
    >>> help(myvar)  # This will open the help for "ints"

* Type ``pydoc`` in the shell.

  * Same as ``help()`` in the REPL.
  * Use ``pydoc -p 8080`` to run a local web-server on port ``8080``. This is
    useful if you have no internet connection.
  * … or ``pydoc -g`` to run a GUI (pretty much useless).


Diving in
=========

Common Data Types
-----------------

.. sidebar:: Explore

    * ``help(None)``
    * ``help(bool)``, ``help(True)``
    * ``help(str)``, ``help('')``
    * ``help(bytes)``, ``help(b'')``
    * ``help(int)``, ``help(123)``

* None (like ``null``)
* Boolean
* String (unicode sequence)
* Bytes (0-255 sequence)
* Numbers

.. tip::

    Useful standard modules when working with numbers:

    - ``fractions``
    - ``math``
    - ``cmath``
    - ``statistics`` (new in 3.4)


Common Data Types (ctd.)
------------------------

.. sidebar:: Explore

    * ``help(list)``, ``help([])``
    * ``help(tuple)``, ``help((1,2))``


* Lists

  - can hold objects of any type, heterogenous
  - slicing
  - appending, inserting
  - popping

* Tuples, Namedtuples

  - Immutable lists
  - Cannot be changed,
  - but can be hashed

Common Data Types (ctd.)
------------------------

.. sidebar:: Explore

    * ``help(dict)``, ``help({})``
    * ``help(set)``

* Dictionaries

  - a.k.a. a HashTable
  - keys can be anything that can be hashed.
  - values can be anything.

* Sets

  - a.k.a. a Bag
  - values must be hashable.
  - only the *first* element is kept. Adding new identical items has no effect.


Python vs other Languages
-------------------------

* Everything is an Object. Even functions.
* Blocks defined by indentation
* "Falsy" values (``''``, ``[]``, ``()``, ``{}``, ``0``, ``False``, …)
* ``True == 1 and False == 0``
* Variable unpacking
* PEP 8


Exercise: scalars
-----------------

.. to-do item #1 code

.. sidebar:: Explore

    * Run ``help`` on your variables (f.ex.: ``help(mytext)``)
    * Difference between ``mytext.find`` and ``mytext.index``?
    * Difference between ``mytext`` and ``mybytes``?


.. code:: python

    >>> mytext = 'Hello World!'
    >>> mytext.split()
    >>> mytext[0:5]
    >>> mytext.find('o')

    >>> mybytes = b'Hello World!'

    >>> myint = 10
    >>> int('101010', 2)

    >>> mybool = True
    >>> bool('hello')
    >>> bool('')


Exercise: collections
---------------------

.. to-do item #1 code

.. sidebar:: Explore

    * Try other types of values (``int``, ``list``, ``tuple``, ...) as keys for
      the ``dict``.
    * Try the ``list`` example with a ``tuple``.
    * Run ``help`` on both ``mylist`` and ``mydict``.


.. code:: python

    >>> # dictionary
    >>> mydict = {}
    >>> mydict['foo'] = 10
    >>> mydict['foo']
    >>> mydict['bar']
    >>> mydict.get('bar', 'mydefault')

    >>> # list
    >>> mylist = [1, 2, 3]
    >>> mylist
    >>> mylist[1:3]
    >>> mylist[0]
    >>> mylist[10]
    >>> mylist[2] = 10
    >>> mylist.append(4)


Functions
---------

* Defined using the ``def`` keyword.
* Always return a value. If no value is specified, it will return ``None``
* In Python they are "First-Class Functions" (i.e.: funtions are objects too).
* Function definition is executed *at runtime* (usually during ``import``)!

Example::

    def say_hello(name):
        print('Hello ' + name)


Exercise: "Falsy" Values
------------------------

.. to-do item #2, #32 code

.. sidebar:: Takeaways

    * Blocks identified by indentation

.. code:: python

    >>> def trueish(true_enough):
    >>>     if true_enough:
    >>>         print('yes.')
    >>>     else:
    >>>         print('no.')

    >>> # Text
    >>> trueish('')
    >>> trueish('hello world')

    >>> # Numbers
    >>> trueish(123)
    >>> trueish(0)
    >>> trueish(-100)

    >>> # Lists
    >>> trueish([])
    >>> trueish([1, 2, 3])


Saving your code
----------------

.. sidebar:: Linux, MacOS

    On \*nix systems, you can make the file executable with a shebang.


* File extension: ``.py``
* Python files are called *modules*.
* Folders can be used to organise your code into *packages*.
* Folders with modules should contain a file with the name ``__init__.py``.
  This special file marks a folder as *package*.
* Execute files with::

    $ python filename.py



Classes – Basics
----------------

.. to-do item #33

* Definition happens at runtime (like with functions).
* Support multiple inheritance.
* No interfaces (Duck Typing).
* **Instance methods get the instance as first parameter.** Conventional name: ``self``
* **Class methods get the class as first parameter.** Conventional name: ``cls``
* Static methods are merely syntactic sugar.


Exercise – A Wiki Page
----------------------

.. code:: python

    # Filename: wiki/model.py
    class WikiPage:

        def __init__(self, title, content):
            self.title = title
            self.content = content

        def teaser(self):
            return self.content

Usage:

.. sidebar:: Explore

    * Run ``help`` on your created instance.
    * Execute the function ``dir`` on your created instance.
    * Try assigning a value to ``page.content``


.. code:: python

    >>> import model
    >>> page = model.WikiPage(
    ...    'index', 'Hello World!')


Wiki Functionality
------------------

* Save a page (create or update)
* Load a page
* Display a page
* List pages


Storing files on Disk
---------------------

.. note:: Assumptions

    * JSON as format.
    * No checks for FS injections.
    * Page titles are valid filenames.

.. sidebar:: Takeaways
    :class: overlapping

    * Imports
    * Defining classes
    * Opening files
    * ``with`` statement

.. code:: python

    # Filename: wiki/storage/disk.py
    from os import listdir
    from os.path import join, exists
    import json

    from wiki.model import WikiPage


    class DiskStorage:

        def __init__(self, root):
            self.root = root

        def save(self, document):
            filename = join(self.root, document.title) + '.json'
            with open(filename, 'w') as file_handle:
                json.dump({
                    'title': document.title,
                    'content': document.content
                }, file_handle)



Storing files on disk (ctd)
---------------------------

.. sidebar:: Takeaways
    :class: overlapping

    * ``for … in …``  loop
    * Variable unpacking

.. code:: python

    class DiskStorage:  # continuation

        def load(self, title):
            filename = join(self.root,
                title) + '.json'
            if not exists(filename):
                return None

            with open(filename, 'r') as file_handle:
                document = json.load(file_handle)

            return WikiPage(document['title'],
                            document['content'])

        def list(self):
            titles = []
            for filename in listdir(self.root):
                title, _ = filename.rsplit('.', 1)
                titles.append(title)
            return titles


Imports
-------

* Partial imports are possible (``from foo import bar``)
* *Never* write ``from foo import *`` (Why?).
* Can be wrapped in a ``try … except`` block (more on this later). This allows
  for graceful degradation.
* They do not have to be at the beginning of the file.
* They are cached. File lookup, and actual loading only happens the first
  time.

.. warning:: Import Side-Effects

    Modules (``.py``) files should never execute active code on it's root! This
    code will be executed on import and is very hard to test with unit-tests!


The "``in``" Operator
---------------------

.. sidebar:: Warning

    A ``for`` loop does not create a new scope, and variables from that block
    will leak to the outside!

* Loops
* Tests for membership

**Examples:**

.. code:: python

    >>> for element in [1, 2, 3]:
    >>>     print(element)
    >>>
    >>> print(element)  # Caution! Keep this in mind!

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

.. code:: python

    with open('names.txt') as file_handle:
        names = file_handle.read().splitlines()

    for name in names:
        if name == 'foo':
            print('foo was found!')
            break
    else:
        print('foo was not found in the file!')


The "``with``" Statement
------------------------

* Also called "Context Manager"
* Used for code which needs a clean "finalisation" step (closing an open file,
  a DB connection, …).
* The ``with`` block does **not** create a new variable scope. Variables
  created in that block are accessible outside!
* Ensures that finalisation step is taken. Even on unexpected exit.
* Can be created by implementing the magic ``__enter__`` and ``__exit__``
  methods in a class.


Variable Unpacking
------------------

.. sidebar:: Throwaway Variable

    The underscore "``_``" is a perfectly valid identifier in Python. By
    *convention* it is used whenever you must store a value but don't need it.

    This is most commonly used with variable unpacking.

    Using the conventional ``_``, communicates to any future reader that the
    variable is intentionally unused.

* Assign multiple values at once, "extracting" them from an iterable.
* Use ``_`` for "throwaway" variables.

**Example**

.. code:: python

    >>> a, _, b = [1, 2, 3]
    >>> print(a)

    >>> # What could possibly go wrong?
    >>> a, b = {'a': 1, 'b': 2}

    >>> # Is this safe?
    >>> a, b = {1, 2}


Common Mistakes
---------------

* Mutable vs. Immutable Objects
* mutable default arguments
* Automatic string concatenation::

    $ python -m timeit "'aaa' 'bbb'"
    $ python -m timeit "'aaa' + 'bbb'"
