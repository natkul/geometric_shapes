from figures.figure import BaseFigure


class Square(BaseFigure):
    def __init__(self, a):
        self.a = a
        self.name = 'Square'

    @property
    def area(self):
        return self.a ** 2

    @property
    def perimetr(self):
        return self.a * 4
