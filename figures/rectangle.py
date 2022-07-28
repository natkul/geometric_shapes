from figures.figure import BaseFigure


class Rectangle(BaseFigure):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.name = "Rectangle"

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimetr(self):
        return (self.a + self.b) * 2
