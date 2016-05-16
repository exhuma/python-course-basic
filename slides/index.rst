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

.. |home| image:: _static/icons/home.png
    :class: midline

.. |github| image:: _static/icons/github-circle.png
    :class: midline

.. |gplus| image:: _static/icons/google-plus.png
    :class: midline


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
* Playing with the REPL and Python basics.
* Wiki
    * List pages.
    * Load & display a page.
    * Save a page (create or update).
    * Replace WikiWords with links.
* Packaging

About Me
--------

* First program written in 1989.
* Professional Software Developer since 1998.
* GFA-Basic → Delphi → PHP → Java → Python → ?
* Degree in Computer Science (BSc CS AI).
* Lead Software Developer in Post BackBone-OSS.
* Semantics Nerd, Gamer, Geek.


About You
---------

* Your name
* Your experience
* *What do you expect from this course*


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

    For this course we will use ``Python-3.5.1.tgz``.

    In order to successfully compile with all features for this course, you
    need the required libraries and system packages. For debian derivates these
    packages are:

    * ``build-essential``
    * ``libsqlite3-dev``

    Once the requirements are available run::

        ./configure --prefix=/opt/python3.5
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

* Download the ``python-3.5.x.msi`` file and install.


Introduction
============

* High-level overview of the language.
* Implementations
* Editors
* Language features


Code examples in these slides
-----------------------------

There are 3 ways, this course shows code examples:

* Examples from the Python REPL. These are marked with leading ``>>>``
  characters which is the default REPL promp.
* Blocks with filename header. These are meant to be in the filename seen in
  the header. The filename is always relative to the project folder.
* Blocks without filename header. These are "throwaway" examples which can be
  saved anywhere. Or run directly in the REPL.


Birds-Eye View
--------------

* Runs on all major platforms.
* JIT Compiled (into bytecode).
* Large community. #5 on TIOBE Index (Java on #1, PHP on #6). Based on result
  of May 2016
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


Strings & Bytes in Python 2 & 3
-------------------------------

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


Python 2 vs Python 3
--------------------

.. sidebar:: Python 3.5

    This course is based on **Python 3.5** as it comes bundled with ``pip`` and
    ``pyvenv``.

* Start at Python 3.3+ (current version is 3.5).
* Improved Unicode support. (bytes ≠ text, developer in full control).
* Iterators everywhere.
* No new features are added to Python 2 (f.ex.: :py:mod:`asyncio`, but
  backports exist).
* Python 3 is slower than Python 2 though (at the moment).
* *BUT:* Legacy platforms may only support Python 2.


.. note::
    Python 3.3 reintroduced unicode strings (strings with a ``u`` prefix). This
    prefix was removed in 3.0 and made porting very difficult.


Editors
-------

* PyCharm — *https://www.jetbrains.com/pycharm/*
* IDLE
* Komodo IDE — *http://komodoide.com/*
* Eclipse (with PyDev) — *https://eclipse.org*
* Netbeans (with Python plugin) — *https://netbeans.org*
* Any text-editor
    * vim
    * emacs
    * notepad++
    * sublime
    * …


Duck Typing
-----------

    When I see a bird that walks like a duck and swims like a duck and quacks
    like a duck, I call that bird a duck.

    -- James Whitcomb Riley


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


.. note:: Explore

    Go to http://repl.it/ and try to execute ``20 + "22"`` in some languages.
    What are the results? What does this tell you?

    Make sure to test Python, PHP and JavaScript. They have a very simple REPL
    and show a good example of coercion problems that may arise.

.. admonition:: Definition

    Coercion
        Implicit Type Conversion.

    ``20 + "22" -> ?``


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


Getting Help
------------

* On the web: http://docs.python.org
* Type ``help()`` in the REPL. This can be used on any object::

    >>> myvar = 1
    >>> help(myvar)  # This will open the help for "ints"

* Type ``pydoc`` in the shell.

  * Same as ``help()`` in the REPL.
  * Use ``pydoc -b`` (``python -m pydoc -b`` on Windows) to run a local
    web-server on a random port. This is useful if you have no internet
    connection.


