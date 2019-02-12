# This is an ambiguous import but it is good enough for this example.
#
# Imports only the name "read_file" from the module, but the whole module will
# be loaded and interpreted. This helps keeping the local name-space clean.
from util import read_file

read_file()
