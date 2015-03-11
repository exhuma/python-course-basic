Python
======


Birds-Eye View
--------------

 * Slow
 * Runs on all major platforms.
 * JIT Compiled (into bytecode).
 * Large community. #8 on TIOBE Index (Java on #2, PHP on #7). Based on result
   of March 2015
 * Strict Syntax (indentation matters)!
 * *Large* Standard Library
 * Global Interpreter Lock (the GIL)
 * PEP 8


Implementations
~~~~~~~~~~~~~~~

 * **CPython** (the default - *recommended*).
 * Jython (runs in Java VM).
 * IronPython (runs in dotNET CLR).
 * PyPy (faster).
 * Stackless (microthreads).


Editors
~~~~~~~

* PyCharm -- *https://www.jetbrains.com/pycharm/*
* IDLE
* Komodo IDE -- *http://komodoide.com/*
* Eclipse (with PyDev) -- *https://eclipse.org*
* Netbeans (with Python plugin) -- *https://netbeans.org*


Duck Typing
~~~~~~~~~~~

    When I see a bird that walks like a duck and swims like a duck and quacks
    like a duck, I call that bird a duck.

         *-- James Whitcomb Riley*

+--------------------+--------------------+---------------------+
|                    | **Strong Binding** | **Weak Binding**    |
+--------------------+--------------------+---------------------+
| **Static Typing**  | Java, C#           | ?                   |
+--------------------+--------------------+---------------------+
| **Dynamic Typing** | Python, Ruby       | PHP, C              |
+--------------------+--------------------+---------------------+



Python 2 or 3
-------------

 * Starting from Python 3.3 it has become really usable (current version is 3.4
   with 3.5 on the horizon).
 * No new features are added to Python 2 (f.ex.: ``asyncio``).
 * Python 3 has much improved Unicode support. It puts the developer in control
   (and enforces that control).
 * Python 3 is even slower than Python 2 (at the moment).
 * Legacy platforms may only support Python 2.
 * Iterators


Installation
------------

Linux
~~~~~

* Available by default on most Unix platforms.
* Packaged default may either be Python 2 (Debian, Red-Hat), or Python 3 (Arch).
* Python 2 and 3 can both happily live on the same system without interfering
  with each other.

Windows
~~~~~~~

Installation on Windows is as easy as downlading the installer and running it.



The Python Shell (REPL)
-----------------------

::

    >>> 1 + 1
    2

    >>> print("Hello World!")
    Hello World!


Syntax & Features
-----------------

* Everything is an Object. Even functions.
* Mutable vs. Immutable Objects
* mutable default arguments
* Blocks defined by indentation


Common Data Types
-----------------

* Boolean
* String (unicode sequence)
* Bytes (0-255 sequence)
* Numbers
  * ``numbers``
  * ``fractions``
  * ``cmath``
* Lists
  * can hold objects of any type
  * slicing
  * appending
  * inserting
  * popping
* Tuples
  * Immutable lists
  * Cannot be changed,
  * but can be hashed
* Dictionaries (HashTable)
* Sets (Bag)