Diving in
=========

.. sidebar:: Explore

    "Explore" blocks show a few simple things for you to try out yourself.

* Saving and running the code.
* Data types and primitives.
* Functions and classes.


Saving your code
----------------

.. sidebar:: Linux, MacOS

    On \*nix systems, you can make the file executable with a shebang. For
    example::

        #!/usr/bin/python

* File extension: ``.py``
* Python files are called *modules*.
* Folders can be used to organise your code into *packages*.
* Folders with modules should contain a file with the name ``__init__.py``.
  This special file marks a folder as *package*.
* Execute files with

.. code-block:: bash

    $ python filename.py



Common Data Types
-----------------

.. sidebar:: Explore

    * ``help(str)`` (skip special methods named  ``__<word>__``)
    * ``help(int)``, ``help(123)``
    * ``help(bytes)``, ``help(b'')``
    * ``type(123)``
    * ``help(None)``
    * ``help(bool)``, ``help(True)``

* None (like ``null``)
* Boolean
* String (unicode sequence)
* Bytes (0-255 sequence)
* Numbers

.. note::

    Useful standard modules when working with numbers:

    - :py:mod:`fractions`
    - :py:mod:`math`
    - :py:mod:`cmath`
    - :py:mod:`statistics` (new in 3.4)

.. nextslide::
    :increment:

.. code-block:: python

    mybool = False
    nothing = None
    mystring = 'hello world'
    mystring2 = "hello w\u00f0rld"  # Python2 needs "u" prefix
    mystring3 = '''John's "world"'''
    mystring4 = """
        Mary's "world"
    """
    mybytes = b'H\xc3\xa9llo World!'
    myint = 123


.. nextslide::
    :increment:

.. sidebar:: Explore

    * ``help(list)``, ``help([])``
    * ``help(tuple)``, ``help((1,2))``

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

* Lists

  - can hold objects of any type, heterogenous
  - slicing
  - appending, inserting
  - popping (queue, stack)

* Tuples (see also: :py:func:`~collections.namedtuple`)

  - Immutable lists
  - Cannot be changed
  - but can be hashed

.. nextslide::
    :increment:

.. code-block:: python

    mylist = [1, 2, 3]
    mylist_2 = [
        1,
        'foo',
        int,
        mylist,
    ]

    mytuple = (1, 2, 3)
    mytuple_2 = (
        1,
        'foo',
        int,
        mylist,
    )

.. nextslide::
    :increment:

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


.. nextslide::
    :increment:

.. code-block:: python

    mydict = {
        'hello': 'world',
        42: 'everything',
    }
    mydict2 = dict(
        foo='world',
        bar='hello',
    )

    myset = {"hello", "hello", "world"}
    myset2 = set(["hello", "hello", "world"])

Python vs other Languages
-------------------------

* Everything is an Object. Even functions.
* Blocks defined by indentation
* "Falsy" values (``''``, ``[]``, ``()``, ``{}``, ``0``, ``False``, ``None``,
  …)
* ``True`` ≡ ``1``
* ``False`` ≡ ``0``
* Variable unpacking (f.ex.: ``a, b = 1, 2``).
* "lambda" expressions.
* :pep:`8`

.. note::

    Historically, ``True`` and ``False`` did not exist in Python. Instead ``1``
    and ``0`` were used. Those literals were introduced in Python 2.2.1. The
    boolean type was introduced in 2.3. The values are *constant* for backwards
    compatibility with older versions.


Exceptions
----------

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
        The finlename that caused the error.

    **line 3**
        The line in the file.

    **in foo**
        The function-name in which the error was thrown.

    Moving up the "stack", the lines have the same format. The further you move
    "up", the closer you get to the entry-point of the application.



Exercise: primitives
--------------------

.. sidebar:: Explore

    * Run ``help`` on your variables (f.ex.: ``help(str)``)
    * Difference between ``mytext.find`` and ``mytext.index``?
    * Difference between ``mytext`` and ``mybytes``?


