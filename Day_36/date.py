import datetime as dt


class Today():

    def __init__(self):
        self.now = dt.datetime.now()
        self.day = self.now.day
        self.month = self.now.month
        self.year = self.now.year

        self.date = self.get_date()

    def _get_date(self):
        if self.day < 10 and self.month < 10:
            return f"{self.year}-0{self.month}-0{self.day}"
        elif self.day < 10:
            return f"{self.year}-{self.month}-0{self.day}"
        elif self.month < 10:
            return f"{self.year}-0{self.month}-{self.day}"