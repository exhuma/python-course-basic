def read_file(filename, separator):
    """
    This is the documentation string of the function.

    The first string" in the function is made accessible to external
    tools. This allows automatic generation of documentation
    """
    infile = open(filename)

    output = []
    for line in infile:
        stripped_line = line.strip()
        columns = stripped_line.split(separator)
        output.append([columns[0], columns[1]])
    return output
