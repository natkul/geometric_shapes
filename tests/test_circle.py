import pytest
from figures.figure import BaseFigure
from figures.circle import Circle


class TestFigures:
    base_figure = BaseFigure()
    circle = Circle(5)

    @pytest.fixture
    def create_base_figure(self):
        base_figure = BaseFigure()
        return base_figure

    def test_get_name(self, create_base_figure):
        base_figure = create_base_figure
        assert base_figure.get_name(self.circle) == 'Circle'

    def test_get_perimetr(self):
        assert self.circle.perimetr == 31.4

    def test_get_area(self):
        assert self.circle.area == 78.5
