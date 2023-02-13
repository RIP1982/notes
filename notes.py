from note import Note


class Notes(Note):
    def __init__(self, id, title, note, date):
        super().__init__(title, note)
        self._id = id
        self._date = date

    def __str__(self):
        return ("id: " + str(self._id) + ", title: " + self._title +
                ", note: " + self._note + ", date: " + self._date)