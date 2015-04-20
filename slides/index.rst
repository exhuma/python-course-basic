.. |br| raw:: html

   <br />

.. |clear| raw:: html

   <br clear="both" />

.. role:: strike
    :class: strike


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

* Linux
* Windows
* MacOS


Linux
-----

.. sidebar:: Custom install on Linux
    :subtitle: ~5min

    For this course, we need ``libsqlite3-dev``!

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

* High-level overview of the language.
* Implementations
* Editors
* Language features


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
  * Use ``pydoc -p 8080`` to run a local web-server on port ``8080``. This is
    useful if you have no internet connection.
  * … or ``pydoc -g`` to run a GUI (pretty much useless).


Diving in
=========

* Language data types and primitives.
* Functions and classes.
* Saving and running the code.


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

.. to-do item #1 code

.. sidebar:: Explore

    * Try other types of values (``int``, ``list``, ``tuple``, ...) as keys for
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
        '''
        Prints "Hello <name>" to stdout.
        '''
        print('Hello ' + name)


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

.. to-do item #2, #32 code

.. sidebar:: Takeaways

    * Blocks identified by indentation

.. code-block:: python

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



Classes – Basics
----------------

.. to-do item #33

* Definition happens at runtime (like with functions).
* Support multiple inheritance.
* No interfaces (Duck Typing).
* **Instance methods get the instance as first parameter.** Conventional name: ``self``
* **Class methods get the class as first parameter.** Conventional name: ``cls``
* Static methods are merely syntactic sugar.


Demo Project
============

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

.. code-block:: python
    :caption: **Filename:** wiki / storage / disk.py

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


Storing files on disk (ctd)
---------------------------

.. sidebar:: Takeaways
    :class: overlapping

    * Opening files
    * ``with`` statement

.. code-block:: python
    :caption: **Filename:** wiki / storage / disk.py

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

Storing files on disk (ctd)
---------------------------

.. sidebar:: Takeaways
    :class: overlapping

    * ``for … in …``  loop
    * Variable unpacking

.. code-block:: python
    :caption: **Filename:** wiki / storage / disk.py

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

    Remember that packages must have a ``__init__.py`` file!

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



Imports
-------

* Partial imports are possible (``from foo import bar``)
* Aliasing imports: ``from foo import bar as qux``
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

.. code-block:: python

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
* Used for code which needs a clean "finalisation" step (closing an open file,
  a DB connection, …).
* The ``with`` block does **not** create a new variable scope. Variables
  created in that block are accessible outside!
* Ensures that finalisation step is taken. Even on unexpected exit.
* Context managers can be created by implementing the magic ``__enter__`` and
  ``__exit__`` methods in a class.


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

.. sidebar:: Alternative use

    * ``$ source env/bin/activate``
    * ``virtualenvwrapper``

.. code-block:: bash

    $ /opt/python3.4/bin/pyvenv env
    $ ./env/bin/pip install flask


Packaging our application
-------------------------

A minimal setup script:

.. code-block:: python
    :caption: **Filename:** setup.py

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

    * Module level variables are all-caps (PEP 8).
    * Naming variables in function call.
    * There are no "constants" in Python.
    * ``__name__`` is the module's name.
    * Avoiding "import side-effects" using |br| ``if __name__ == '__main__':``


.. code-block:: python
    :caption: **Filename:** wiki / webui.py

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


Using our DiskStorage class
---------------------------

Imports:

.. code-block:: python
    :emphasize-lines: 1

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
        pages = g.db.list()
        return '\n'.join(pages)


HTML Output (via templating) in Flask
-------------------------------------

.. code-block:: python
    :emphasize-lines: 1, 8
    :caption: **Filename:** wiki / webui.py

    from flask import Flask, g, render_template

    ...

    @APP.route('/list')
    def list():
        page_names = g.db.list()
        return render_template('pagelist.html', page_names=page_names)


.. slide::

    .. image:: _static/brace_for_html.jpg
        :align: center


HTML Output (ctd.)
------------------

* Jinja Templating Engine (http://jinja.pocoo.org)

.. code-block:: html+jinja
    :caption: **Filename:** wiki / templates / pagelist.html

    <html>
    <body>
      <ul>
      {% for name in page_names %}
        <li>{{name}}</li>
      {% endfor %}
      </ul>
    </body>
    </html>


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
    :emphasize-lines: 3

    ...

    @APP.route('/<name>')
    def display(name):
        page = g.db.load(name)
        return render_template('page.html', page=page)

    ...

.. code-block:: html+jinja
    :caption: **Filename:** wiki / templates / page.html

    <html>
    <body>
      {{page.content|safe}}
      <hr />
      <a href="{{url_for('display', name=page.title, edit=True)}}">
        Edit</a>
    </body>
    </html>


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
    :emphasize-lines: 1-2, 7-11, 15-20

    from flask import ..., redirect, url_for
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


Creating Pages (ctd.)
---------------------

.. code-block:: html+jinja
    :caption: **Filename:** wiki / templates / edit_page.html

    <html>
    <body>
    <form action="{{url_for('index')}}" method="POST">
      Title: <input type="text"
                    name="title"
                    value="{{name}}" /><br />
      Content<br />
      <textarea name="content" rows="10"
                cols="80">{{content|safe}}</textarea>
      <br />
      <input type="submit" />
    </form>
    </body>
    </html>


Wiki Functionality
------------------

* :strike:`List pages`
* :strike:`Load & display a page`
* :strike:`Save a page (create or update)`
* Replace WikiWords with links.


Page Listing Revisited
----------------------

Let's add links to our page listing:

.. code-block:: html+jinja
    :caption: **Filename:** wiki / templates / pagelist.html
    :emphasize-lines: 5-6

    <html>
    <body>
    <ul>
    {% for name in page_names %}
      <li><a href="{{url_for('display',
        name=name.title())}}">{{name}}</a></li>
    {% endfor %}
    </ul>
    </body>
    </html>


