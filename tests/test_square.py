import pytest
from figures.figure import BaseFigure
from figures.square import Square


class TestFigures:
    base_figure = BaseFigure()
    square = Square(40)

    @pytest.fixture
    def create_base_figure(self):
        base_figure = BaseFigure()
        return base_figure

    def test_get_name(self, create_base_figure):
        base_figure = create_base_figure
        assert base_figure.get_name(self.square) == 'Square'

    def test_get_perimetr(self):
        assert self.square.perimetr == 160

    def test_get_area(self):
        assert self.square.area == 1600
