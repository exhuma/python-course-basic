"""
This file contains two solutions for the exercise about "collection types"
(slide 91).

This contains two solutions. The first uses a very traditionaly way of
programming, while the second "pythonic" method makes use of some useful Python
functions.

This demonstates:

    * Using "continue" in a loop to immediately go to the next iteartion
    * Using the "extend" method on a list
    * String formatting using the "%" formatting
    * Usage of the "set" type
    * Usage of the "zip" function
    * Helper functions for iterators from the "itertools" package
"""
import csv
from itertools import tee, islice


def print_record(record):
    """
    This function takes a record from the file and prints is to the console.
    """
    print("First Name: %s" % record[0])
    print("Last Name: %s" % record[1])
    print("Hobbies: %s" % record[2])
    print("Phone: %s" % record[3])
    print("E-Mail: %s" % record[4])
    print("Address:\n%s" % record[5])
    print(80 * "-")


def traditional(reader):
    """
    This function uses a traditional approach to combine the line-pairs and
    read the data.
    """

    # We will use a variable "current" row to collect all the columns.
    current_record = []

    # Using a "set" will allow us to store the hobbies without duplicates. If
    # adding something to a set that already exisst, it will have no effect.
    hobbies = set()

    # We enumerate the lines in our readed. We need the index to find out if we
    # have an even or odd number.
    for i, row in enumerate(reader):

        # The first two lines contain headers which we ignore. The "continue"
        # statement immediately goes to the next iteration, skipping the
        # remaining statements in the loop.
        if i <= 1:
            continue

        # The "extend" method on a list takes another list. All elements from
        # the second list (row in this case) will be appended to the other
        # list.
        current_record.extend(row)

        # The "%" operator is the mathematical "modulo" operation. We can use
        # it to see if we have an even row.
        if i % 2 != 0:
            # If he do *not* have an even row, we know that we hit the
            # beginning of a new record and everything we collected in
            # "current_record" needs to printed out and eptied.
            hobbies |= set(current_record[2].split(","))
            # We can finally print the row...
            print_record(current_record)
            # We can also remove anything in the currently collected columns
            current_record.clear()

    # ... and return the result
    return hobbies


def pythonic(reader):
    """
    This function uses a more "pythonic" approach to this exercise.

    This is much more advanced, demonstrating some of the powerful features of
    Python. If you feel adventurous, you can read through it, I tried to
    explain it as best as I can.
    """

    # A CSV reader object depends on the location of the file. If we want to
    # split it into even & odd lines we would need to run over it twice. The
    # "tee" function duplicates anything that can be looped over without
    # "consuming" the data right away. This is very efficient when working with
    # large files.
    even, odd = tee(reader)

    # We now have two "handles" to the input file which can be looped over
    # seperately and independenlty. We want to retrieve the even and odd lines
    # only as fast as we are working with them. We don't want to read them into
    # memory completely (good for large files). The "islice" function allows us
    # to do just that. It takes a starting index, an ending index (which can be
    # "None" to allow running until the end of the file and finally a "step"
    # function defining how many items we advance on each turn. Using a start
    # of 2 and 3 with a step of 2, we will get even and odd lines, and skipping
    # the first record (headers)
    even = islice(even, 2, None, 2)
    odd = islice(odd, 3, None, 2)

    # This zip function creates an object combining two or more objects which
    # can be iterated over *without* reading them into memory. When you have
    # two lists l1=[1, 2, 3] and l2=['a', 'b', 'c'], then zip(l1, l2) will
    # behave like a list with [[1, 'a'], [2, 'b'], [3, 'c']]
    # The items will only be created at the moment it will be looped over, so
    # it can work with files of endless size.
    zipped = zip(even, odd)

    # We want each hobby only once, so we use a set for this.
    hobbies = set()

    # We can now loop over our zip object, which will have in each iteration
    # the first and second line of the same record.
    for line1, line2 in zipped:
        # We print it to the console
        print_record(line1 + line2)

        # ... and us a binary "or" operator to combine the two sets. This is
        # the same as calling the function hobbies = hobbies.union(...)
        hobbies = hobbies | set(line1[2].split(","))
    return hobbies


with open("collections.csv") as infile:
    reader = csv.reader(infile)
    variant = input("Which code do you want to execute [traditional|advanced]? ")
    if variant.strip().lower() == "traditional":
        hobbies = traditional(reader)
    elif variant.strip().lower() == "advanced":
        hobbies = pythonic(reader)
    else:
        print("Unknown variant")
        hobbies = set()

    print("All hobbies:")
    for hobby in sorted(hobbies):
        print(hobby)
