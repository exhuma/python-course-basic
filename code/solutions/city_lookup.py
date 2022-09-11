"""
This exercise contains a solution for the exercie which uses data files as
lookup.

* The file "city_lookup_cities.csv" contains a collection of cities. Each city
  has a unique ID.
* The file "city_lookup_people.csvl" contains a list of people. Each entry has
  a column "City ID" which can be used to look up the city in the other file.


This exercises demonstrates:

* Using dictionaries for fast and easy lookup
"""
import csv


def merge(cities_file, people_file):
    """
    This function takes a file of people and a file of cities and returns a
    list of records with the information merged (the city name will be added to
    the person's record)
    """

    # First, we read the city data into a dictionary for fast lookup. We use
    # the first column of the row (the ID) as key, and the whole row as value.
    # This duplicates the "ID" value, but because the data-set is so small this
    # is OK and makes theremaining code easier.
    rdr_cities = csv.reader(cities_file)
    cities_lookup = {}
    for row in rdr_cities:
        cities_lookup[row[0]] = row

    # Now we will loop over the people list, and use the dictionary from before
    # to lookup cities.
    rdr_people = csv.reader(people_file)

    # Using "next" on a CSV reader will return the next row and advance it by
    # one record. Here we ignore the return value. The first row is the header
    # and we will ignore it.
    next(rdr_people)

    # The reader is now advanced to the second record and we can start looping.
    for row in rdr_people:
        city_id = row[6]
        # We now print the person's first and last name and the city name from
        # the lookup
        print(row[0], row[1], cities_lookup[city_id][1])

    return []


# This will start the application, opeb both files and run the merge operation
if __name__ == "__main__":
    with open("city_lookup_cities.csv") as infile_cities:
        with open("city_lookup_people.csv") as infile_people:
            output = merge(infile_cities, infile_people)
            for row in output:
                print(row)
