import csv
from uuid import uuid4

PEOPLE = [
    (
        "John",
        "Doe",
        "Fishing,Biking",
        "12345",
        "jodo@example.com",
        "1, Sample Street\n123ABC Stonehenge",
    ),
    (
        "Jane",
        "Doe",
        "Biking,Videogames",
        "12345",
        "jado@example.com",
        "1, Sample Street\n123ABC Stonehenge",
    ),
    (
        "Karl",
        "Mustermann",
        "Fitness,Cooking,Football",
        "11223",
        "musti@example.com",
        "2A Schlossallee\n123 Brett",
    ),
    (
        "Anna",
        "Musterfrau",
        "Häkeln,Cooking",
        "11223",
        "musti@example.com",
        "22 Ostbahnhof\n111 Brett",
    ),
]

HOBBIES = {
    "Fishing",
    "Biking",
    "Videogames",
    "Fitness",
    "Cooking",
    "Reading",
    "Football",
    "Häkeln",
}


def make_split_rows():
    """
    Creates a more complex example for the "collections" exercise
    """

    with open("slides/_static/collections.csv", "w") as outfile:
        rows = []
        rows.append(["First Name", "Last Name", "Hobbies"])
        rows.append(["Phone", "email", "Address"])
        for person in PEOPLE:
            rows.append(person[:3])
            rows.append(person[3:])
        writer = csv.writer(outfile)
        writer.writerows(rows)


def make_lookup_table():
    """
    Creates data which can be used for the encoding & merging exercise
    """
    from random import choice

    cities = [
        (uuid4(), "São Paulo", "Yellow"),
        (uuid4(), "Bogotá", "Yellow"),
        (uuid4(), "澳门特别行政区", "Blue"),
        (uuid4(), "犬山市", "Red"),
        (uuid4(), "Mersch", "Blue"),
    ]

    with open("slides/_static/city_lookup_people.csv", "w") as outfile:
        writer = csv.writer(outfile)
        header = [
            "First Name",
            "Last Name",
            "Hobbies",
            "Phone #",
            "email",
            "Address",
            "City ID",
        ]
        writer.writerow(header)
        for input_row in PEOPLE:
            city = choice(cities)
            city_id = city[0]
            output_row = input_row + (city_id,)
            writer.writerow(output_row)

    with open("slides/_static/city_lookup_cities.csv", "w") as outfile:
        writer = csv.writer(outfile)
        header = ["id", "name", "team"]
        writer.writerow(header)
        writer.writerows(cities)


if __name__ == "__main__":
    make_lookup_table()
