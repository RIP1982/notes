from datetime import datetime
from notes import Notes
import csv
import os.path
import readFromCsv

def creater(name):
    notes_list = readFromCsv.readerFromCsv(name)
    id = 0
    if os.path.getsize(name) == 0:
        id = 1
    else:
        last_record = notes_list[-1]
        id = int(last_record[0].split(',')[0]) + 1
    print("Write note title: ")
    title = input()
    print("Write a note: ")
    new_note = input()
    current_datetime = str(datetime.now()).split('.')[0]
    note = Notes(id, title, new_note, current_datetime)
    return note