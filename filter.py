import readFromCsv
import datetime
import time
import csv
import view

def filter(name):
    count = 0
    all_notes = readFromCsv.readerFromCsv(name)
    notes_filter = []
    print("Enter the date(YYYYmmdd): ")
    date = datetime.datetime.strptime(input(), '%Y%m%d').date()
    for i in range(len(all_notes)):
        if i != 0:
            if datetime.datetime.strptime(all_notes[i][3], '%Y-%m-%d %H:%M:%S').date() == date:
                notes_filter.append(all_notes[i])
                count += 1
    for i in range(len(notes_filter)):
        print(notes_filter[i])
    if count == 0:
        print("Wrong request!")