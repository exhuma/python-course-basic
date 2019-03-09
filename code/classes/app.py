class MyReader:
    '''
    This is the class docstring which is commonly used to document the
    "constructor" in documentation tools like Sphinx.
    '''

    def __init__(self, filename):
        '''
        The class "initialisor". This is always calles right after an instance
        of the class is constructed. That instance is available in *self*.
        '''
        self.filename = filename

    def read(self):
        """
        A normal instance method
        """
        infile = open(self.filename)

        for line in infile:
            stripped_line = line.strip()
            columns = stripped_line.split(';')
            print(repr(columns))


the_instance = MyReader('data.csv')
the_instance.read_file()
