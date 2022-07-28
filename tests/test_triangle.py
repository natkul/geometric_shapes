import pytest
from figures.figure import BaseFigure
from figures.triangle import Triangle


class TestFigures:
    base_figure = BaseFigure()
    triangle = Triangle(13, 14, 15)

    @pytest.fixture
    def create_base_figure(self):
        base_figure = BaseFigure()
        return base_figure

    def test_get_name(self, create_base_figure):
        base_figure = create_base_figure
        assert base_figure.get_name(self.triangle) == 'Triangle'

    def test_get_perimetr(self):
        assert self.triangle.perimetr == 42

    def test_get_area(self):
        assert self.triangle.area == 84
