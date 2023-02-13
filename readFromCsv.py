import csv

def readerFromCsv(name):
    with open(name, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        notes = []
        for row in reader:
            notes.append(row)
        csvfile.close()
    return notes