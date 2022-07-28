import pytest
from figures.figure import BaseFigure
from figures.rectangle import Rectangle


class TestFigures:
    base_figure = BaseFigure()
    rectangle = Rectangle(9, 10)

    @pytest.fixture
    def create_base_figure(self):
        base_figure = BaseFigure()
        return base_figure

    def test_get_name(self, create_base_figure):
        base_figure = create_base_figure
        assert base_figure.get_name(self.rectangle) == 'Rectangle'

    def test_get_perimetr(self):
        assert self.rectangle.perimetr == 38

    def test_get_area(self):
        assert self.rectangle.area == 90
