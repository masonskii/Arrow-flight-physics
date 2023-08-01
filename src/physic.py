import numpy as np

from dataclasses import dataclass
from typing import Any, Tuple, Union
from enum import Enum

class AngleEnum(Enum):
    """
    A class representing different types of angles.

    This class provides a way to define and access different types of angles as attributes of the class.
    The class makes use of the Enum module to create a set of named constants that represent the different types of angles.
    These constants can be used in place of integer values, making the code more readable and easier to understand.

    Attributes:
        ACUTE_ANGLE (int): Represents an acute angle.
        RIGHT_ANGLE (int): Represents a right angle.
        OBTUSE_ANGLE (int): Represents an obtuse angle.
        STRAIGHT_ANGLE (int): Represents a straight angle.
        EXACTLY_180_DEGREES (int): Represents an angle that is exactly 180 degrees.
    """
    ACUTE_ANGLE = 0
    RIGHT_ANGLE = 1
    OBTUSE_ANGLE = 2
    STRAIGHT_ANGLE = 3
    EXACTLY_180_DEGREES = 4

class LaunchAngle:
    """
    A class representing the launch angle of a projectile.

    Attributes:
    - _angle: The launch angle in degrees, stored as a numpy float64 value.
    - _speed_angle_change_rate: The rate at which the launch angle changes with respect to speed, stored as a numpy float64 value.
    - _type_angle: The type of angle (acute, right, obtuse, straight, or exactly 180 degrees), stored as an instance of the AngleEnum class.
    """

    def __init__(self) -> None:
        """
        Constructor method that initializes the fields of the class.
        """
        self._angle: np.float64 = np.float64(0.0)
        self._speed_angle_change_rate: np.float64 = np.float64(0.0)
        self._type_angle: AngleEnum = AngleEnum.ACUTE_ANGLE
    
    @property
    def angle(self) -> np.float64:
        return self._angle
    
    @angle.setter
    def angle(self, value: np.float64) -> None:
        self._angle = value
    

@dataclass
class Color:
    """
    Represents a color with RGB values.

    Fields:
    - r: an integer representing the red value of the color
    - g: an integer representing the green value of the color
    - b: an integer representing the blue value of the color.
    """

    r: int
    g: int
    b: int
    
class ObjectState(Enum):
    '''
    ObjectState is an enumeration class that represents the state of an object.
    
    Attributes:
        STATIC (int): represents a static object.
        DYNAMIC (int): represents a dynamic object.
        MOVING (int): represents a moving object.
        JUMPING (int): represents a jumping object.
        FALLING (int): represents a falling object.
        EXPLODING (int): represents an exploding object.
        INACTIVE (int): represents an inactive object.
        ACTIVE (int): represents an active object.
        HIDDEN (int): represents a hidden object.
        DESTROYED (int): represents a destroyed object.
    '''
    STATIC = 1
    DYNAMIC = 2
    MOVING = 3
    JUMPING = 4
    FALLING = 5
    EXPLODING = 6
    INACTIVE = 7
    ACTIVE = 8
    HIDDEN = 9
    DESTROYED = 10


