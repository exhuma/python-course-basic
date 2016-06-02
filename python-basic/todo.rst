..          ┌─ (*) essential, (**) basic, (***) advanced
..          │   ┌─ doc
..          │   │ ┌─ code example
..          │   │ │
.. TODO   1 *       data types -> Boolean, String (&literals), Bytes, Numbers, Lists, Tuples, Dictionaries, Sets
.. TODO   2 *       Falsy values
.. TODO  32 *       defining functions
.. TODO  33 *       defining classes
.. TODO   3 *       ``in`` operator
.. TODO   4 *   x x ``None``
.. TODO   5 *       Slicing
.. TODO   6 *       String formatting
.. TODO   7 **      Variable Unpacking
.. TODO   8 *       imports
.. TODO  10 *       Docstrings
.. TODO  11 **         └─everything is an object (__doc__ of function)
.. TODO  12 *       raising and catching exceptions
.. TODO  24 **      Essential modules: os, sys, ... (sys.stderr, out, in)
.. TODO  14 **  d c *args, *, **kwargs
.. TODO  15 *** d c iterators and generators
.. TODO  16 **  d c comprehensions (list, set & dict), generator expressions
.. TODO  17 *** d c decorators
.. TODO  18 *** d c sys.path
.. TODO  19 **      Packaging
.. TODO  20 **  d c "magic" Variables and attributes
.. TODO  21 **  d c logging
.. TODO  23 **      DBAPI2
.. TODO  25 *       PEPs
.. TODO  26 *       REs
.. TODO  27 *       with statement (context managers)
.. TODO  28 *   d c sorting lists
.. TODO  29 **  d c unit tests
.. TODO  30 *** d c lambda
.. TODO  31 *   d c ReST & Pygments
.. TODO  34 **  d c ABCs
.. TODO  35 **  d c Class Customisation

.. TODO PEP8
.. TODO   9 *   d c line continuations and parens


Code Samples
------------

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


Extension Modules
-----------------

SQLAlchemy
~~~~~~~~~~

xlrd
~~~~

Requests
~~~~~~~~

Click
~~~~~

Alembic
~~~~~~~

