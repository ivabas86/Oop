import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
    """ Производный класс. Прямоугольник. """
    # TODO определить конструктор
    def __init__(self, a, b):

    # TODO перегрузить метод area, чтобы он возвращал площадь, но не терял родительский функционал
        self.a = a
        self.b = b

    def area(self):
        super().area()
        return round(self.a * self.b, 3)



class Circle(Figure):
    """ Производный класс. Круг. """
    # TODO определить конструктор
    def __init__(self, a):
        self.a = a

    # TODO перегрузить метод area, чтобы он возвращал площадь,но не терял родительский функционал"
    def area(self):
        super().area()
        return round(self.a * self.a * math.pi, 3)

if __name__ == "__main__":
    fig = Figure()
    print(fig.area())

    rect = Rectangle(5, 10)
    print(rect.area())

    circle = Circle(5)
    print(circle.area())