Creating an Index Page
----------------------

… and let's replace the hard-coded "Hello World" index page with a default wiki
page.

.. code-block:: python
    :caption: **Filename:** wiki / webui.py
    :emphasize-lines: 5

    ...

    @APP.route('/')
    def index():
        return redirect('/Index')

    ...


Replacing WikiWords
-------------------

.. code-block:: html+jinja
    :caption: **Filename:** wiki / templates / page.html
    :emphasize-lines: 3

    <html>
    <body>
      {{page.content|wikify|safe}}
      <hr />
      <a href="{{url_for('display', name=page.title, edit=True)}}">
        Edit</a>
    </body>
    </html>


Flask allows us to *easily* create "modifier" functions for values. Turning an
existing document into HTML is essentially a modification of the raw content.
So we will create a filter.


Custom Template Filter
----------------------

.. code-block:: python
    :caption: **Filename:** wiki / webui.py

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

``re.sub`` replaces all occurrences in a string with something else. In this
case we give a *function* as replacement. This function will be called for each
match.


Let's pick this apart (ctd)
---------------------------

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

That *thing* again
------------------

.. code-block:: python
    :caption: **Filename:** wiki / webui.py

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


Page Layout
-----------

.. code-block:: html+jinja
    :caption: **Filename:** wiki / templates / master.html

    <html>
    <body>
      <nav>
        <a href="{{url_for('list')}}">Page List</a>
      </nav>
      <hr />
      <div id="content">{% block content %}{% endblock %}</div>
    </body>
    </html>

.. code-block:: html+jinja
    :caption: **Filename:** wiki / templates / page.html

    {% extends "master.html" %}
    {% block content %}
    {{page.content|wikify|safe}}
    <hr />
    <a href="{{url_for('display', name=page.title, edit=True)}}">
      Edit</a>
    {% endblock %}


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

    from setuptools import setup, find_packages
    from pkg_resources import resource_string
    setup(
        name='wiki',
        description="Replacemend for Wikipedia",
        url="http://www.newwp-project.com",
        license="BSD",
        author="Michel Albert",
        author_email="michel@albert.lu",
        version='1.0',
        packages=find_packages(),
        install_requires=[
            'Flask',
        ],
    )

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


Deploying
---------

* WSGI (PEP 333 and PEP 3333) — Commonly pronounced "Whisky"
* Web Server Gateway Interface.
* Supported by all major web servers (Apache httpd, nginx, Tornado, …)

.. image:: _static/whisky.jpg
    :align: center


Apache httpd
------------

.. code-block:: python
    :caption: / var / www / mywiki / wsgi / myall.wsgi

    from wiki.webui import APP as application

.. code-block:: apache
    :caption: / etc / apache2 / site-available / mywiki.conf

    <VirtualHost 1.2.3.4:80>
        ServerName mywiki.example.com

        WSGIDaemonProcess yourapplication user=user1 group=group1 \
            threads=5
        WSGIScriptAlias / /var/www/mywiki/wsgi/myall.wsgi

        <Directory /var/www/mywiki>
            WSGIProcessGroup yourapplication
            WSGIApplicationGroup %{GLOBAL}
            Order deny,allow
            Allow from all
        </Directory>
    </VirtualHost>



Database Connectivity
=====================

* DBAPI2 (PEP 249)
* SQLAlchemy
* sqlite3


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

* Type hints will be *provisional* in Python 3.5 (See PEP 484)
* Syntax is valid back to Python 3.2 (PEP 3107)


SQLite and DPAPI 2
------------------

SQLite3 is included in the Python standard library (since Python 2.5). It is
compliant to DBAPI2 (PEP 249).

DBAPI compliant code looks like this:

.. code-block:: python

    connection = driver.connect(driver_parameters)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mytable")
    for row in cursor:
        print(row)
    connection.close()

.. warning::

    If you compile Python manually, the sqlite development headers
    (``libsqlite3-dev`` on debian and derivates) must be available. If not, the
    extension will not be included!


A new Storage class
-------------------

.. code-block:: python
    :caption: **Filename:** wiki / storage / sqlite.py

    import sqlite3

    from wiki.model import WikiPage


    class SQLiteStorage:

        def __init__(self, dsn):
            self.connection = sqlite3.connect(dsn)

A new Storage class (ctd.)
--------------------------

.. code-block:: python
    :caption: **Filename:** wiki / storage / sqlite.py

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

A new Storage class (ctd.)
--------------------------

.. code-block:: python
    :caption: **Filename:** wiki / storage / sqlite.py

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

A new Storage class (ctd.)
--------------------------

.. code-block:: python
    :caption: **Filename:** wiki / storage / sqlite.py

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

A new Storage class (ctd.)
--------------------------

.. code-block:: python
    :caption: **Filename:** wiki / storage / sqlite.py

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

.. code-block:: python
    :caption: **Filename:** wiki / webui.py

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


Essential Modules
-----------------

* sys
* os
* os.path
* logging
* datetime, time
* unittest
* pprint
* io
* functools
* collections


Other Interesting Modules
-------------------------

================== ==================
 Modulename         Modulename
================== ==================
 argparse           multiprocessing
 configparser       profile
 csv                pstats
 enum               random
 getpass            shutil
 hashlib            signal
 html               subprocess
 http               tempfile
================== ==================


Common Mistakes
---------------

* Mutable vs. Immutable Objects
* mutable default arguments
* Automatic string concatenation

.. code-block:: bash

    $ python -m timeit "'aaa' 'bbb'"
    $ python -m timeit "'aaa' + 'bbb'"


Advanced Python
===============

TODO
