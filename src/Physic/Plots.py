from typing import Any, Union
import numpy as np
import matplotlib.pyplot as plt

class Plot:
    def __init__(self) -> None:
        pass

    def create_plot(self) -> None:
        raise NotImplementedError("Subclasses of Plot should implement the 'create_plot' method.")
    
    def change_plot(self) -> None:
        raise NotImplementedError("Subclasses of Plot should implement the 'change_plot' method.")

    def draw(self) -> None:
        raise NotImplementedError("Subclasses of Plot should implement the 'draw' method.")

    def is_collision(self, obj: object) -> None:
        raise NotImplementedError("Subclasses of Plot should implement the 'is_collision' method.")


class SquarePlot(Plot):
    def __init__(self, x0: np.float64, y0: np.float64, length: np.int64) -> None:
        super().__init__()
        self._x0: np.float64 = x0
        self._y0: np.float64 = y0
        self._length: list = [(x0 + length, y0 + length)]

    def draw(self, dataset: Union[list, dict, Any]) -> None:
        pass
    def is_collision(self, obj: object) -> None:
        pass