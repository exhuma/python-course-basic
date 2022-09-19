# The Standard Library

---

### Python comes with “batteries included”

- Many features supported "out of the box"

Note:

The [standard library][1] of Python comes with many useful features. This makes
it possible to write many useful applications without third-party (external)
libraries.

- Standard Library modules are also imported using the `import` statement.

Standard Library modules take precedence in imports (Use relative imports on
name-conflicts). See [PEP 328][2].

<!-- .element: class="admonition warning" -->

[1]: https://docs.python.org/3/library/
[2]: https://www.python.org/dev/peps/pep-0328

^

## Essential Modules

^

# [`os`](https://docs.python.org/3/library/os.html)

```py
import os

print(os.getenv("MY_ENVIRONMENT_VARIABLE"))
print(f"Current Process ID: {os.getpid()}")
```

<!-- .element: data-caption="Code Sample" -->

Note:

Operating System details. Contains values which are different on
Windows/Linux/MacOS like path \& folder separators.

Also contains access to environment variables & general operating-system
information.

^

# [`os.path`][1] \& [`pathlib`][2]

[1]: https://docs.python.org/3/library/os.path.html
[2]: https://docs.python.org/3/library/pathlib.html

```py
import os.path
import pathlib

print(os.path.isdir("example-filename"))
print(Path("example-filename").is_dir())
```

<!-- .element: data-caption="Code Sample" -->

Note:

Helper functions to deal with file- and folder-names. Contains helpers to
manipulate filenames, converting them from/to absolute files, adding/removing
path elements from names, e.t.c.

`pathlib` was only introduced in Python 3.4

^

# [`logging`](https://docs.python.org/3/library/logging.html)

```py
import logging

logger = logging.getLogger("my-logger")
logging.debug("This is a debug message on the root logger")
logger.error("This is a debug message on my custom logger")
```

<!-- .element: data-caption="Code Sample" -->

Note:

Fully featured logging system inspired by `log4j`. Very easy for simple setups,
but can also handle very complex needs:

- Log to rotating files
- Log to the console
- Log to a remote UDP/TCP destination (Logstash, Splunk, syslog, ...)
- ...

^

# [`json`](https://docs.python.org/3/library/json.html)

```py
import json

data = json.loads('{"mykey": 10}')
print(data["mykey"])
print(json.dumps(data))
```

<!-- .element: data-caption="Code Sample" -->

Note:

Simple helpers for parsing and creating JSON documents.

^

# [`datetime`][1] \& [`time`][2]

[1]: https://docs.python.org/3/library/datetime.html
[2]: https://docs.python.org/3/library/time.html

```py
from datetime import datetime

begin = datetime.now()
user_response = input("Type your name: ")
duration = datetime.now() - begin
print(f"Your name is: {user_response}. Answered in {duration}")
```

Note:

Helpers for date/time processing.

Timezone information was not included in Python versions before 3.9 to allow
faster updates. For Python older than 3.9, the official external module
[pytz][1] can be used.

[1]: https://pypi.org/project/pytz/

---

## Notable Modules

^

# [`argparse`](https://docs.python.org/3/library/argparse.html)

```py
import argparse

parser = argparse.ArgumentParser(description="My CLI program")
parser.add_argument("-v", "--verbose", action="store_true", default=False)
parser.add_argument("filename", help="The filename to process")
args = parser.parse_args()

print(args.filename)
print(args.verbose)
```

Note:

Allows creating simple to complex parsers for CLI argument handling (successor
of both `optparse` and `getopt`).

^

# [`tempfile`](https://docs.python.org/3/library/tempfile.html)

```py
import tempfile

with tempfile.TemporaryFile() as file_object:
    file_object.write(b"Hello World!")
```

Note:

Support for creating temporary files securely.

^

# [`sqlite3`](https://docs.python.org/3/library/sqlite3.html)

```py
import sqlite3
connection = sqlite3.connect("my-db.db")
with connection.cursor() as cursor:
    cursor.execute("SELECT column FROM table ORDER BY column")
    for row in cursor:
        print(row)
```

<!-- .element: data-caption="Code Sample" -->

Note:

Support for structured persistent data storage without a DB server.

^

# [`configparser`](https://docs.python.org/3/library/configparser.html)

```py
import configparser

config = configparser.ConfigParser()
config.read('example.ini')
print(config.get("section_name", "option_name", fallback="default_value"))
```

<!-- .element: data-caption="Code Sample" -->

Note:

Support for working with `.ini` files.

^

# [`hashlib`](https://docs.python.org/3/library/hashlib.html)

```py
import hashlib

response = input("Enter a value: ")
hashed = hashlib.sha256(response.encode("utf8"))
print(hashed.hexdigest())
```

<!-- .element: data-caption="Code Sample" -->

Note:

Support for calculating common hashes (`md5`, `sha1`, …)

---

## The CSV module

^

- [RFC-4180](https://www.rfc-editor.org/rfc/rfc4180.html) compliant CSV implementation
- Support for quoted values
- Support for multiline values
- Support for escaped characters

^

### Example

```py
import csv


infile = open('data/basics.csv')
reader = csv.reader(infile, delimiter=';')
for row in reader:
    print(row)
```

<!-- .element: data-filename="code/read-csv.py" -->

^

## Demo

```py
import csv
from decimal import Decimal
from hashlib import md5


def read_data(filename):
    infile = open(filename)
    output = []
    reader = csv.reader(infile, delimiter=";")
    for row in reader:
        checksum = md5(row[6].encode("utf8")).hexdigest()
        age = int(row[4])
        income = Decimal(row[5])
        hobbies = row[6].split(",")
        new_line = [
            row[0],
            row[1],
            row[2],
            row[3],
            age,
            income,
            hobbies,
            checksum,
        ]
        output.append(new_line)
    return output

print(read_data("data.csv"))
```

<!-- .element: class="stretch smallcode" -->

Note:

<!-- .element: style="font-size: 50%" -->

We will write a new function `read_data` that takes a filename as argument. The
file [csv3.csv](/fileview.html?filename=data/csv3.csv) can be used as example. The function will do
the following:

- Open the file with the given filename
- Initialise a new variable named output as empty list.
- Create a CSV reader with the opened file object
- Loop through each line and do the following:
  - Convert each numerical column into an appropriate type (f.ex.: use
    `decimal.Decimal` for monetary values).
  - Split the 7 th column (index 6) into a list of strings.
  - Add a new column at the end which contains the MD5 hex-digest of the whole
    line, values only (see `hashlib.md5()`).
    - MD5 sums can only be calculated on bytes (not strings)
  - Append the new columns to the `output` list
- After the loop, return the list `output`
