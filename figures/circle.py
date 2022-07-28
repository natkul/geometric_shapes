from figures.figure import BaseFigure


class Circle(BaseFigure):
    def __init__(self, r):
        self.r = r
        self.name = 'Circle'

    @property
    def area(self):
        return 3.14 * self.r ** 2

    @property
    def perimetr(self):
        return round(2 * 3.14 * self.r, 1)
