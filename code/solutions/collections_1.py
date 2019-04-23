import csv
from itertools import tee, islice


def print_record(record):
    print('First Name: %s' % record[0])
    print('Last Name: %s' % record[1])
    print('Hobbies: %s' % record[2])
    print('Phone: %s' % record[3])
    print('E-Mail: %s' % record[4])
    print('Address:\n%s' % record[5])
    print(80 * '-')


def functional(reader):
    even, odd = tee(reader)
    even = islice(even, 0, None, 2)
    odd = islice(odd, 1, None, 2)
    combined = zip(even, odd)
    hobbies = set()
    for line1, line2 in combined:
        print_record(line1 + line2)
        hobbies = hobbies | set(line1[2].split(','))
    return hobbies


def imperative(reader):
    current_row = []
    hobbies = set()
    for i, row in enumerate(reader):
        if i <= 2:
            continue
        current_row.extend(row)
        if i % 2 == 0:
            hobbies |= set(row[-1].split(','))
            current_row.clear()
    print_record(current_row)
    hobbies |= set(row[-1].split(','))
    return hobbies


with open('slides/_static/collections.csv') as infile:
    reader = csv.reader(infile)
    hobbies = functional(reader)
    print('All hobbies:')
    for hobby in sorted(hobbies):
        print(hobby)
