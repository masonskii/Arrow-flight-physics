import numpy as np
from typing import Union, Any

from.Figure import Figure


class Sphere(Figure):
    def __init__(self, radius: np.float64):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        return 4 * 3.14 * self.radius ** 2

    def calculate_volume(self):
        return (4 / 3) * 3.14 * self.radius ** 3
    