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
