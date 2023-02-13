import readFromCsv
import csv
import view

def editor(name):
    count = 0
    all_notes = readFromCsv.readerFromCsv(name)
    view.readerFromCsv(name)
    print("Enter the note title: ")
    keyword = input()
    for i in range(len(all_notes)):
        if all_notes[i][1].lower() == keyword.lower():
            print(all_notes[i])
            print("Edit your note: ")
            all_notes[i][2] = input()
            with open(name, 'w', encoding='UTF8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(all_notes)
            csvfile.close()
            count+=1
    if count == 0:
        print("Wrong request!")








