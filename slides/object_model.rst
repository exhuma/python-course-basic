Python Object Model & Customisation
===================================

Magic Methods
-------------

Reference: `Basic Customisation`_

* ``__str__``, ``__unicode__`` (Python 2 only), ``__bytes__`` (Python 3 Only)
* ``__repr__``
* ``__eq__``, ``__hash__``, ``__lt__``, ``__gt__`` |ell|
* ``__getattr__``, ``__getattribute__``, ``__setattr__``, ``__getitem__``,
  ``__contains__`` |ell|

.. _Basic Customisation: https://docs.python.org/3/reference/datamodel.html#basic-customization

Magic Methods Example
---------------------

.. code-block:: python
    :emphasize-lines: 5-7, 9-11

    class MagicTestA:
        def __init__(self, foo):
            self.foo = foo

        def __str__(self):
            print('__str__ called')
            return self.foo

        def __repr__(self):
            print('__repr__ called')
            return 'MagicTestA(foo=%r)' % self.foo

        def __unicode__(self):
            print('__unicode__ called')
            return self.foo

        def __bytes__(self):
            print('__bytes__ called')
            return self.foo.encode('utf8')

.. nextslide::
    :increment:

.. code-block:: python
    :emphasize-lines: 5-7, 9-11, 13-15

    class MagicTestB:
        def __init__(self, foo):
            self.foo = foo

        def __eq__(self, other):
            print('__eq__ called')
            return other.foo == self.foo

        def __hash__(self):
            print('__hash__ called')
            return hash(('MagicTestB', self.foo))

        def __lt__(self, other):
            print('__lt__ called')
            return self.foo < other.foo

        def __gt__(self, other):
            print('__gt__ called')
            return self.foo > other.foo

.. nextslide::
    :increment:

.. code-block:: python

    class MagicTestC:

        def __getattr__(self, attribute_name):
            print('__getattr__ called')

        def __getattribute__(self, attribute_name):
            print('__getattribute__ called')

        def __setattr__(self, attribute_name, value):
            print('__setattr__ called')

        def __getitem__(self, key):
            print('__getitem__ called')

        def __contains__(self, key):
            print('__contains__ called')


Wiki Page Customisation
-----------------------

.. code-block:: python

    class WikiPage:

        ...

        def __repr__(self):
            return 'WikiPage(%r, %r)' % (self.title, self.content)

        def __str__(self):
            return self.content

        ...

.. nextslide::
    :increment:

.. code-block:: python
    :caption: Before Adding __str__ and __repr__

    >>> from wiki.model import WikiPage
    >>> page = WikiPage('hello', 'Hello World!')
    >>> page
    <wiki.model.WikiPage object at 0x7f34a465d518>
    >>> repr(a)
    '<wiki.model.WikiPage object at 0x7f34a465d518>'
    >>> print(page)
    <wiki.model.WikiPage object at 0x7f34a465d518>
    >>> str(a)
    '<wiki.model.WikiPage object at 0x7f34a465d518>'
    >>> id(page)
    139864073164056
    >>> page.__class__
    <class 'wiki.model.WikiPage'>

.. nextslide::
    :increment:

.. code-block:: python
    :caption: After Adding __str__ and __repr__

    >>> from wiki.model import WikiPage
    >>> page = WikiPage('hello', 'Hello World!')
    >>> page
    WikiPage('hello', 'Hello World!')
    >>> print(page)
    Hello World!
    >>> id(page)
    139864073164056
    >>> page.__class__
    <class 'wiki.model.WikiPage'>

.. note::
    When converting the return value of ``id`` to base 16, you will get the
    same value as shown in the default ``repr`` return value.


