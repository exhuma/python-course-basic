..          ┌─ (*) essential, (**) basic, (***) advanced
..          │   ┌─ doc
..          │   │ ┌─ code example
..          │   │ │
.. TODO   1 *       data types -> Boolean, String (&literals), Bytes, Numbers, Lists, Tuples, Dictionaries, Sets
.. TODO   2 *       Falsy values
.. TODO  32 *       defining functions
.. TODO  33 *       defining classes
.. TODO   3 *   d c ``in`` operator
.. TODO   4 *   x x ``None``
.. TODO   5 *       Slicing
.. TODO   6 *   d c String formatting
.. TODO   7 **    c Variable Unpacking
.. TODO   8 *   d   imports
.. TODO   9 *   d c line continuations and parens
.. TODO  10 *   d c Docstrings
.. TODO  11 **  d c    └─everything is an object (__doc__ of function)
.. TODO  12 *   d c raising and catching exceptions
.. TODO  13 *   d c Use // ** and % for numbers
.. TODO  14 **  d c *args, *, **kwargs
.. TODO  15 *** d c iterators and generators
.. TODO  16 **  d c comprehensions (list, set & dict), generator expressions
.. TODO  17 *** d c decorators
.. TODO  18 *** d c sys.path
.. TODO  19 **  d   Packaging & Virtualenv
.. TODO  20 **  d c "magic" Variables and attributes
.. TODO  21 **  d c logging
.. TODO  22 **  d c MySQL on Python 3
.. TODO  23 **  d   DBAPI2
.. TODO  24 **  d c Essential modules: os, sys, ... (sys.stderr, out, in)
.. TODO  25 *   d   PEPs
.. TODO  26 *   d c REs
.. TODO  27 *   d c with statement (context managers)
.. TODO  28 *   d c sorting lists
.. TODO  29 **  d c unit tests
.. TODO  30 *** d c lambda
.. TODO  31 *   d c ReST & Pygments
.. TODO  34 **  d c ABCs
.. TODO  35 **  d c Class Customisation


Code Samples
------------

argparse
~~~~~~~~

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

