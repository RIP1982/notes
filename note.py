class Note:

    def __init__(self, id, title, note, date):
        self.id = id
        self.title = title
        self.note = note
        self.date = date

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_date(self):
        return self.date

    def __str__(self):
        return ("id: " + self.id + "; title: " +
                self.title + "; note: " +
                self.note + "; date: " +
                self.date)

