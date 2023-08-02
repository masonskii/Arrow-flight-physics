import numpy as np

from src.Figures.Line import Line, LineEnum
from src.Enums.LineEnum import LineEnum
from src.Enums.FigureEnum import FigureEnum


class Figure:
    def __init__(self) -> None:
        self._a: np.float64 = np.float64(0.0)
        self._S: np.float64 = np.float64(0.0)
        self._v: np.float64 = np.float64(0.0)
        self._r: np.float64 = np.float64(0.0)
