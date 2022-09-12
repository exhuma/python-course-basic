# Essential Syntax

^

* The variable type is implicit, but strong (dynamic typing)
* Variables are assigned with the `=` operator
* Line-comments start with a `#` character. Block comments don’t exist.
* Lines do not need to end with a semicolon (`;`)
* Blocks are defined by indentation. `:` starts a new block (like `begin` or
  `{`)

^

```py
# Variable Assignment
my_variable = 10

# Conditional & Blocks
if my_variable >= 10:
    print("Yes")
```
^

### Simple Operations

```py
# Calling the builtin function "print"
print('Hello ' + 'World!')
print(10 + 3)
print(10 / 3)

# Setting variables
a = 'Hello'
b = 'World!'
print(a + b)

a = 10
b = 3
print(a * b)
```


---

### Builtin Functions and Working with Files

* Python has a few [builtin functions][builtins] which are very useful.
* [open()][open] is used to access files on the disk (for reading and writing).
* By default files are opened as “text”.
* Using a for loop on file objects will iterate line-by-line. Newlines are not removed.
* [pathlib][pathlib] and [os.path][path] contain useful functions for working with files.

[builtins]: https://docs.python.org/3/library/functions.html
[open]: https://docs.python.org/3/library/functions.html#open
[pathlib]: https://docs.python.org/3/library/pathlib.html#module-pathlib
[path]: https://docs.python.org/3/library/os.path.html#module-os.path
^

### Reading a File

```py
input_file = open('data/hello.txt')

# "for … in …" knows how to loop over many things
for row in input_file:
    print(row)
```
<!-- .element: data-caption="code/reading-a-file.py" -->

```txt
This is the first line

This is line #3
```
<!-- .element: data-caption="code/data/reading-a-file.txt" -->

---

## Looping

Executing code on a collection of items (looping) can be done in several ways
in Python:

* A `for ... in` ... loop
* A `while ...` loop
* A comprehension expression (not covered in this course)
* Functional aproach using [map()][map], [filter()][filter] and
  [functools.reduce()][reduce] (not covered in this course).

[map]: https://docs.python.org/3/library/functions.html#map
[filter]: https://docs.python.org/3/library/functions.html#filter
[reduce]: https://docs.python.org/3/library/functools.html#functools.reduce
^

### Example

```py
# Simple loop
mydata = [1, 2, 3, 4]
for item in mydata:
    print(item)

# Loop over each item in a list with an index
mydata = [1, 2, 3, 4]
for i, item in enumerate(mydata):
    print(i, item)

# Loop until the user wants to quit
response = 'y'
while response != 'n':
    response = input('Do you want to continue [y/n]?')
```
<!-- .element: data-caption="code/looping.py" -->


---

## Reading Files

Reading and writing files is done using the builtin function [open()][open].
This function will return a “file-like object” which has low-level methods like
[read()][read] and [write()][write].

[read]: https://docs.python.org/3/library/io.html#io.RawIOBase.read
[write]: https://docs.python.org/3/library/io.html#io.RawIOBase.write
[open]: https://docs.python.org/3/library/functions.html#open
^

### Example
```py
# Open a file in default ("read") mode
infile = open('data/basics.csv')


# Iterating over the file object will give us lines (as string)
for line in infile:

    # string objects have many useful methods. "strip" will remove
    # leading and trailing whitespace, ...
    stripped_line = line.strip()

    # ... and "split" will convert a string to a list of strings
    columns = stripped_line.split(';')

    # "repr" is a helper function for debugging. It converts a value
    # into a developer-friendly "representation". For strings this
    # includes the proper quotes (and escapes).
    print(repr(columns))
```
<!-- .element: class="smallcode" data-caption="code/read-csv.py" -->

^

### CSV File Contents

```txt
name;first_name;phone;email
Doe;John;12345;jdoe@exampe.com
Dane;John;12345;jdoe@exampe.com
```
<!-- .element: class="smallcode" data-caption="code/data/basics.csv" -->

^

### Closing Resources

Files, database-/network-connections and similar resources should always be
closed.

Python can ensure that this is done correctly by using the `with` statement:

```py
with open('data.csv') as infile:
    do_something_with(infile)
    print(infile.closed)  # Will print "False"

# Variables created in the "with" block will remain accessible,
# but cleanup has taken place. In this case, the file will be
# closed now.
print(infile.closed)  # Will print "True"
```
