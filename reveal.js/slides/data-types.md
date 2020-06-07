# Basic Data Types

---

## Scalars

See https://docs.python.org/3/library/stdtypes.html

---

### None (NULL)


* Default return value of functions
* Is seen as “false” in a boolean context
* Immutable
* Special instance of the `NoneType` class.
* Singleton.

```py
myvariable = None
```

---

### Strings (text)

* Instances of class [str](https://docs.python.org/3/library/stdtypes.html#str).
* Delimited by one of `'`, `"`, `'''`, `"""`
* Unicode objects, sequence of unicode code-points (in Python3).
* Many useful methods
  * [str.split()](https://docs.python.org/3/library/stdtypes.html#str.split),
    [str.partition()](https://docs.python.org/3/library/stdtypes.html#str.partition),
    [str.strip()](https://docs.python.org/3/library/stdtypes.html#str.strip)
  * [str.startswith()](https://docs.python.org/3/library/stdtypes.html#str.startswith)
  * [str.encode()](https://docs.python.org/3/library/stdtypes.html#str.encode)
  * [str.find()](https://docs.python.org/3/library/stdtypes.html#str.find)
  * [str.isnumeric()](https://docs.python.org/3/library/stdtypes.html#str.isnumeric)
  * …


^


```py
mystring = 'Hello World!'
print(mystring.split())
print(mystring.split('o'))
```

^

### String Literals

* Simple Quotes (`'` and `"`)
* Triple Quotes / Multiline Strings (`'''` and `"""`)
* String-Liteal Prefixes
  * `r` raw-string: All backslash-escapes are ignored. Useful for regular expressions.
  * `f` format-string: Allows embedding of variables
  * `u` unicode (Backwards compatibility for Python 2)

```py
mytext = u"Hello World!"
unescaped = r"This does *not* \n contain a new-line!"
formatted = f'The variable "mytext" contains the value {mytext}'
```

^

### String Formatting

3 Styles, same result:

```py
# “printf”-style formatting
print("Hello %20s %s" % (a, b))

# Formatting “mini-language”
print("Hello {:20s} {}".format(a, b))

# f-Strings
print(f"Hello {a:20s} {b}")
```

See [RealPython Post][1], [printf-style formatting][2] and [format-language][3]
for more information.

[1]: https://realpython.com/python-string-formatting/
[2]: https://docs.python.org/3/library/stdtypes.html#old-string-formatting
[3]: https://docs.python.org/3/library/string.html

---

### Numbers

* Builtin types: [int][6] and [float][7]
* No difference between “long” and “short” integers (handled internally by
  Python). There is also no “double precision” type.
* Support for precise decimal operations ([fractions][1], [decimal][2]).
* Noteworthy modules: [statistics][3], [math][4] and [cmath][5].

[1]: https://docs.python.org/3/library/fractions.html#module-fractions
[2]: https://docs.python.org/3/library/decimal.html#module-decimal
[3]: https://docs.python.org/3/library/statistics.html#module-statistics
[4]: https://docs.python.org/3/library/math.html#module-math
[5]: https://docs.python.org/3/library/cmath.html#module-cmath
[6]: https://docs.python.org/3/library/functions.html#int
[7]: https://docs.python.org/3/library/functions.html#float

^

```py
myint = 42              # type: int
bin_notation = 0b101010 # type: int, base: 2
hex_notation = 0x2a     # type: int, base: 16
octal_notation = 0o52   # type: int, base: 8

myfloat = 3.5           # type: float
myfloat2 = .3           # type: float
sci_notation = 1.3E5    # type: float, value: 130000.0
```

^

### Decimals

Fixed precision numbers

#### Demo

```py
>>> from decimal import Decimal
>>> print(0.1 + 0.2)
?
>>> print(Decimal("0.1") + Decimal("0.2"))
?
```

^

### Fractions

```py
>>> from fractions import Fraction
>>> Fraction(3, 4)
?
>>> Fraction(32, 16)
?
>>> Fraction(3, 4) + Fraction(1, 8)
?
>>> Fraction(3, 4) + Fraction(1, 8) + Fraction(1, 8)
?
>>> Fraction(1, 1) == 1
?
```

^

### Complex Numbers

```py
>>> 3+2j
?
>>> a = 3+2j
>>> a.complex
?
>>> a.imag
?
```

---

### Boolean


Two reserved words:

* `True`
* `False`

They are object instances of type `bool` (subclass of `int`).

```py
my_boolean_a = True
my_boolean_b = False
```

^

### Testing for "Truthy" \& "Falsy" Values

In Python many values are considered as "false" without converting to `bool`
when they are used in a place where a boolean value is expected. The most
common places are if and while blocks.
<!-- .element: class="prose" -->

The value “seen” by Python can be tested by converting it to a boolean using
`bool(value)`. But this conversion is not necessary in production code.
<!-- .element: class="prose" -->

```py
if <here>:
    pass

while <here>:
    pass
```

^

### Values Considered `False`


* `None`
* The numbers `0`, `0.0`, `Decimal('0.0')`
  * <!-- .element: class="smaller" --> Question: What is the output of
    <code>bool(0.1 + 0.2 - 0.3)</code>?
* The empty string `""`
* Empty structures `[]`, `{}`, `set()`
* Any custom object overriding the special `__bool__` method.

---

### Type Conversions

As we have seen, Python has dynamic typing but fairly strict coercion rules. In
English: the same <span class="important">variable</span> can change it’s type
over time. But two <span class="important">values</span> of different types
cannot be easily combined.
<!-- .element: class="prose" -->

In Python some types are compatible for some operations (`int` and `float`) while
others are not (`str` and `int` for addition).
<!-- .element: class="prose" -->

^

### Explicit Conversion

When a user enters numeric values from the keyboard (or if read from a CSV
file), they are seen as strings and must be converted to numeric values:
<!-- .element: class="prose" -->

```py
value_str = input('Please enter a number:')
value_int = int(value_str)
print(value_int + 10)
```

Probably the most common conversions you will encounter are: `int`, `str`,
`float`, `bytes`.
<!-- .element: class="prose" -->

^

### Implicit Conversion

Some values are compatible for some operations. The resulting type depends on
the operation:

```py
>>> type(10 * 3.14)
float
>>> type('a' * 3)
str
>>> type(['a'] * 3)
list
```

---

# The Standard Library

---

<!-- .slide: class="prose" -->

### Python comes with “batteries included”

The [standard library][1] of Python comes with many useful features. This makes
it possible to write many useful applications without third-party (external)
libraries.

* Standard Library modules are also imported using the `import` statement.
* Standard Library modules take precedence in imports (Use relative imports on
  name-conflicts). See [PEP 328][2].

[1]: https://docs.python.org/3/library/
[2]: https://www.python.org/dev/peps/pep-0328

^

#### Essential Modules

^

`os`

Operating System details. Contains values which are different on
Windows/Linux/MacOS like path \& folder separators.
<!-- .element: class="prose" -->

Also contains access to environment variables & general operating-system
information.
<!-- .element: class="prose" -->

^

`os.path` \& `pathlib`

Helper functions to deal with file- and folder-names. Contains helpers to
manipulate filenames, converting them from/to absolute files, adding/removing
path elements from names, e.t.c.
<!-- .element: class="prose" -->

`pathlib` was only introduced in Python 3.4
<!-- .element: class="prose" -->

^

`logging`

Fully featured logging system inspired by `log4j`. Very easy for simple setups,
but can also handle very complex needs:
<!-- .element: class="prose" -->

* Log to rotating files
<!-- .element: class="prose" -->
* Log to the console
<!-- .element: class="prose" -->
* Log to a remote UDP/TCP destination (Logstash, Splunk, syslog, ...)
<!-- .element: class="prose" -->
* ...
<!-- .element: class="prose" -->

^

`json`

Simple helpers for parsing and creating JSON documents.
<!-- .element: class="prose" -->

^

`datetime` \& `time`

Helpers for date/time processing.
<!-- .element: class="prose" -->

**Important**: Timezone data is kept outside of the stdlib in the module
[pytz][1].  This allows faster updates than the normal release cycle of Python.
<!-- .element: class="prose" -->

[1]: https://pypi.org/project/pytz/

---

#### Notable Modules

^

`argparse`

Allows creating simple to complex parsers for CLI argument handling (successor
of both `optparse` and `getopt`).
<!-- .element: class="prose" -->

^

`gettext`

Support for multilingual translations with decoupled translations from
source-code using the well-known GNU
[gettext](https://www.gnu.org/software/gettext/) system.
<!-- .element: class="prose" -->

^

`tempfile`

Support for creating temporary files securely.
<!-- .element: class="prose" -->

^

`sqlite3`

Support for structured persistent data storage without a DB server.
<!-- .element: class="prose" -->

^

`configparser`

Support for working with `.ini` files.
<!-- .element: class="prose" -->

^

`hashlib`

Support for calculating common hashes (`md5`, `sha1`, …)
<!-- .element: class="prose" -->


---

## The CSV module

^

The csv module makes it easy to read delimited data. It also deals with:

* quoted values
* multiline values
* escaped characters

^

### Example

```py
import csv


infile = open('data.csv')
reader = csv.reader(infile, delimiter=';')
for row in reader:
    print(row)
```

^

<!-- .slide: class="prose smaller" -->

#### Demo

We will write a new function `read_data` that takes a filename as argument. The
file [csv3.csv](/data/csv3.csv) can be used as example. The function will do
the following:

* Open the file with the given filename
* Initialise a new variable named output as empty list.
* Create a CSV reader with the opened file object
* Loop through each line and do the following:
  * Convert each numerical column into an appropriate type (f.ex.: use
    `decimal.Decimal` for monetary values).
  * Split the 7 th column (index 6) into a list of strings.
  * Add a new column at the end which contains the MD5 hex-digest of the whole
    line, values only (see `hashlib.md5()`).
    * MD5 sums can only be calculated on bytes (not strings)
  * Append the new columns to the `output` list
* After the loop, return the list `output`
