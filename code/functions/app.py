def read_file(filename):
    """
    This is the documentation string of the function.

    The first string" in the function is made accessible to external
    tools. This allows automatic generation of documentation
    """
    infile = open(filename)

    for line in infile:
        stripped_line = line.strip()
        columns = stripped_line.split(';')
        print(repr(columns))


read_file('data.csv')
