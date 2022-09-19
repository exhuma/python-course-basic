import csv

infile = open("data/basics.csv")
reader = csv.reader(infile, delimiter=";")
for row in reader:
    print(row)
