import csv

def merge(cities_file, people_file):
    rdr_cities = csv.reader(cities_file)
    cities_lookup = {}
    for row in rdr_cities:
        cities_lookup[row[0]] = row

    rdr_people = csv.reader(people_file)

    next(rdr_people)  # This skips the header
    for row in rdr_people:
        city_id = row[6]
        print(row[0], row[1], cities_lookup[city_id][1])

    return []


if __name__ == '__main__':
    with open('slides/_static/city_lookup_cities.csv') as infile_cities:
        with open('slides/_static/city_lookup_people.csv') as infile_people:
            output = merge(infile_cities, infile_people)
            for row in output:
                print(row)
