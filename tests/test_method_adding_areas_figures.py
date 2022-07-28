import pytest
from figures.figure import BaseFigure
from figures.circle import Circle
from figures.triangle import Triangle
from figures.rectangle import Rectangle
from figures.square import Square


class TestFigures:
    base_figure = BaseFigure()
    triangle = Triangle(13, 14, 15)
    rectangle = Rectangle(9, 10)
    square = Square(40)
    circle = Circle(5)

    @pytest.mark.parametrize('incorrect_figure', [triangle, rectangle, square, circle, 'something', 55165])
    @pytest.mark.parametrize('default_figure', [triangle, rectangle, circle, square])
    def test_add_square(self, incorrect_figure, default_figure):
        if isinstance(incorrect_figure, BaseFigure):
            assert default_figure.add_area(incorrect_figure) == default_figure.area + incorrect_figure.area
        else:
            assert default_figure.add_area(incorrect_figure) == 'Invalid geometric shape class passed'
