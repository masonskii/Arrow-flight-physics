import numpy as np
import random
from src.Physic import Object

class Bow(Object):
    
    # Возможные варианты силы натяжения
    forces = [60, 80, 100, 120, 140] 

    def __init__(self, angle: np.float64) -> None:
        super().__init__()
        self._angle: np.float64 = angle
        self._force: np.float64 = self.forces[random.randint(0, 4)]
        # ...

    # ...
    @property
    def force(self) -> np.float64:
        return self._force
    
    @property
    def angle(self) -> np.float64:
        return self._angle
    
    @force.setter
    def force(self, value: np.float64) -> None:
        self._force = value

    @angle.setter
    def angle(self, value: np.float64) -> None:
        self._angle = value

