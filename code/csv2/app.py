import csv


infile = open("data.csv")
reader = csv.reader(infile, delimiter=";")
for row in reader:
    print(row)
