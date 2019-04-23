import csv
from decimal import Decimal
from hashlib import md5


def read_data(filename):

    infile = open(filename)
    output = []
    reader = csv.reader(infile, delimiter=';')

    for row in reader:
        checksum = md5(row[6].encode('utf8')).hexdigest()
        age = int(row[4])
        income = Decimal(row[5])
        hobbies = row[6].split(',')
        new_line = [
            row[0], row[1], row[2], row[3], age, income, hobbies, checksum]
        output.append(new_line)
    return output


print(read_data('data.csv'))