.. code-block:: python

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

.. sidebar:: Explore
    :class: overlapping

    * Try other types of values (``int``, ``list``, ``tuple``, …) as keys for
      the ``dict``.
    * Try the ``list`` example with a ``tuple``.
    * Run ``help`` on both ``mylist`` and ``mydict``.


.. code-block:: python

    >>> # dictionary
    >>> mydict = {}
    >>> mydict['foo'] = 10
    >>> mydict['foo']
    >>> mydict['bar']
    >>> mydict.get('bar', 'mydefault')

    >>> # list
    >>> mylist = [1, 2, 3]
    >>> mylist
    >>> mylist[1:3]  # 1=included, 3=excluded
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
        '''
        Prints "Hello <name>" to stdout.
        '''
        print('Hello ' + name)


Functions as Objects
--------------------

Because functions are objects, they can be assigned to variables. For example
as values in a dictionary::

    def case_1():
        print("Hello 1")

    def case_2():
        print("Hello 2")

    cases = {
        1: case_1,
        2: case_2,
    }

    user_selection = int(input('Type a number: '))

    function = cases.get(user_selection, lambda: print("unknown case"))
    function()


Documenting Code
----------------

* The first ``string`` inside a module/class/function are their so called
  "docstrings".
* No standard formatting.
* Sphinx (http://www.sphinx-doc.org)
* Accessible via the special variable ``__doc__``.

.. sidebar:: Takeaways

    * Everything is an object. Functions too!

.. code-block:: python

    >>> def noop():
    ...     '''
    ...     Does nothing
    ...     '''
    ...     pass

    >>> print(noop.__doc__)


Exercise: "Falsy" Values
------------------------

.. sidebar:: Takeaways

    * Blocks identified by indentation

.. code-block:: python
    :emphasize-lines: 2

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


Classes – Basics
----------------

* Definition happens at runtime (like with functions).
* Support multiple inheritance.
* No interfaces (Duck Typing).
* **Instance methods get the instance as first parameter.** Conventional name: ``self``
* **Class methods get the class as first parameter.** Conventional name: ``cls``
* Static methods are merely syntactic sugar.


Classes – Basic Example
-----------------------

.. code-block:: python

    class MyClass(AParentClass, AMixinClass):

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


Our Project
===========

:download:`Starter Pack <_static/wiki-skeleton.tar.gz>` (:download:`zip <_static/wiki-skeleton.zip>`)

A very simple wiki page.


Exercise – A Wiki Page
----------------------

.. code-block:: python
    :caption: **Filename:** wiki / model.py

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


.. code-block:: python

    >>> import wiki.model as model
    >>> page = model.WikiPage(
    ...    'index', 'Hello World!')


Wiki Functionality
------------------

* List pages.
* Load & display a page.
* Save a page (create or update).
* Replace WikiWords with links.


Storing documents on Disk
-------------------------

.. note:: Assumptions

    * JSON as format.
    * No checks for FS injections.
    * Page titles are valid filenames.

.. sidebar:: Takeaways
    :class: overlapping

    * Imports
    * Defining classes

.. code-block:: python
    :caption: **Filename:** wiki / storage / disk.py
    :name: diskstorage1

    from os import listdir
    from os.path import join, exists
    import json

    from wiki.model import WikiPage


    class DiskStorage:

        def __init__(self, root):
            self.root = root

        def init(self):
            pass

        def close(self):
            pass

.. nextslide::
    :increment:

.. sidebar:: Takeaways
    :class: overlapping

    * Opening files
    * ``with`` statement

.. code-block:: python
    :caption: **Filename:** wiki / storage / disk.py
    :name: diskstorage2

    def save(self, document):
        filename = join(self.root,
            document.title) + '.json'
        with open(filename, 'w') as file_hndl:
            json.dump({
                'title': document.title,
                'content': document.content
            }, file_hndl)

    def load(self, title):
        filename = join(self.root,
            title) + '.json'
        if not exists(filename):
            return None

        with open(filename, 'r') as file_handle:
            document = json.load(file_handle)

        return WikiPage(document['title'],
                        document['content'])

.. nextslide::
    :increment:

.. sidebar:: Takeaways
    :class: overlapping

    * ``for … in …``  loop
    * Variable unpacking

.. code-block:: python
    :caption: **Filename:** wiki / storage / disk.py
    :name: diskstorage3

    def list(self):
        titles = []
        for filename in listdir(self.root):
            title, _ = filename.rsplit('.', 1)
            titles.append(title)
        return titles


Using the DiskStorage Class
---------------------------

.. sidebar:: Remember
    :class: overlapping

    Packages must have a ``__init__.py`` file!

    `source code (step 1) <_static/wiki-0.1.tar.gz>`_ (`zip <_static/wiki-0.1.zip>`_)

.. code-block:: python
    :caption: **Filename:** runner.py

    from wiki.model import WikiPage
    from wiki.storage.disk import (
        DiskStorage
    )

    storage = DiskStorage('wiki_pages')
    for page in storage.list():
        print(page)

    mypage = WikiPage('HelloWorld', 'This is an example!')
    storage.save(mypage)

    for page in storage.list():
        print(page)

    loaded_page = storage.load('HelloWorld')
    print(mypage == loaded_page)


.. slide::

    .. figure:: _static/checkpoint.jpg
        :class: fill

    :checkpoint:`$ python3 runner.py`


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

    >>> element = 'Whoops'
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

.. code-block:: python

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

* Used with a so called "Context Manager".
* Used for code which needs an "entry" and guaranteed "exit" step (a open file,
  a DB connection, …).
* The ``with`` block does **not** create a new variable scope. Variables
  created in that block are accessible outside!
* Ensures that finalisation step is taken. Even on unexpected exit.
* Context managers can be created manuall by implementing the magic
  ``__enter__`` and ``__exit__`` methods in a class, or
  :py:func:`contextlib.contextmanager`.



Variable Unpacking
------------------

.. sidebar:: Throwaway Variable

    The underscore "``_``" is a perfectly valid identifier in Python. By
    *convention* it is used whenever you must store a value but don't need it.

    This is most commonly used with variable unpacking.

* Assign multiple values at once, "extracting" them from an iterable.
* Use ``_`` for "throwaway" variables.

**Example**

.. code-block:: python

    >>> title, _ = filename.rsplit('.', 1)

    >>> a, _, b = [1, 2, 3]
    >>> print(a)

    >>> # What could possibly go wrong?
    >>> a, b = {'a': 1, 'b': 2}

    >>> # Is this safe?
    >>> a, b = {1, 2}


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

    $ /opt/python3.5/bin/pyvenv env
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


Our first Web Page
------------------

.. sidebar:: Takeaways
    :class: overlapping

    * Module level variables are all-caps (:pep:`8`).
    * Naming variables in function call.
    * There are no "constants" in Python.
    * ``__name__`` is the module's name.
    * Avoiding "import side-effects" using |br| ``if __name__ == '__main__':``


.. code-block:: python
    :caption: **Filename:** wiki / webui.py
    :name: webui1

    from flask import Flask

    APP = Flask(__name__)


    @APP.route('/')
    def index():
        return 'Hello World'


    if __name__ == '__main__':
        APP.run(debug=True, host='0.0.0.0',
                port=5000)

|clear|

.. code-block:: bash

    $ ./env/bin/python wiki/webui.py


.. slide::

    .. figure:: _static/checkpoint.jpg
        :class: fill

    :checkpoint:`http://localhost:5000`



Using our DiskStorage class
---------------------------

Imports:

.. code-block:: python
    :emphasize-lines: 1
    :caption: wiki / webui.py
    :name: webui2

    from flask import Flask, g
    from wiki.storage.disk import DiskStorage

Making storage available:

.. code-block:: python

    @APP.before_request
    def before_request():
        g.db = DiskStorage('wiki_pages')

Prividing a page listing:

.. sidebar:: Takeaways

    * Joining lists

.. code-block:: python
    :emphasize-lines: 4

    @APP.route('/list')
    def list():
        page_names = g.db.list()
        return '\n'.join(page_names)


.. slide::

    .. figure:: _static/checkpoint.jpg
        :class: fill

    :checkpoint:`http://localhost:5000/list`


HTML Output (via templating) in Flask
-------------------------------------

.. code-block:: python
    :emphasize-lines: 1, 8
    :caption: **Filename:** wiki / webui.py
    :name: webui4

    from flask import Flask, g, render_template

    ...

    @APP.route('/list')
    def list():
        page_names = g.db.list()
        return render_template('pagelist.html',
                               page_names=page_names)

.. sidebar:: Source Code

    `source code (step 2) <_static/wiki-0.2.tar.gz>`_ (`zip <_static/wiki-0.2.zip>`_)


.. slide::

    .. figure:: _static/checkpoint.jpg
        :class: fill

    :checkpoint:`http://localhost:5000/list`


Wiki Functionality
------------------

* :strike:`List pages`
* Load & display a page
* Save a page (create or update)
* Replace WikiWords with links.


Loading and Displaying a Page
-----------------------------

.. code-block:: python
    :caption: **Filename:** wiki / webui.py
    :name: webui5
    :emphasize-lines: 3

    ...

    @APP.route('/<name>')
    def display(name):
        page = g.db.load(name)
        return render_template('page.html', page=page)

    ...

.. sidebar:: Source Code
    :class: overlapping

    `source code (step 3) <_static/wiki-0.3.tar.gz>`_ (`zip <_static/wiki-0.3.zip>`_)


.. slide::

    .. figure:: _static/checkpoint.jpg
        :class: fill

    :checkpoint:`http://localhost:5000/BingoBongo`


Wiki Functionality
------------------

* :strike:`List pages`
* :strike:`Load & display a page`
* Save a page (create or update)
* Replace WikiWords with links.


Creating Pages
--------------

.. code-block:: python
    :caption: **Filename:** wiki / webui.py
    :name: webui7
    :emphasize-lines: 1-2, 7-11, 14-20

    from flask import ..., redirect, url_for, request
    from wiki.model import WikiPage

    @APP.route('/<name>')
    def display(name):
        page = g.db.load(name)
        if not page:
            return render_template('edit_page.html', name=name)
        if 'edit' in request.args:
            return render_template('edit_page.html', name=name,
                                   content=page.content)
        return render_template('page.html', page=page)

    @APP.route('/', methods=['POST'])
    def save_page():
        page = WikiPage(request.form['title'],
                        request.form['content'])
        g.db.save(page)
        return redirect(url_for('display', name=page.title))


.. sidebar:: Source Code
    :class: overlapping

    `source code (step 4) <_static/wiki-0.4.tar.gz>`_ (`zip <_static/wiki-0.4.zip>`_)


.. slide::

    .. figure:: _static/checkpoint.jpg
        :class: fill

    :checkpoint:`http://localhost:5000/BingoBongo`


Wiki Functionality
------------------

* :strike:`List pages`
* :strike:`Load & display a page`
* :strike:`Save a page (create or update)`
* Replace WikiWords with links.


Creating an Index Page
----------------------

… and let's replace the hard-coded "Hello World" index page with a default wiki
page.

.. code-block:: python
    :caption: **Filename:** wiki / webui.py
    :name: webui8
    :emphasize-lines: 5

    ...

    @APP.route('/')
    def index():
        return redirect('/Index')

    ...


Replacing WikiWords
-------------------

Flask allows us to *easily* create "modifier" functions for values. Turning an
existing document into HTML is essentially a modification of the raw content.
So we will create a filter.


Planning the Filter
-------------------


.. code-block:: python

    @APP.template_filter('wikify')
    def wikify(text):
        return text.upper()

* Filters are functions that take a string and return a modified string.
* **Input:** ``'Foo HelloWorld bar'`` |br|
  **Output:** ``'Foo <a href="http://localhost:5000/HelloWorld"> HelloWorld</a> bar'``
* **Challenge:** Use ``url_for`` to create proper URLs.
* *How?*


Custom Template Filter
----------------------

.. code-block:: python
    :caption: **Filename:** wiki / webui.py
    :name: webui10

    import re

    P_WIKIWORD = re.compile(r'\b((?:[A-Z][a-z0-9]+){2,})\b')

    def make_page_url(match):
        groups = match.groups()
        title = groups[0]
        return '<a href="{url}">{title}</a>'.format(
            url=url_for('display', name=title),
            title=title)

    @APP.template_filter('wikify')
    def wikify(text):
        # NOTE: We could do much more here!
        return P_WIKIWORD.sub(make_page_url, text)


.. slide::

    .. image:: _static/shock.jpg
        :align: center


Let's pick this apart
---------------------

.. sidebar:: "Raw" Strings
    :class: overlapping

    A string prefixed with an `r` is a raw string. This means that no escaping
    is done. For example, ``\n`` will not be replaced by a newline.

.. code-block:: python

    import re  # Import the regex module

    # pre-compile the regular expression
    P_WIKIWORD = re.compile(
        r'\b((?:[A-Z][a-z0-9]+){2,})\b')

    # Assigns a new filter. Filters can be used in the template to "modify"
    # values (see also the ``safe`` filter we used earlier.
    @APP.template_filter('wikify')
    def wikify(text):
        # This takes the value from the template and returns a modified text.
        return P_WIKIWORD.sub(make_page_url, text)

:py:func:`re.sub` replaces all occurrences in a string with something else. In
this case we give a *function* as replacement. This function will be called for
each match.


.. nextslide::
    :increment:

The following function is created to be used in ``re.sub``. It takes a
``match`` object, and returns a replacement string.

This is needed so we can use ``url_for`` to generate the correct URLs.

Python string formatting can be done using C-Style ``%`` escapes, *or* using a
mini templating language.

.. code-block:: python

    def make_page_url(match):
        groups = match.groups()
        title = groups[0]
        return '<a href="{url}">{title}</a>'.format(
            url=url_for('display', name=title),
            title=title)

.. slide:: That *thing* again
    :level: 2

    .. code-block:: python
        :caption: **Filename:** wiki / webui.py
        :name: webui11

        import re

        P_WIKIWORD = re.compile(r'\b((?:[A-Z][a-z0-9]+){2,})\b')

        def make_page_url(match):
            groups = match.groups()
            title = groups[0]
            return '<a href="{url}">{title}</a>'.format(
                url=url_for('display', name=title),
                title=title)

        @APP.template_filter('wikify')
        def wikify(text):
            # NOTE: We could do much more here!
            return P_WIKIWORD.sub(make_page_url, text)


.. slide::

    `source code (step 5) <_static/wiki-0.5.tar.gz>`_ (`zip <_static/wiki-0.5.zip>`_)

.. slide::

    .. figure:: _static/checkpoint.jpg
        :class: fill

    :checkpoint:`http://localhost:5000/list`


String Formatting
-----------------

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


================ =========================
 C-Style           Mini-Language
================ =========================
 faster            slower
 less readable     more readable
 less verbose      more verbose
 less powerful     more powerful
================ =========================


Wiki Functionality
------------------

* :strike:`List pages`
* :strike:`Load & display a page`
* :strike:`Save a page (create or update)`
* :strike:`Replace WikiWords with links.`


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
    :caption: Uploading / Publishing

    $ python setup.py register
    $ twine upload dist/*

See: https://packaging.python.org

.. sidebar:: Source Code
    :class: overlapping

    `source code (step 6) <_static/wiki-0.6.tar.gz>`_ (`zip <_static/wiki-0.6.zip>`_)


Deploying
---------

* WSGI (:pep:`333` and :pep:`3333`) — Commonly pronounced "Whisky"
* Web Server Gateway Interface.
* Supported by all major web servers (Apache httpd, nginx, Tornado, …)

.. image:: _static/whisky.jpg
    :align: center


Apache httpd
------------

.. code-block:: python
    :caption: / var / www / mywiki / wsgi / myapp.wsgi

    from wiki.webui import APP as application

.. code-block:: apache
    :caption: / etc / apache2 / site-available / mywiki.conf

    <VirtualHost 1.2.3.4:80>
        ServerName mywiki.example.com

        WSGIDaemonProcess yourapplication user=user1 group=group1 \
            threads=5
        WSGIScriptAlias / /var/www/mywiki/wsgi/myapp.wsgi

        <Directory /var/www/mywiki>
            WSGIProcessGroup yourapplication
            WSGIApplicationGroup %{GLOBAL}
            Order deny,allow
            Allow from all
        </Directory>
    </VirtualHost>



Database Connectivity
=====================

* DBAPI2 (:pep:`249`)
* :py:mod:`sqlite3`


Our own Storage API
-------------------

* Remember ``wiki/storage/disk.py``

.. code-block:: python
    :caption: Storage API

    def save(self, document: WikiPage) -> None:
        pass

    def load(self, title: str) -> Optional[WikiPage]:
        pass

    def list(self) -> List[str]:
        pass

.. note::

    * Type hints are *provisional* in Python 3.5 (See :pep:`484`)
    * Syntax is valid back to Python 3.2 (:pep:`3107`)


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
    :caption: **Filename:** wiki / storage / sqlite.py
    :name: sqlitestorage2

    import sqlite3

    from wiki.model import WikiPage


    class SQLiteStorage:

        def __init__(self, dsn):
            self.connection = sqlite3.connect(dsn)

.. nextslide::
    :increment:

.. code-block:: python
    :caption: **Filename:** wiki / storage / sqlite.py
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
    :caption: **Filename:** wiki / storage / sqlite.py
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
    :caption: **Filename:** wiki / storage / sqlite.py
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
    :caption: **Filename:** wiki / storage / sqlite.py
    :name: sqlitestorage6

        def list(self):
            cursor = self.connection.cursor()
            cursor.execute('SELECT title FROM wikipage')

            titles = []
            for row in cursor:
                titles.append(row[0])
            cursor.close()
            return titles


Out with the old, in with the new
---------------------------------

.. sidebar:: Takeaways
    :class: overlapping

    * Exception Handling

    `source code (step 7) <_static/wiki-0.7.tar.gz>`_ (`zip <_static/wiki-0.7.zip>`_)

.. code-block:: python
    :caption: **Filename:** wiki / webui.py
    :name: webui12

    from wiki.storage.sqlite import SQLiteStorage

    @APP.before_first_request
    def init_storage():
        try:
            db = SQLiteStorage('wikipages.sqlite')
            db.init()
        except Exception as exc:
            print(exc)
        finally:
            db.close()

    @APP.before_request
    def before_request():
        g.db = SQLiteStorage('wikipages.sqlite')

    @APP.teardown_request
    def teardown_request(request):
        g.db.close()
        return request


.. slide::

    .. figure:: _static/checkpoint.jpg
        :class: fill

    :checkpoint:`http://localhost:5000`



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


Common Mistakes
---------------

* Mutable vs. Immutable Objects
* mutable default arguments
* Automatic string concatenation

.. code-block:: bash

    $ python -m timeit "'aaa' 'bbb'"
    $ python -m timeit "'aaa' + 'bbb'"


.. slide::
    :level: 2

    .. container:: centered

        Thank You!

        .. image:: _static/avatar.jpg
            :align: center
            :class: avatar

        Questions?

    * |home| http://michel.albert.lu
    * |github| exhuma
    * |gplus| MichelAlbert

References
----------

Full source code to the above wiki can be :download:`downloaded here <_static/wiki-0.7.tar.gz>` (:download:`zip <_static/wiki-0.7.zip>`).


* http://www.python.org
* http://www.sphinx-doc.org
* https://virtualenvwrapper.readthedocs.org
* https://packaging.python.org
* http://www.sqlalchemy.org
* http://pypi.python.org
* http://jinja.pocoo.org