class Physic:
    """
    Physic class represents a physical object with properties such as mass, speed, acceleration, position, radius, color, state, and collision properties. It provides getter and setter methods for accessing and modifying these properties. The class also includes a static method for checking and converting values to np.float64. 

    Fields:
    - _mass: np.float64 representing the mass of the object
    - _speed: np.float64 representing the speed of the object
    - _acceleration: np.float64 representing the acceleration of the object
    - _position: np.float64 representing the position of the object
    - _radius: np.float64 representing the radius of the object
    - _color: Color object representing the color of the object
    - _state: ObjectState enum representing the state of the object (STATIC or DYNAMIC)
    - _is_collidable: boolean indicating if the object is collidable
    - _is_collidable_with_static: boolean indicating if the object is collidable with static objects
    - _is_collidable_with_dynamic: boolean indicating if the object is collidable with dynamic objects
    """

    def __init__(self) -> None:
        """
        Physic class constructor
        """
        
        # public variables
        self.max_height: np.float64 = np.float64(0.0)
        self.flight_time: np.float64 = np.float64(0.0)
        self.distance: np.float64 = np.float64(0.0)
        self.trajectory_x: list[np.float64] = []
        self.trajectory_y: list[np.float64] = []
        
        # private variables
        self._mass: np.float64 = np.float64(0.0)
        self._speed: np.float64 = np.float64(0.0)
        self._acceleration: np.float64 = np.float64(0.0)
        self._position: np.float64 = np.float64(0.0)
        self._radius: np.float64 = np.float64(0.0)
        self._color: Color = Color(0, 0, 0)
        self._state: ObjectState = ObjectState.STATIC
        self._is_collidable: bool = False
        self._is_collidable_with_static: bool = False
        self._is_collidable_with_dynamic: bool = False

    
    @property
    def mass(self) -> np.float64:
        return self._mass
    
    @mass.setter
    def mass(self, value: np.float64) -> None:
        self._mass = self._check_and_convert_to_float64(value)
        
    @property
    def speed(self) -> np.float64:
        return self._speed
    
    @speed.setter
    def speed(self, value: np.float64) -> None:
        self._speed = self._check_and_convert_to_float64(value)
        
    @property
    def acceleration(self) -> np.float64:
        return self._acceleration
    
    @acceleration.setter
    def acceleration(self, value: np.float64) -> None:
        self._acceleration = self._check_and_convert_to_float64(value)
        
    @property
    def position(self) -> np.float64:
        return self._position
    
    @position.setter
    def position(self, value: np.float64) -> None:
        self._position = self._check_and_convert_to_float64(value)
        
    @property
    def radius(self) -> np.float64:
        return self._radius
    
    @radius.setter
    def radius(self, value: np.float64) -> None:
        self._radius = self._check_and_convert_to_float64(value)
        
    @property
    def color(self) -> dict:
        return self._color
    
    @color.setter
    def color(self, value: Color) -> None:
        if not isinstance(value, Color):
            raise TypeError('Expected Color object')
        self._color = value
    
    @property
    def state(self) -> ObjectState:
        return self._state
    
    @state.setter
    def state(self, value: ObjectState) -> None:
        self._state = value

    @property
    def is_collidable(self) -> bool:
        return self._is_collidable
    
    @is_collidable.setter
    def is_collidable(self, value: bool) -> None:
        """
        Set the 'is_collidable' attribute of the 'Physic' class to a boolean value indicating whether the object is collidable objects or not.

        Args:
            value (bool): Indicates whether the object is collidable with static objects or not.

        Returns:
            None
        """
        self._is_collidable = value
        
    @property
    def is_collidable_with_static(self) -> bool:
        return self._is_collidable_with_static
    
    @is_collidable_with_static.setter
    def is_collidable_with_static(self, value: bool) -> None:
        """
        Set the 'is_collidable_with_static' attribute of the 'Physic' class to a boolean value indicating whether the object is collidable with static objects or not.

        Args:
            value (bool): Indicates whether the object is collidable with static objects or not.

        Returns:
            None
        """
        self._is_collidable_with_static = value
    
    @property
    def is_collidable_with_dynamic(self) -> bool:
        return self._is_collidable_with_dynamic
    
    @is_collidable_with_dynamic.setter
    def is_collidable_with_dynamic(self, value: bool) -> None:
        """
        Setter method for the 'is_collidable_with_dynamic' attribute of the 'Physic' class.

        Args:
            value: A boolean value indicating whether the object is collidable with dynamic objects or not.

        Returns:
            None
        """
        self._is_collidable_with_dynamic = value
    
    @staticmethod
    def _check_and_convert_to_float64(value: Union[float, int, Any]) -> np.float64:
        """
        Check if the input value is a float or an integer, and if not, convert it to a np.float64 value.

        Args:
        - value: The input value that needs to be checked and converted to np.float64.

        Returns:
        - The input value as np.float64 if it is already a float or an integer, or converts it to np.float64 and returns it.
        """
        if isinstance(value, (float, int)):
            return value
        else:
            return np.float64(value)
    
    def start_flight(self, speed: Union[float, int, Any], mass: Union[float, int, Any], angle: Union[float, int, Any]) -> Tuple[np.float64, np.float64, np.float64, list[np.float64], list[np.float64]]:
        """_summary_

        Args:
            speed (Union[float, int, Any]): _description_
            mass (Union[float, int, Any]): _description_
            angle: (Union[float, int, Any]): _description_
        Returns:
            Tuple[np.float64, np.float64, np.float64]: _description_
        """
        # Constants
        g: np.float16 = np.float16(9.8)  # Acceleration due to gravity
        time_step: np.float16 =np.float16(0.01)  # Time step for numerical integration (adjust for accuracy)
        air_resistance: np.float64 = np.float64(0.001)  # coefficient of air 
        
        # Initial conditions
        x: np.float64 = np.float64(0.0)
        y: np.float64 = np.float64(0.0)
        
        # Lists to store trajectory data
        trajectory_x: list[np.float64] = [x]
        trajectory_y: list[np.float64] = [y]
            
        launch_angle = LaunchAngle()
        launch_angle.angle = np.radians(angle)
        
        self.speed = speed
        self.mass = mass
   
        vx = self.speed * np.cos(launch_angle.angle)
        vy = self.speed * np.sin(launch_angle.angle)
        while y >= 0:
            # Calculate speed components
            v = np.sqrt(vx ** 2  + vy ** 2)
            dx = (air_resistance * vx * v) * time_step
            dy = (vy * v - g) * time_step
            
            # Update position
            x += dx
            y += dy
            
            # Update speedsrc/physic.py
            vx -= (air_resistance * vx * v) / vx * time_step
            vy -= (g + (air_resistance * vy * v)) * time_step
            
            #Append current position to trajectory lists
            trajectory_x.append(x)
            trajectory_y.append(y)
            
        self.trajectory_x = trajectory_x
        self.trajectory_y = trajectory_y
        
        horizontal_speed = self.speed * np.cos(launch_angle.angle)
        vertical_speed = self.speed * np.sin(launch_angle.angle) 
        
        self.flight_time = (2 * vertical_speed) / g 
        
        self.max_height = (np.power(vertical_speed, 2)) / (2 * g)
        self.distance = horizontal_speed * self.flight_time
        
        return [self.flight_time, self.max_height, self.distance, trajectory_x, trajectory_y]
    
    