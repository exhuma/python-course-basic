.. SQLAlchemy {{{

.. http://www.slideshare.net/mengukagan/an-introduction-to-sqlalchemy
.. https://www.youtube.com/watch?v=P141KRbxVKc&t=2h58m
.. TODO -> Read about "leaky abstraction"
.. TODO Add architecture graph, explain the elements.
.. SA Unit Testing: http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html#joining-a-session-into-an-external-transaction-such-as-for-test-suites
.. transactions (engine is in autocommit vs UOW)

.. |ell| raw:: html

   …

Databases
=========

.. {{{ DBAPI2

DBAPI-2
-------

* `PEP-0249`_
* Default Database Interface spec.
* Loose spec.
* Raw SQL, few abstractions.

.. note::
    While the spec standardises many concepts, there are still some substantial
    differences between the different implementations. Most prominent is the
    difference between value placeholders (``?``, ``%s``, ``:varname``, |ell|).

.. _PEP-0249: https://www.python.org/dev/peps/pep-0249/


.. }}}

SQLAlchemy
----------

* **The** DB Toolkit for Python.
* Abstraction over DBAPI-2
* Separated into:

  * **ORM** *(focus of this introduction)*
  * Expression Language
  * Metadata
  * Core

* Helps DB development at any level.
* Consistent API across DB engines (|ell| ehm |ell|)

.. note::
    While the *API* is consistent, you still have to decide whether to use DB
    specific concepts. For example, PostgreSQL has many advanced data types
    (Geometric Types, IP-Addresses, Arrays, |ell|). These data types may not be
    available on other databases. It is a tradeoff between being portable, and
    leveraging database features.


ORM Advantages / Disadvantages
------------------------------

* No need to index columns.
* Method chaining for adding filters (``WHERE``).
* Less SQL to write.


Example Mapping
---------------

::

    from sqlalchemy import String, Unicode
    from sqlalchemy.ext.declaratvie import Base

    class User(Base):
        __tablename__ = 'user'

        email = String(primary_key=True)
        name = Unicode()
        telephone_number = String()

.. note::
    "Declarative" was implemented as SQLAlchemy *extension*. It has since
    become the de-facto standard for defining domain models together with data
    models. You can still use the "classical" way of mapping classes, in case
    your domain model does not directly map to the data model.

    In classical mapping, definition of tables, and objects is competely
    separate. It can for example be used to map an already existing domain
    model to a DB without touching the existing codebase.

    Both approaches can also be used together without problem.


Reflection (Introspection)
--------------------------

::

    class User(Base):
        __tablename__ = 'user'
        __table_args__ = {
            'autoload': True
        }

See `table configuration`_

.. _table configuration: http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/table_config.html

.. note::
    Reflection can be extremely useful if you already have an existing DB. The
    downside is however, that your application may break if the Database
    changes. But that may even happen if you *don't* use reflection! So it's
    fairly safe to use.


The Session
-----------

* implements the well known `Unit of Work`_ pattern.
* Holds objects in different states (the Lifecycle):

  *transient*
    The object has been newly created (exists in memory) and is not yet in the
    session.

  *pending*
    The object is changed in memory but that has not yet been flushed to the
    database.

  *persistent*
    The object exists in memory and changes have been recorded to the database.

  *detached*
    The object exists in memory, but is no longer attached to the database.


.. _Unit of Work: http://martinfowler.com/eaaCatalog/unitOfWork.html


Querying
--------

* ``session.query(User)`` creates a basic ``SELECT`` query without filters or
  orderings (``SELECT * FROM user``).
* ``query = query.filter(User.name == 'John')`` creates a new query with an
  added ``WHERE`` clause.
* ``query = query.filter(or_(User.name == 'John', User.name == 'Jane'))``.
* Calls to query methods (``.filter()``, ``.order()``, ``.group_by``, |ell|)
  can be chained. They usually do not modify an existing query object.






* Reflection Table(autoload=True, autoload_with)
  * Inspector
* Alembic
* SQL
  x + 10
  x + 'hello'
  * Bound placeholders
    expr = x.c.name == 10
    compiled = expr.compile(<dialect>)
    compiled.params
* Object Identity (identity map)::

  >>> a = User(name='john')
  >>> b = session.query(User).first()
  >>> a is b
  True


* Session.new
* Session.dirty
* Flush & Commit
* After commit, all objects are expired (can be turned off).
* ORM query indexing/slicing
* filter (full-blown) vs filter_by (less typing)
* all, first, one (multiple, none)
* Not opinionated about existing schema. Not enforcing anything.
* Custom Base Classes / Mixins
* ORM events
* ORMs (in general) synchronize primary keys with corresponding foreign keys
* Once data is loaded in memory it will not reloaded (unless explicitly specified, or session closed/committed).
* Default = Connection Pool, Can be used without one.
* Use objects instead of FKs when working with relationships (works both ways, but when editing FKs, the ORM will be unaware). Will get complicated if you cannot commit the TX mid-way.
* N+1 Problem
  * subqueryload
  * joinedload
  * contains_eager

.. My History {{{

My History
----------

Python - SQLObject
Java Oracle Toplink
Java Eclipselink
Java Hibernate
Java JPA
PHP PDO
PHP mDB2
PHP Doctrine (-)
.NET ADO

.. }}}

Installation
------------

SQLAlchemy installs just like any other third party module in Python::

    pip install sqlalchemy

You do however need the proper DB library installed as well if it is not
included in the standard library (for example for PostgreSQL)::

    pip install psycopg2

* No imposed standards (like "id" column).
* ORM & Expression Language
* Connection Pooling & Lazy Connections
* primary key needed in ORM
* Creating
* Selecting (one/first)
* Lifecycle - transient - pending - persistent - detached
* Lazy/Eager Loading (relationships)
* Joins
* To map a table it must be at least 1NF
* alembic instead of ``create_all``
http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html

.. }}}

.. {{{ Unit Testing

* Writing Unit Tests
* Test Runners
  * builtin
  * py.test
  * nose
* Mocking

.. }}}

.. Debugging {{{
* Understanding Stack-Traces
* The code of the Standard Library
* pdb
* ipdb
* winpdb
* remote debugging

References
----------

* https://wiki.python.org/moin/PythonDebuggingTools

.. }}}

.. vim: set fdm=marker foldlevel=0:
