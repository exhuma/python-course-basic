# Import only the name "read_file" from the module
# The whole module will be loaded and interpreted. This helps keeping the local
# name-space clean.
from util import read_file

read_file('data.csv')
