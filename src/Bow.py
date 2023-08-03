import numpy as np
import random
from src.Physic import Object

class Bow(Object):
    """
    Represents a bow object in a physics simulation.

    Attributes:
        forces (list): Possible values for the force property of the bow object.

    """

    forces = [60, 80, 100, 120, 140]

    def __init__(self, angle: np.float64) -> None:
        """
        Initializes a new instance of the Bow class.

        Args:
            angle (np.float64): The angle of the bow.

        """
        super().__init__()
        self._angle: np.float64 = angle
        self._force: np.float64 = self.forces[random.randint(0, 4)]

    @property
    def force(self) -> np.float64:
        """
        Gets the force of the bow.

        Returns:
            np.float64: The force of the bow.

        """
        return self._force

    @property
    def angle(self) -> np.float64:
        """
        Gets the angle of the bow.

        Returns:
            np.float64: The angle of the bow.

        """
        return self._angle

    @force.setter
    def force(self, value: np.float64) -> None:
        """
        Sets the force of the bow.

        Args:
            value (np.float64): The new force value.

        """
        self._force = value

    @angle.setter
    def angle(self, value: np.float64) -> None:
        """
        Sets the angle of the bow.

        Args:
            value (np.float64): The new angle value.

        """
        self._angle = value

