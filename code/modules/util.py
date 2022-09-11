"""
This is the documentation string of the module. It can be extracted
for automatic documentation.

Modules are nothing special. Every Python file can be imported as
module into other Python files.
"""


def read_file(filename):
    infile = open(filename)

    for line in infile:
        stripped_line = line.strip()
        columns = stripped_line.split(";")
        print(repr(columns))


# Don't do this! This "print" will be exectued on first import
print("This is an import side-effect")
