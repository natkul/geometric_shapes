from figures.figure import BaseFigure
import math


class Triangle(BaseFigure):
    def __init__(self, a, b, c):
        self.name = 'Triangle'
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def calc_area(a, b, c):
        half_p = (a + b + c) / 2
        return round(math.sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c)))

    @property
    def area(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return self.calc_area(self.a, self.b, self.c)
        else:
            raise ValueError('triangle does not exist')

    @property
    def perimetr(self):
        return self.a + self.b + self.c

    @area.setter
    def area(self, value):
        self._area = value
