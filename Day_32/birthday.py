import datetime as dt


class Person():
    def __init__(self, person: dict):
        self.person = person

        self.name = person['name']
        self.email = person['email']
        self.year_of_birth = person['year']
        self.month_of_birth = person['month']
        self.day_of_birth = person['day']


class Today():
    def __init__(self):
        self.now = dt.datetime.now()
        self.day = self.now.day
        self.month = self.now.month
        self.year = self.now.year