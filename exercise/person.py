import datetime


class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def get_last_name(self):
        return self.lastName

    def __str__(self):
        return self.name

    def set_birthday(self, m, d, y):
        self.birthday = datetime.date(y, m, d)

    def get_age(self):
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).day

    def __lt__(self, other):
        if self.lastName is other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName


class MITPerson(Person):
    nextId = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.id = MITPerson.nextId
        MITPerson.nextId += 1

    def get_id(self):
        return self.id

    def __lt__(self, other):
        return self.id < other.id

    def speak(self, utterance):
        return f"{self.get_last_name()} says {utterance}"
