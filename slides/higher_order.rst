Higher Order Functions
======================

"Higher Order Functions" are functions that operate on functions. They can
either modify existing functions or generate functions.

Simple Example: Creating Functions
----------------------------------

.. code-block:: python

    def multiplicator(n):
        def fun(m):
            return n*m
        return fun

    times2 = multiplicator(2)
    times3 = multiplicator(3)
    times2(2)
    times3(2)


Simple Example: Modifying Functions
-----------------------------------

.. code-block:: python

    from datetime import datetime

    def timed(f):
        def fun(*args, **kwargs):
            begin = datetime.now()
            result = f(*args, **kwargs)
            runtime = datetime.now() - begin
            print('Runtime of %s: %s' % (f, runtime))
            return result
        return fun

    def hello():
        print("Hello World")

    timed_hello = timed(hello)

    hello()
    timed_hello()
