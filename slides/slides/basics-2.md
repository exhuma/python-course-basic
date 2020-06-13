## Basics++

This chapter covers a few topics beyond the fundamental basics, but which
should nonetheless be understood when developing Python applications.
<!-- .element: class="smaller prose" -->

---

## Exceptions

<!-- .slide: class="prose" -->

* Python’s error-handling mechanism.
* Triggered automatically by Python
* Triggered manually by using `raise`
* Can be caught/handled using a `try/except` block.
* Unhandled exceptions will crash the application.

^

An example exception:

```py
>>> from example_exception import foo
>>> foo()
Traceback (most recent call last):
  File "&lt;stdin&gt", line 1, in &lt;module&gt
  File "/path/example_exception.py", line 3, in foo
    return a['z']
KeyError: 'z'
```

^

### Manually raising an exception

* By default, Python will raise an exception of one of the [builtin
  types](https://docs.python.org/3/library/exceptions.html#exception-hierarchy).
* You can create your own exceptions by subclassing.
* Raising (triggering/throwing) exceptions is done using the `raise` keyword:

```py
class MyException(Exception):
   pass

if user_input > 4096:
   raise ValueError('user_input must be smaller than 4096')
raise MyException('Hello World!')
```

^

### Handling Exceptions


* If not handled, exceptions will crash the application and print a traceback
  on `stderr`.
* They can be handled using a `try/except` block:

```py
from example_exception import foo

try:
   foo()
except KeyError as the_exception:
   # Something bad happened :(
   print(the_exception)
```

Always log the traceback of an exception using either
`logging.debug(the_exception, exc_info=True)` or `logging.exception('Simple
description')`.
<!-- .element: class="admonition tip smaller" -->

---

### Logging

* Use `print()` only if you display text to a user in a CLI application or if
  you write to a file.
* **For all other cases use the logging module**
* When logging inside an exception use the `exc_info=True` argument. This cases
  the traceback to be logged and can be invaluable when debugging:

```py
logging.debug('The error message', exc_info=True)
```

^

### Demo

* Adding error-handling to the previous CSV code for type-conversions
* Add logging for errors

---

### Variable Unpacking

Python can assign more than one value in one statement:

```py
# Assign 13 to variable_a, and 'Hello' to variable_b
variable_a, variable_b = 13, 'Hello'
```

This work in every place where values are assigned:

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

<!-- .slide: class="prose" -->

Keeping a reference to the current iteration number is easy by using the
[enumerate()](https://docs.python.org/3/library/functions.html#enumerate)
function.

In combination with variable unpacking loops can be written as:

```py
for i, item in enumerate(mylist):
   print('Item at index %d is: %r' % (i, item))
```

Python makes it relatively easy to avoid accessing items by index (see for
example `zip()`). Enumerating lists like this only needed in rare cases
(calculating progress, logging the current line during text-file processing,
…).
<!-- .element: class="admonition tip smaller" -->


---

### Basic Data Types - 2

#### Collections

Also on https://docs.python.org/3/library/stdtypes.html
<!-- .element: class="prose smaller" -->

So far we’ve only covered “scalar” values. This chapter covers the most
commonly used “collection” types in Python.
<!-- .element: class="prose smaller" -->

---

### Lists

```py
mylist = [1, 2, 3, 'hello', 5, 6, True]
mylist[3] == 'hello'
mylist.append('one more value')
```

^

* Used for collections with variable length and which have a specific ordering.
* Square brackets `[...]`
* Very similar to arrays in other languages.
* Heterogenuous
* Indexable from both left (`mylist[3]`) and right (`mylist[-3]`).
* Slicing: `mylist[3:7]`
* Mutable:

```py
mylist[2] = new_value
mylist.append(10)
```

---

### Bytes

```py
data = b'H\xc3\xa9llo World'
```
^

* Builtin type: `bytes`.
* byte-literals look just like strings, but with a `b` prefix:
* Immutable (for byte-operations see `bytearray`).

^

Almost identical API to strings. The key differences are:

* Bytes almost always come “from the outside world” (hard-disk, network, …)
* Strings are almost always meant to be read by a human (bytes not so much).
* Bytes can only be “decoded” into strings
* Strings can only be “encoded” into bytes

^

Bytes are (generally) used to talk to machines:

  * Write data to files
  * Send data over a network socket

^

String are used to be displayed to a human user:

  * Text on a button label
  * CLI output, HTML content
  * …

^

#### Rule of Thumb

For text, as long as the value remains held by variables, use normal
string-literals (unicode objects). As soon as the value crosses the memory/io
boundary (network, disk) it needs to be encoded to bytes or decoded to string.

---

### Tuples

```py
mytuple = (1, 2, 3, 4, 5, 6, 7)
mytuple[3] == 4
```

^

* For collections where *position* means something
* Parentheses `()`
* Like lists, but immutable.
* Hashable (if contents are hashable)
* Recommended alternative: `collections.namedtuple()`

^

#### Note

Tuple of one element

```py
myvalue = (1,)
```

---

### Dictionaries (dicts)

```py
mydict = {"a": 1, "b": 2}
mydict["a"] == 1
```

^

* Used to map from one value to another.
* Curly braces `{}` and colons `:`
* Key/Value stores (Like `HashTables` in Java or C#)
* Looping over key/values is easy using:
  ```py
  for key, value in mydict.items():
     ...
  ```
* Starting from Python 3.7, ordering of keys is retained.

^

#### Warning

Do not rely on ordering behaviour if your application runs in an older Python
environment!
<!-- .element: class="admonition warning" -->


---

### Sets

```py
myset = {1, 2, 3, 4, 5}
```

^

* Used for collections of variable size with unique values and with no
  particular ordering.
* curly braces `{}`
* [set()](https://docs.python.org/3/library/stdtypes.html#set) can be used to
  convert any iterable to a set (dropping duplicates).
* Useful methods like
  [set.union()](https://docs.python.org/3/library/stdtypes.html#frozenset.union),
  [set.intersection()](https://docs.python.org/3/library/stdtypes.html#frozenset.intersection), …
* If a value is already in the set, adding it again will have no effect.
* Values must be hashable

---

# Demo

---

<!-- .slide: class="prose" -->

#### Simple List Processing

For this demo we will be using the file
[collections.csv](data/collections.csv).

In this file, each entry is split into two lines (Line 1 and line 2 are the
headers).

We will loop over the entries, joining each couple together into one record.
Print the entries nicely formatted to standard output.

At the end of the script, we print out each hobby only once sorted
alphabetically.

---

<!-- .slide: class="smaller prose" -->

#### Data Lookup

Sample Data Files: [data.public.lu-sample-2019-03-09.zip](data/data.public.lu-sample-2019-03-09.zip)

* The file `caclr/TR.DICACOLO.RUCP` contains location names in position 120-160
  and ZIP codes in position 200-204. The file uses the `cp1252` encoding
* The file `rnrpp-code-postal.csv` contains the number of inhabitants per ZIP
  code.

We will write a program which:

* Reads the data from both files
* For each ZIP-code per location, look up the number of inhabitants and calculate the sum
* Sort the list by descending number of inhabitants
* Print out the location name and number of inhabitants of the top 10 items using 30 characters for the location, right aligned.
* Sample output is on the following slide

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

#### Bytes \& Collections
<!-- .slide: class="prose" -->

Using the files [data_latin1.csv](data/data_latin1.csv) and
[data_utf8.csv](data/data_utf8.csv), we will write a function which diffs the
two files.

Both lists represent the same data from two different sources. It can be
assumed that each line is unique in each file.

The program will print:

* Which lines are missing in the first file
* Which lines are missing in the second file

---

#### Pwned Passwords

<!-- .slide: class="prose" -->

**Goal:** Find out if a password was ever leaked by an attack without sending
the password to a remote API.

API docs: https://haveibeenpwned.com/API/v2#PwnedPasswords

^

#### Boilerplate

NB: We could also use the third-party library `requests` to simplify
this.

```py
from urllib.request import Request, urlopen

def http_get(url):
    '''
    Fetch the contents of *url* using a HTTP GET call
    '''
    # Headers must be set, otherwirse we get a "403 Forbidden" error
    headers = {'User-Agent': 'pythontraining/pwdchecker'}
    request = Request(url, headers=headers, method='GET')
    response = urlopen(request)
    data = response.read()
    return data
```

---

### Functions Revisited

Until now we have only seen very simple function definitions. This small
chapter discusses a few more advanced techniques which are very useful in most
applications.
<!-- .element: class="prose smaller" -->

---

### Default Arguments

* Functions can have default values for arguments.
* When the function is called, and those arguments are not specified, the
  default value is used:

```py
def hello(name="John"):
    print("Hello %s" % name

hello("Jane")  # Prints "Hello Jane"
hello()  # Prints "Hello John"
```

^

#### Warning

Never use mutable objects (lists, sets, dictionaries, custom objects, …) as
default values on arguments.

The value (and instance) will be bound to the function when the function
definition is parsed.

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

^

### Passing values into functions

Providing arguments to functions can be done in two ways: positional and by
keywords. Consider this function signature:

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

---

### Classes Revisited

"Instance Methods", "Class Methods" and "Static Methods"

^

### Instance Methods

<!-- .slide: class="prose" -->

When simply defining a method in a function inside a function it becomes an
instance method. Contrary to many other languages, **an instance method receives
a reference to the instance as first argument.**

This argument is - by convention - called `self` in Python. It serves the same
purpose as `this` in languages like Java.

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

^

### Static Methods
<!-- .slide: class="prose" -->

Static methods are prefixed with `@staticmethod`

Static methods are unaware of their instance or class. They do not receive an
additional argument by default.

They are useful to organise code.

```py
class MyClass:

    @staticmethod
    def my_method():
        return 1

print(MyClass.my_method())
```

^

### Class Methods
<!-- .slide: class="prose" -->

Class methods are prefixed with `@classmethod`

Class methods are something fairly unique to Python. They also get a default
argument. But compared to instance methods, this argument will have a reference
to the class! This is particularly useful when subclassing.

They are called like static-methods, but know from which class they were
called. Static methods don't.

By convention this argument is called `cls`.

```py
class MyClass:

    @classmethod
    def my_method(cls):
        print(cls)  # Prints the string representaion of the current class
```

^

### Abstract Methods
<!-- .slide: class="smaller prose" -->

The standard module
[abc](https://docs.python.org/3/library/abc.html#module-abc) (abstract base
classes) can be used to define abstract classes.

They differ in a fundamental way from abstract classes in other (static)
languages: **They are not checked at compile-time. They are checked at
runtime.**

```py
from abc import ABCMeta, abstractmethod

class MyAbstractClass(metaclass=ABCMeta):

    @abstractmethod
    def mymethod(self):
        raise NotImplementedError('Not yet implemented')
```
