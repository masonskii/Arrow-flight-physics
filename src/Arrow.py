import numpy as np
from src.Physic.Object import Object

class Arrow(Object):
    """
    Represents an arrow object with properties such as mass and air resistance.
    The arrow's trajectory is affected by these properties.
    """

    def __init__(self) -> None:
        """
        Initializes the Arrow object with default values for mass and air resistance.
        """
        super().__init__()
        self._mass: np.float64() = np.float64(0.2) 
        self._air_resistance: np.float64 = np.float64(0.001)

    @property
    def mass(self) -> np.float64:
        """
        Gets the mass of the arrow.
        
        Returns:
            The mass of the arrow.
        """
        return self._mass
    
    @mass.setter
    def mass(self, value: np.float64) -> None:
        """
        Sets the mass of the arrow to the given value.
        
        Args:
            value: The new mass value for the arrow.
        """
        self._mass = value

    @property
    def air_resistance(self) -> np.float64:
        """
        Gets the air resistance of the arrow.
        
        Returns:
            The air resistance of the arrow.
        """
        return self._air_resistance
    
    @air_resistance.setter
    def air_resistance(self, value: np.float64) -> None:
        """
        Sets the air resistance of the arrow to the given value.
        
        Args:
            value: The new air resistance value for the arrow.
        
        Raises:
            TypeError: If the value is not a number.
        """
        if isinstance(value, float or int):
            self._air_resistance = value
        else:
            raise TypeError("Air resistance must be a number")