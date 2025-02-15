from wsgiref.handlers import format_date_time


class Date:
    def __init__(self, day: int, month: int, year: int):
        # TODO Инициализируйте переменные с проверкой соответствия типа, если не соответствует, то вызывайте ошибку TypeError
        if not isinstance(day, int):
            raise TypeError
        self.day = day
        if not isinstance(month, int):
            raise TypeError
        self.month = month
        if not isinstance(year, int):
            raise TypeError
        self.year = year

    def __str__(self):
        ... # TODO Реализуйте возвращение в формате DD/MM/YYYY
        return f'{self.day:02d}/{self.month:02d}/{self.year:04d}'
    def __repr__(self):
        ... # TODO Реализуйте возвращение в формате Date(day=..., month=..., year=...)
        return f'{self.__class__.__name__}(day={self.day}, month={self.month}, year={self.year})'

if __name__ == "__main__":
    date1 = Date(1, 1, 2021)
    print(date1)  # 01/01/2021
    date2 = Date(11, 10, 1999)
    print(date2)  # 11/10/1999
    print(repr(date1), repr(date2))  # Date(day=1, month=1, year=2021) Date(day=11, month=10, year=1999)

    try:
        Date('1', 1, 2021)
    except TypeError:
        print('Верный вызов TypeError')  # Верный вызов TypeError
    else:
        print('Должен быть вызов TypeError')
