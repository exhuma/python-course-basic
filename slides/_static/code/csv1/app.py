# Open a file in default ("read") mode
infile = open('data.csv')


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
