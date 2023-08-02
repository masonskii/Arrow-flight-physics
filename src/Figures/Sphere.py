import numpy as np
from typing import Union, Any

from.Figure import Figure


class Sphere(Figure):
    def __init__(self, radius: np.float64):
        super().__init__()
        self.radius = radius

    def area(self):
        return 4 * np.pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * np.pi * self.radius ** 3
    