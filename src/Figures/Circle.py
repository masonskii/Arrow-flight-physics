import numpy as np
from .Figure import Figure


class Circle(Figure):
    def __init__(self, radius: np.float64):
        super().__init__()
        self.add_dimension(radius)

    def perimeter(self):
        return 2 * 3.14 * self.dimensions[0]

    def area(self):
        return 3.14 * self.dimensions[0] ** 2
    
    def __str__(self):
        return f'Circle with radius {self.dimensions[0]}' 