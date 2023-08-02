import numpy as np

from typing import Union, Any
from .Figure import Figure


class Triangle(Figure):
    def __init__(self, side: list[Union[np.float64,np.int64,Any]]):
        super().__init__()
        self.add_side(side)

    def perimeter(self):
        return sum(self.sides)

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2])) ** 0.5