import remove
from notes import Notes
import create
import save
import edit
import view

def start_button():
    while True:
        print("1. 'CREATE' - create a note")
        print("2. 'EDIT' - edit a note")
        print("3. 'REMOVE' -  remove a note")
        print("4. 'VIEW' - list notes")
        print("5. 'FILTER' - list notes")
        print("6. 'EXIT' - exit")
        cmd = input("Enter your request: ")

        if cmd.lower() == "create":
            new_note = create.creater("notes.csv")
            print("Do you want to save the note? Y/N")
            answer = input()
            if answer.lower() == "y":
                save.writerToCsv("notes.csv", new_note)
            else:
                continue
        elif cmd.lower() == "edit":
            edit.editor("notes.csv")
        elif cmd.lower() == "remove":
            remove.remover("notes.csv")
        elif cmd.lower() == "view":
            view.readerFromCsv("notes.csv")
        elif cmd.lower() == "filter":
            print(filter)
        elif cmd.lower() == "exit":
            break
        else:
            print("Wrong request, try again!")


