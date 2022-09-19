import csv
from decimal import Decimal
from hashlib import md5


def read_data(filename):

    infile = open(filename)
    output = []
    reader = csv.reader(infile, delimiter=";")

    for row in reader:
        checksum = md5(row[6].encode("utf8")).hexdigest()

        try:
            age = int(row[4])
        except ValueError:
            logging.error("Invalid number: %r", row[4], exc_info=True)
            age = 0

        try:
            income = Decimal(row[5])
        except ValueError:
            logging.error("Invalid number: %r", row[5], exc_info=True)
            income = Decimal("0.0")

        hobbies = row[6].split(",")
        new_line = [
            row[0],
            row[1],
            row[2],
            row[3],
            age,
            income,
            hobbies,
            checksum,
        ]
        output.append(new_line)
    return output


print(read_data("data.csv"))
