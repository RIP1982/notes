import csv
def readerFromCsv(name):
    print()
    with open(name) as csvfile:
        print(csvfile.read())