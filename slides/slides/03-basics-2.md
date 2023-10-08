## Basics++

This chapter covers a few topics beyond the fundamental basics, but which
should nonetheless be understood when developing Python applications.

<!-- .element: class="smaller prose" -->

---

## Exceptions

```py
>>> from example_exception import foo
>>> foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in &lt;module&gt
  File "/path/example_exception.py", line 3, in foo
    return a['z']
KeyError: 'z'
```

<!-- .element: data-caption="Example Exception Output" -->

Note:

- Python’s error-handling mechanism.
- Triggered automatically by Python
- Triggered manually by using `raise`
- Can be caught/handled using a `try/except` block.
- Unhandled exceptions will crash the application.

^

### Manually raising an exception

```py
class MyException(Exception):
   pass

if user_input > 4096:
   raise ValueError("user_input must be smaller than 4096")

raise MyException("Hello World!")
```

<!-- .element: data-caption="Code Sample" -->

Note:

- By default, Python will raise an exception of one of the [builtin
  types](https://docs.python.org/3/library/exceptions.html#exception-hierarchy).
- You can create your own exceptions by subclassing.
- Raising (triggering/throwing) exceptions is done using the `raise` keyword:

^

### Handling Exceptions

```py
from example_exception import foo

try:
   foo()
except KeyError as the_exception:
   # Something bad happened :(
   print(the_exception)
```

<!-- .element: data-caption="Code Sample" -->

Note:

- If not handled, exceptions will crash the application and print a traceback
  on `stderr`.
- They can be handled using a `try/except` block:

When logging, always include the traceback of the exception:

```py
# Manual inclusion of the traceback info
logging.debug(the_exception, exc_info=True)
# Automatic inclusion (log-level will be "critical")
logging.exception('Simple description')
```

The above code-example will include the exception information in the logging
_object_ that is passed to the log _handler_. It is up to the handler to decide
what to do with that object. This means: If the exception information is
included but it does not show up in the logs, it might be the handler who is
ignorning the object.

^

### Demo

See [read-csv-demo-handling-errors.py](fileview.html?filename=code/read-csv-demo-handling-errors.py)

<!-- .element: style="font-size: 50%" -->

- Adding error-handling to the previous CSV code for type-conversions
- Add logging for errors

---

### Logging

```py
import logging
logging.debug("The log message")
logging.info("The log message")
logging.warning("The log message")
logging.error("The log message")
logging.critical("The log message")
```

<!-- .element: data-caption="Code Sample" -->

Note:

The "logging" module provides extremely powerful configuration to deal with
messages throughout your application. You can have multiple loggers and route
messages to various destinations (files, console, network, ...). Each
destination can be configured with different rules (log-level, logger-name, ...)

- Avoid `print()` whenever possible.
- Use `logging` instead

`print()` should only be used when you display text to a user in a CLI
application or when you write to a file.

**For all other cases use the logging module**

When logging inside an exception use the `exc_info=True` argument. This causes
the traceback to be logged for most log-handers. This information is invaluable
when debugging.

---

### Variable Unpacking

^

Assign more than one variable in one statement

```py
# Assign 13 to variable_a, and 'Hello' to variable_b
variable_a, variable_b = 13, 'Hello'
```

^

This works in every place where values are assigned:

```py [1-9|8]
mylist = [
   [1, 2],
   [11, 22]
]

# Each item in the list is another list of two elements each.
# They can be "unpacked" directly in the loop.
for variable_a, variable_b in mylist:
   print(variable_a, variable_b)
```

---

### Enumerating Loops

```py
for i, item in enumerate(mylist):
   print('Item at index %d is: %r' % (i, item))
```

<!-- .element: data-caption="Code Sample" -->

Note:

Keeping a reference to the current iteration number is easy by using the
[enumerate()](https://docs.python.org/3/library/functions.html#enumerate)
function.

Works well in combination with variable unpacking.

Python makes it relatively easy to avoid accessing items by index (see for
example `zip()`). Enumerating lists like this is only needed in rare cases
(calculating progress, logging the current line during text-file processing,
…).

<!-- .element: class="admonition tip smaller" -->

---

# Basic Data Types - 2

---

## Collections

Also on https://docs.python.org/3/library/stdtypes.html

So far we’ve only covered “scalar” values. This chapter covers the most
commonly used “collection” types in Python.

Note:

- A _scalar_ type only contains a single value
- A _collection_ type only contains many values

---

### Lists

```py
mylist = [1, 2, 3, 'hello', 5, 6, True]
mylist[3] == 'hello'
mylist.append('one more value')
```

Note:

- Used for collections with variable length and which have a specific ordering.
- Square brackets `[...]`
- Very similar to arrays in other languages.
- Heterogenuous
- Indexable from both left (`mylist[3]`) and right (`mylist[-3]`).
- Slicing: `mylist[3:7]`
- Mutable:

```py
mylist[2] = new_value
mylist.append(10)
```

---

### Tuples

```py
mytuple = (1, 2, 3, 4, 5, 6, 7)
mytuple[3] == 4
```

Note:

- For collections where _position_ means something. For example 2D-Points.
- Parentheses `()`.
- Like lists, but immutable.
- Hashable (if contents are hashable)
- Recommended alternative: `collections.namedtuple()`

<div class="admonition warning">
Tuple of one element is written as `(value,)`.

Notice the trailing comma. This is a syntax limitation of Python.

A line ending with a comma is also interpreted as tuple!

```py
this_is_a_tuple = (1,)
this_is_also_a_tuple = 1,
```

_Be careful when copy/pasting code!_

</div>

---

### Dictionaries (dicts)

```py
mydict = {"a": 1, "b": 2}
mydict["a"] == 1
```

Note:

- Dictionaries map from one value to another.
- The syntax uses curly braces `{}` and colons `:`
- The behave like Key/Value stores (like `HashTables` in Java or C#)
- Looping over key/values is easy using the `.items()` method:
  ```py
  for key, value in mydict.items():
     ...
  ```
- Starting from Python 3.7, ordering of keys is retained.

Do not rely on ordering behaviour if your application runs in an older Python
environment!

<!-- .element: class="admonition warning" -->

---

### Sets

```py
myset = {1, 2, 3, 4, 5}
my_other_set = {4, 5, 6}

print(myset.intersection(my_other_set))
print(myset.difference(my_other_set))
print(my_other_set.difference(myset))
```

<!-- .element: data-caption="Code Sample" -->

Note:

- Used for collections of variable size with unique values and with no
  particular ordering.
- curly braces `{}`
- [set()](https://docs.python.org/3/library/stdtypes.html#set) can be used to
  convert any iterable to a set (dropping duplicates).
- Useful methods like
  [set.union()](https://docs.python.org/3/library/stdtypes.html#frozenset.union),
  [set.intersection()](https://docs.python.org/3/library/stdtypes.html#frozenset.intersection), …
- If a value is already in the set, adding it again will have no effect.
- _Values must be hashable_

---

## Simple List Processing

- First "real world" program
- Basic Statements & Structures
- Importing & Standatd Library

Note:

For this demo we will be using the file
[collections.csv](fileview.html?filename=code/solutions/collections.csv)

In this file, each entry is split into two lines (Line 1 and line 2 are the
headers).

We will loop over the entries, joining each couple together into one record.
Print the entries nicely formatted to standard output.

At the end of the script, we print out each hobby only once sorted
alphabetically.

[Solution](fileview.html?filename=code/solutions/collections_1.py)

---

<!-- .slide: class="smaller prose" -->

## Data Lookup

- Dictionaries & Lookups
- Sorting
- Text encoding
- String Operations & Formatting

Note:

Sample Data Files: [data.public.lu-sample-2019-03-09.zip](fileview.html?filename=data/data.public.lu-sample-2019-03-09.zip)

- `caclr/TR.DICACOLO.RUCP`: location names in position 120-160,
  ZIP codes in position 200-204. The file uses the `cp1252` encoding
- `rnrpp-code-postal.csv`: contains the number of inhabitants per ZIP
  code.

We will write a program which:

- Reads the data from both files
- Look up the total number of inhabitants for each zip-code
- Sort the list
- Print out a simple table woth location and number of inhabitants
- Sample output is on the following slide

Solution: [zip_code_inhabitants.py](fileview.html?filename=code/zip_code_inhabitants.py)

^

Example Output

```txt
      Luxembourg 120547
Esch-sur-Alzette 35635
       Dudelange 21087
     Differdange 16348
     Schifflange 11184
        Strassen 10503
         Pétange 9506
       Bertrange 9491
     Bettembourg 8995
         Belvaux 8129
```

---

## Bytes \& Collections

- Raw Bytes
- Text Encoding
- Set Operations

Note:

Using the files [data_latin1.csv](fileview.html?filename=code/diff/data_latin1.csv)
and [data_utf8.csv](fileview.html?filename=code/diff/data_utf8.csv), we will write a
function which diffs the two files.

Both lists represent the same data from two different sources. It can be
assumed that each line is unique in each file.

The program will print:

- Which lines are missing in the first file
- Which lines are missing in the second file

Solution: [diff.py](fileview.html?filename=code/diff/app.py)

---

## Pwned Passwords

- HTTP API
- Find password leaks
- Don't send password to cloud service

Note:

In this demo we use a simple _HTTP API_. The API provides a service to find out
if a password was leaked.

To make this safe, we first "hash" the password and then only send a small part
of that has to the remote service. We then receive a list of all _hashes_ that
contain that part. We can then compare our original (full) hash with that
result.

Note that the hash is _already fairly safe_ to submit. By sending only a small
fragment, it is _even safer_.

API documentation: https://haveibeenpwned.com/API/v2#PwnedPasswords

^

#### Boilerplate

```py
from urllib.request import Request, urlopen

def http_get(url):
    """
    Fetch the contents of *url* using a HTTP GET call
    """
    # Headers must be set, otherwise we get a "403 Forbidden" error
    headers = {"User-Agent": "pythontraining/pwdchecker"}
    request = Request(url, headers=headers, method="GET")
    response = urlopen(request)
    data = response.read()
    return data
```

Solution: [pwned_passwords.py](fileview.html?filename=code/solutions/pwned_passwords.py)

Note:

We could also use the third-party library
[`requests`](https://pypi.org/project/requests/) to simplify this.

We use "pure Python" in this example to avoid complexities with packaging &
third-party library dependencies in this "basic" course.

Instead, we provide this simple function to make a simple "HTTP GET" request.

When using _external libraries_ one has to be careful to avoid incompatbilities
between multiple projects. To solve this issue, Python offers [virtual
environments](https://docs.python.org/3/library/venv.html). This makes it
possible to keep the dependencies isolated for each project.

For a more detailed documentation see [Installing
Packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)
in the official documentation. This also explains how to keep your library
requirements in separate files.

---

### Functions Revisited

Until now we have only seen very simple function definitions. This small
chapter discusses a few more advanced techniques which are very useful in most
applications.

---

### Default Arguments

- Functions can have default values for arguments.
- When the function is called, and those arguments are not specified, the
  default value is used:

```py
def hello(name="John"):
    print("Hello %s" % name

hello("Jane")  # Prints "Hello Jane"
hello()  # Prints "Hello John"
```

^

## Warning

**Don’t do this**

```py
def myfunction(names=[]):
    ...
```

**Do this instead**

```py
def myfunction(names=None):
    names = names or []
```

Note:

Never use mutable objects (lists, sets, dictionaries, custom objects, …) as
default values on arguments.

The value (and instance) will be bound to the function when the function
definition is parsed.

## Technical Explanation

Python is an interpreted language. When the code is interpreted (first import),
the default-value for the function arguments is evaluated immediately, and _the
reference to that value is bound to the enclosing scope_.

In this example, the enclosing scope is the module-/file-scope. It is _not_
bound to the inner-scope of the function. Therefore, the value is _not
re-evaluated on each function call!_

In other words: The value is evaluated at function _definition_ time. Not at
function _call_ time.

^

### Passing values into functions

```py
def hello(name, prefix="Hello"): ...
```

This can be called in the following ways:

```py [1|2|3|4|5|1-5]
hello("John")  # by position, using defaults
hello(name="John") # by keyword, using defaults
hello("John", "Goodbye")  # by position
hello(name="John", prefix="Goodbye")  # by keyword
hello(prefix="Goodbye", name="John")  # different order
```

Note:

Providing arguments to functions can be done in two ways:

- positional
- by keywords

---

### Classes Revisited

- Instance Methods
- Class Methods
- Static Methods

^

### Instance Methods

Bound to an _instance_/_object_

```py
class MyClass:

    def my_method(self):
        print(self)  # Prints the string representaion of the current instance

    def my_broken_method():
        # This method will never be callable. Python automatically passes
        # in the instance reference. But because this method does not take
        # any arguments, this will fail.
        pass
```

Note:

When simply defining a method in a function inside a function it becomes an
instance method. Contrary to many other languages, **an instance method receives
a reference to the instance as first argument.**

This argument is - by convention - called `self` in Python. It serves the same
purpose as `this` in languages like Java.

^

### Static Methods

Bound to a _class_

```py
class MyClass:

    @staticmethod
    def my_method():
        return 1

print(MyClass.my_method())
```

Note:

Static methods are prefixed with `@staticmethod`

Static methods are unaware of their instance or class. They do not receive an
additional argument by default.

They are useful to organise code.

^

### Class Methods

Bound to a _class_

```py
class MyClass:

    @classmethod
    def my_method(cls):
        print(cls)  # Prints the string representaion of the current class

class MySubclass(MyClass):
    pass

print(MyClass.my_method())
print(MySubclass.my_method())
```

Note:

Class methods are prefixed with `@classmethod`

Class methods are something fairly unique to Python. They also get a default
argument. But compared to instance methods, this argument will have a reference
to the class! This is particularly useful when subclassing.

They are called like static-methods, but know from which class they were
called. Static methods don't.

By convention this argument is called `cls`.

^

### Abstract Methods

```py
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):

    @abstractmethod
    def mymethod(self):
        raise NotImplementedError('Not yet implemented')


class MyConcreteClass(MyAbstractClass):
    pass
```

Note:

The standard module
[abc](https://docs.python.org/3/library/abc.html#module-abc) (abstract base
classes) can be used to define abstract classes.

They differ in a fundamental way from abstract classes in other (static)
languages: **They are not checked at compile-time. They are checked at
runtime.**
