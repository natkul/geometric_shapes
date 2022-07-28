class BaseFigure:
    perimetr = None
    area = None

    def add_area(self, second_figure):

        if isinstance(second_figure, BaseFigure):
            sum_areas = self.area + second_figure.area
            return sum_areas
        else:
            return 'Invalid geometric shape class passed'

    def get_name(self, figure):
        return figure.name
