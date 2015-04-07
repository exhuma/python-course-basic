Python
======

About You
---------

* Your name
* Your experience
* What do you expect from this course
* Interest


Birds-Eye View
--------------

* Runs on all major platforms.
* JIT Compiled (into bytecode).
* Large community. #8 on TIOBE Index (Java on #2, PHP on #7). Based on result
  of March 2015
* Strict Syntax (indentation matters)!
* *Large* Standard Library
* Global Interpreter Lock (the GIL)
* Slow


Implementations
---------------

* **CPython** (the default - *recommended*, ≠ cython).
* Jython (runs in Java VM).
* IronPython (runs in dotNET CLR).
* PyPy (faster).
* Stackless (microthreads).


Editors
-------

* PyCharm -- *https://www.jetbrains.com/pycharm/*
* IDLE
* Komodo IDE -- *http://komodoide.com/*
* Eclipse (with PyDev) -- *https://eclipse.org*
* Netbeans (with Python plugin) -- *https://netbeans.org*


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

* Python 3.3+ (current version is 3.4 with 3.5 on the horizon).
* Improved Unicode support. (bytes ≠ text, developer in full control).
* Iterators everywhere.
* No new features are added to Python 2 (f.ex.: ``asyncio``, but backports
  exist).
* Python 3 is slower than Python 2 though (at the moment).
* Legacy platforms may only support Python 2.


Installation
============

Linux
-----

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
    Installing compiled extensions (f.ex. C/C++) in "virtual environments" is
    more difficult on Windows as an appropriate compiler must be present.

    More on "virtual environments" if time permits.



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

  * Use ``pydoc -p 8080`` to run a local web-server on port ``8080``
  * … or ``pydoc -g`` to run a GUI (pretty much useless).


Common Data Types
-----------------

* Boolean -- ``help(bool)``
* String (unicode sequence) -- ``help(str)``
* Bytes (0-255 sequence) -- ``help(bytes)``
* Numbers -- ``help(int)``

  - ``numbers``
  - ``fractions``
  - ``cmath``

Common Data Types (ctd.)
------------------------

* Lists -- ``help(list)``

  - can hold objects of any type, heterogenous
  - slicing
  - appending, inserting
  - popping

* Tuples, Namedtuples -- ``help(tuple)``

  - Immutable lists
  - Cannot be changed,
  - but can be hashed

* Dictionaries (HashTable) -- ``help(dict)``
* Sets (Bag) -- ``help(set)``


Python vs other Languages
-------------------------

* PEP 8
* Everything is an Object. Even functions.
* Blocks defined by indentation
* "Falsy" values (``''``, ``[]``, ``()``, ``{}``, ``0``, ``False``, …)
* ``True == 1 and False == 0``
* Variable unpacking


Common Mistakes
---------------

* Mutable vs. Immutable Objects
* mutable default arguments
* Automatic string concatenation::

    $ python -m timeit "'aaa' 'bbb'"
    $ python -m timeit "'aaa' + 'bbb'"
