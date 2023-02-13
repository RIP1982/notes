from notes import Notes
import csv
import os.path
from datetime import datetime

def writerToCsv(name, note):
    if os.path.getsize(name) == 0:
        with open(name, 'w', encoding='UTF8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([("id", "Title", "Note", "Date"), [str(note._id), note._title, note._note, str(note._date)],])
    else:
        with open(name, 'a', encoding='UTF8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([str(note._id), note._title, note._note, str(note._date)])
    csvfile.close()