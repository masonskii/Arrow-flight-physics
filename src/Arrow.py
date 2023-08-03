import numpy as np
from src.Physic.Object import Object

class Arrow(Object):
    def __init__(self) -> None:
        super().__init__()
        self._mass: np.float64() = np.float64(0.2) 
        self._air_resistance: np.float64 = np.float64(0.001)

        # TODO:next task change type arrow
    @property
    def mass(self) -> np.float64:
        return self._mass
    
    @mass.setter
    def mass(self, value: np.float64) -> None:
        self._mass = value

    @property
    def air_resistance(self) -> np.float64:
        return self._air_resistance
    @air_resistance.setter
    def air_resistance(self, value: np.float64) -> None:
        if isinstance(value, float or int ):
            self._air_resistance = value
        else : raise TypeError("Air resistance must be a number")
