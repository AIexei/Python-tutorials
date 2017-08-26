class Test:
    price = 9999

    @classmethod
    def get_price(cls):
        return cls.price

    @classmethod
    def change_price(cls, value):
        cls.price = value

    @staticmethod
    def some_method(value):
        return value


class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date = cls(day, month, year)
        return date

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <=12 and year <= 3999


if __name__ == '__main__':
    a = Test()
    print(a.get_price())

    Test.change_price(888)
    c = Test()
    print(c.price)

    date = Date.from_string('11-08-2017')
    print(date.__dict__)