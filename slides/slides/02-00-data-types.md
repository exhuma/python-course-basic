# Basic Data Types

---

## Scalars

See https://docs.python.org/3/library/stdtypes.html

---

### None (NULL)

```py
myvariable = None
```

<!-- .element: data-caption="Code Sample" -->

Note:

- Default return value of functions
- Is seen as “false” in a boolean context
- Immutable
- Special instance of the `NoneType` class.
- Singleton.

---

### Strings (text)

```py
mystring = "Hello World!"
print(mystring.split())
print(mystring.split("o"))
```

<!-- .element: data-caption="Code Sample" -->

Note:

- Instances of class [str](https://docs.python.org/3/library/stdtypes.html#str).
- Delimited by one of `'`, `"`, `'''`, `"""`
- Unicode objects, sequence of unicode code-points (in Python3).
- Many useful methods
  - [str.split()](https://docs.python.org/3/library/stdtypes.html#str.split),
    [str.partition()](https://docs.python.org/3/library/stdtypes.html#str.partition),
    [str.strip()](https://docs.python.org/3/library/stdtypes.html#str.strip)
  - [str.startswith()](https://docs.python.org/3/library/stdtypes.html#str.startswith)
  - [str.encode()](https://docs.python.org/3/library/stdtypes.html#str.encode)
  - [str.find()](https://docs.python.org/3/library/stdtypes.html#str.find)
  - [str.isnumeric()](https://docs.python.org/3/library/stdtypes.html#str.isnumeric)
  - …

^

### String Literals & Prefixes

```py
# Unicode-Text (only required in Python 2)
mytext = u"Hello World!"

# Raw string (disables escape sequences)
unescaped = r"This does *not* \n contain a new-line!"

# Embedded Variables (f-strings)
formatted = f'The variable "mytext" contains the value {mytext}'
```

<!-- .element: data-caption="Code Sample" -->

Note:

- Simple Quotes (`'` and `"`)
- Triple Quotes / Multiline Strings (`'''` and `"""`)
- String-Liteal Prefixes
  - `r` raw-string: All backslash-escapes are ignored. Useful for regular expressions.
  - `f` format-string: Allows embedding of variables
  - `u` unicode (Backwards compatibility for Python 2)

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

Note:

See [RealPython Post][1], [printf-style formatting][2] and [format-language][3]
for more information.

[1]: https://realpython.com/python-string-formatting/
[2]: https://docs.python.org/3/library/stdtypes.html#old-string-formatting
[3]: https://docs.python.org/3/library/string.html

---

### Bytes

```py
data = b'H\xc3\xa9llo World'
```

Note:

- Builtin type: `bytes`.
- byte-literals look just like strings, but with a `b` prefix:
- Immutable (for byte-operations see `bytearray`).

Bytes are almost identical API to strings. The key differences are:

- Bytes almost always come “from the outside world” (hard-disk, network, …)
- Strings are almost always meant to be read by a human (bytes not so much).
- Bytes can only be “decoded” into strings
- Strings can only be “encoded” into bytes

Bytes are (generally) used to talk to machines:

- Write data to files
- Send data over a network socket

String are used to be displayed to a human user:

- Text on a button label
- CLI output, HTML content
- …

Use normal strings for text, as long as the value remains held by variables. As
soon as the value _crosses the memory/io boundary_ (network, disk) it needs to
be encoded to bytes or decoded to string.

<!-- .element: class="admonition tip" -->

---

### Numbers

```py
myint = 42                  # type: int
for_readability = 1_000_000 # type: int, value: 1000000
bin_notation = 0b101010     # type: int, base: 2
hex_notation = 0x2a         # type: int, base: 16
octal_notation = 0o52       # type: int, base: 8

myfloat = 3.5               # type: float
myfloat2 = .3               # type: float
sci_notation = 1.3E5        # type: float, value: 130000.0
```

<!-- .element: data-caption="Code Sample" -->

Note:

- Builtin types: [int][6] and [float][7]
- No difference between “long” and “short” integers (handled internally by
  Python). There is also no “double precision” type.
- Support for precise decimal operations ([fractions][1], [decimal][2]).
- Noteworthy modules: [statistics][3], [math][4] and [cmath][5].

[1]: https://docs.python.org/3/library/fractions.html#module-fractions
[2]: https://docs.python.org/3/library/decimal.html#module-decimal
[3]: https://docs.python.org/3/library/statistics.html#module-statistics
[4]: https://docs.python.org/3/library/math.html#module-math
[5]: https://docs.python.org/3/library/cmath.html#module-cmath
[6]: https://docs.python.org/3/library/functions.html#int
[7]: https://docs.python.org/3/library/functions.html#float

^

### Decimals

```py
>>> from decimal import Decimal
>>> print(0.1 + 0.2)
?
>>> print(Decimal("0.1") + Decimal("0.2"))
?
```

<!-- .element: data-caption="REPL Demo" -->

Note:

Decimals guarantee precision in calculations.

With "floating point" numbers, some errors are normal for every language due to
hardware implementation and they should not be used for financial operations.
Decimals are internally represented as integers and don't suffer from this issue
at the expense of performance.

<!-- .element: class="admonition warning" -->

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

<!-- .element: data-caption="REPL Demo" -->

Note:

Fractions offer helpful methods like `numerator` and `denominator`. They also
automatically simplify values where appropriate.

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

<!-- .element: data-caption="REPL Demo" -->

Note:

While not widely useful outside of scientific settings, it is an interesting
tidbit to know that complex numbers are natively supported by Python.

---

### Boolean

```py
my_boolean_a = True
my_boolean_b = False
```

<!-- .element: data-caption="Code Sample" -->

Note:

Two reserved words:

- `True`
- `False`

They are object instances of type `bool` (subclass of `int`).

^

### Testing for "Truthy" \& "Falsy" Values

```py
if <here>:
    pass

while <here>:
    pass
```

<!-- .element: data-caption="Code Sample" -->

Note:

In Python many values are considered as "false" without converting to `bool`.
When they are used in a place where a boolean value is expected, Python
_implicitly_ converts them to a boolean first. The most common places are `if`
and `while` blocks.

The value “seen” by Python can be tested by converting it to a boolean using
`bool(value)`. But this conversion is not necessary in production code.

### Values Considered `False`

- `None`
- The numbers `0`, `0.0`, `Decimal('0.0')`
  - _Question:_ What is the output of <code>bool(0.1 + 0.2 - 0.3)</code>?
- The empty string `""`
- Empty structures `[]`, `{}`, `set()`
- Any custom object overriding the special `__bool__` method.

---

### Type Conversions

As we have seen, Python has dynamic typing but fairly strict coercion rules. In
English: the same _variable_ can change it’s type over time. But two _values_ of
different types cannot be easily combined.

In Python some types are compatible for some operations (`int` and `float`) while
others are not (`str` and `int` for addition).

^

### Explicit Conversion

When a user enters numeric values from the keyboard (or if read from a CSV
file), they are seen as strings and must be converted to numeric values:

```py
value_str = input('Please enter a number:')
value_int = int(value_str)
print(value_int + 10)
```

Probably the most common conversions you will encounter are: `int`, `str`,
`float`, `bytes`.

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
