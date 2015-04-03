..      ┌─ (*) essential, (**) basic, (***) advanced
..      │   ┌─ doc
..      │   │ ┌─ code example
..      │   │ │
.. TODO *   d c Falsy values
.. TODO *   d c ``in`` operator
.. TODO *   d c ``None``
.. TODO *     c Slicing
.. TODO *     c data types -> Boolean, String, Bytes, Numbers, Lists, Tuples, Dictionaries, Sets
.. TODO *   d c String literals and formatting
.. TODO **    c Variable Unpacking
.. TODO *   d   imports
.. TODO *   d c line continuations and parens
.. TODO *   d   How to get help (repl: help(), pydoc, docs.python.org) -> Use ``help`` on any object.
.. TODO *   d c Docstrings
.. TODO **  d c    └─everything is an object (__doc__ of function)
.. TODO *   d c raising and catching exceptions
.. TODO *   d c Use // ** and % for numbers
.. TODO **  d c *args, *, **kwargs
.. TODO *** d c iterators and generators
.. TODO **  d c comprehensions (list, set & dict), generator expressions
.. TODO *** d c decorators
.. TODO *** d c sys.path
.. TODO **  d   Packaging & Virtualenv
.. TODO **  d c "magic" Variables and attributes
.. TODO **  d c logging
.. TODO **  d c MySQL on Python 3
.. TODO **  d   DBAPI2
.. TODO **  d c Essential modules: os, sys, ... (sys.stderr, out, in)
.. TODO *   d   PEPs
.. TODO *   d c REs
.. TODO *   d c with statement (context managers)
.. TODO *   d c sorting lists
.. TODO **  d c unit tests
.. TODO *** d c lambda
.. TODO *   d c ReST & Pygments


Code Samples
------------

csv
~~~

A module to easily read and write CSV files.

.. code::
    :language: python

    from csv import Reader
    reader = Reader(open('filename'))
    for row in reader:
        print ' '.join(row)


    writer = Writer(open('output.csv', 'w'))
    data = [
        ('a', 'b', 'c'),
        (1, 1, 1),
        (1, 2, 3)
    ]
    for row in data:
        writer.writerow(data)

cmd
~~~

A module to write interactive console applications.

.. code::
    :language: python

    from cmd impot Cmd
    class MyApp(Cmd):

        DATA = [
            'foo',
            'bar',
            'baz'
        ]


        def do_hello(self, line):
            '''
            Prints out "Hello World"
            '''
            print('Hello World')

        def do_ls(self, line):
            '''
            Lists current data
            '''
            print('\n'.join(self.DATA))

        def do_append(self, line):
            '''
            Adds a new element to the stored data.
            '''
            self.DATA.append(line)


    if __name__ == '__main__':
        app = MyApp()
        MyApp.run()


json
~~~~

Easily read and write JSON documents.

.. code::
    :language: python

    from json import load, dump
    data = load(open('myfile.json'))
    newdata = {
        "key": "value"
    }

    dump(newdata, open('filename', 'w'))



collections
~~~~~~~~~~~


Extension Modules
-----------------

SQLAlchemy
~~~~~~~~~~

Flask
~~~~~

xlrd
~~~~

Requests
~~~~~~~~

Click
~~~~~

Alembic
~~~~~~~

