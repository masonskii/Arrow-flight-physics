import numpy as np

from src.Figures.Line import Line, LineEnum
from src.Enums.LineEnum import LineEnum
from src.Enums.FigureEnum import FigureEnum
class Figure:
    def __init__(self):
        self.sides = []
        self.dimensions = []

    def add_side(self, length):
        self.sides.append(length)

    def add_dimension(self, value):
        self.dimensions.append(value)

    def perimeter(self):
        raise NotImplementedError("Subclasses of Figure should implement the 'perimeter' method.")

    def area(self):
        raise NotImplementedError("Subclasses of Figure should implement the 'area' method.")

    def volume(self):
        raise NotImplementedError("Subclasses of Figure should implement the 'volume' method.")

    