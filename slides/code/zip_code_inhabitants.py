"""
Merges data from multiple files
"""

import csv


def location_to_zips():
    output = {}
    with open("caclr/TR.DICACOLO.RUCP", encoding="cp1252") as infile:
        for row in infile:
            location = row[120:160].strip()
            zipcode = row[200:204].strip()
            # Using "in/not in" on dictionaries checks for the presence of a
            # *key*
            if location not in output:
                output[location] = {zipcode}
            else:
                output[location].add(zipcode)
    return output


def zip_to_inhabitants():
    output = {}
    with open("rnrpp-code-postal.csv") as infile:
        reader = csv.reader(infile)
        # next() advances any iterator by one iteration. Here we use this to
        # skip the header.
        next(reader)
        for code, inhabitants in reader:
            output[code] = int(inhabitants)
    return output


def merge_data():
    locs = location_to_zips()
    inhabitants_map = zip_to_inhabitants()
    output = []
    for location, zip_codes in locs.items():
        total_inhabitants = 0
        for zip_code in zip_codes:
            total_inhabitants += inhabitants_map.get(zip_code, 0)
        output.append((location, total_inhabitants))
    return output


def main():
    data = merge_data()
    # ADVANCED: A "lambda" is an anonymous function with only one statment
    final_output = sorted(data, key=lambda item: -item[1])
    for location, count in final_output[:10]:
        print(f"{location:30s} {count}")


main()
