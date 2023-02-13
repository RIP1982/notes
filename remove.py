import readFromCsv
import csv
import view

def remover(name):
    all_notes = readFromCsv.readerFromCsv(name)
    view.readerFromCsv(name)
    print("Enter the note title: ")
    keyword = input()
    for i in range(len(all_notes)):
        if all_notes[i][1].lower() == keyword.lower():
            print(all_notes[i])
            print("Do you want to remove the note? Y/n: ")
            answer = input()
            if answer.lower() == "y":
                all_notes.pop(i)
                with open(name, 'w', encoding='UTF8', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(all_notes)
                csvfile.close()
                i-=1





