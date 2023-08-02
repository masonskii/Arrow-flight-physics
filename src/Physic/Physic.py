import numpy as np
from typing import Any, Union
from src.Enums.AngleEnum import AngleEnum
from src.Enums.ObjectState import ObjectState
from src.Color import Color
"""
This code defines a class named 'AbstractPhysic' that represents a physics object. The class contains private variables and their states, as well as setters and getters for each variable. 

The class has the following properties:
- mass: the mass of the object
- speed: the speed of the object
- acceleration: the acceleration of the object
- position: the position of the object
- radius: the radius of the object
- square: the square of the object
- volume: the volume of the object
- pulse: the pulse of the object
- strength: the strength of the object
- energy: the energy of the object
- capacity: the capacity of the object
- pressure: the pressure of the object
- frequency: the frequency of the object
- angle: the angle of the object

The class also has the following additional properties:
- color: the color of the object (expects a Color object)
- state: the state of the object (expects an ObjectState object)
- is_collision: a boolean indicating if there is a collision with any object
- is_collision_with_static: a boolean indicating if there is a collision with a static object
- is_collision_with_dynamic: a boolean indicating if there is a collision with a dynamic object

The class provides setters and getters for each property, allowing for easy manipulation of the object's attributes. Additionally, there is a static method '_check_and_convert_to_float64' that checks and converts input values to np.float64 type.

Note: The code assumes the existence of the Color and ObjectState classes, which are imported from external modules.
"""


class Physic:

    def __init__(self) -> None:

        # private variables
        self._mass: np.float64 = np.float64(0.0)
        self._speed: np.float64 = np.float64(0.0)
        self._acceleration: np.float64 = np.float64(0.0)
        self._position: np.float64 = np.float64(0.0)
        self._radius: np.float64 = np.float64(0.0)
        self._square: np.float64 = np.float64(0.0)
        self._volume: np.float64 = np.float64(0.0)
        self._pulse: np.float64 = np.float64(0.0)
        self._strength: np.float64 = np.float64(0.0)
        self._energy: np.float64 = np.float64(0.0)
        self._capacity: np.float64 = np.float64(0.0)
        self._pressure: np.float64 = np.float64(0.0)
        self._frequency: np.float64 = np.float64(0.0)
        self._angle: np.float64 = np.float64(0.0)

        self._color: Color = Color(0, 0, 0)

        # private variables states
        self._consistence: np.float64 = np.float64(0.0)
        self._moment_of_inertia: np.float64 = np.float64(0.0)
        self._moment_of_strength: np.float64 = np.float64(0.0)
        self._angular_momentum: np.float64 = np.float64(0.0)
        self._angle_change_rate: np.float64 = np.float64(0.0)
        self._angular_acceleration: np.float64 = np.float64(0.0)
        self._type_angle: AngleEnum = AngleEnum.ACUTE_ANGLE
        self._quantity_of_heat: np.float64 = np.float64(0.0)
        self._mech_work: np.float64 = np.float64(0.0)
        self._line_density: np.float64 = np.float64(0.0)
        self._surface_density: np.float64 = np.float64(0.0)
        self._state: ObjectState = ObjectState.STATIC
        self._is_collision: bool = False
        self._is_collision_with_static: bool = False
        self._is_collision_with_dynamic: bool = False

    @property
    def freq(self) -> np.float64:
        """ get frequency """
        return self._frequency

    @freq.setter
    def freq(self, value: np.float64) -> None:
        """ set frequency """
        self._frequency = self._check_and_convert_to_float64(value)

    @property
    def angle(self) -> np.float64:
        """ get angle """
        return self._angle

    @angle.setter
    def angle(self, value: np.float64) -> None:
        """ set angle """
        self._angle = self._check_and_convert_to_float64(value)

    @property
    def p(self) -> np.float64:
        """get pressure"""
        return self._pressure

    @p.setter
    def p(self, value: np.float64) -> None:
        """ set pressure """
        self._pressure = self._check_and_convert_to_float64(value)

    @property
    def N(self) -> np.float64:
        """ get capacity """
        return self._capacity

    @N.setter
    def N(self, value: np.float64) -> None:
        """set capacity"""
        self._capacity = self._check_and_convert_to_float64(value)

    @property
    def E(self) -> np.float64:
        """get energy"""
        return self._energy

    @E.setter
    def E(self, value: np.float64) -> None:
        """set energy"""
        self._energy = self._check_and_convert_to_float64(value)

    @property
    def F(self) -> np.float64:
        """get strength"""
        return self._strength

    @F.setter
    def F(self, value: np.float64) -> None:
        """set strength"""
        self._strength = self._check_and_convert_to_float64(value)

    @property
    def p(self) -> np.float64:
        """get pulse"""
        return self._pulse

    @p.setter
    def p(self, value: np.float64) -> None:
        """set pulse"""
        self._pulse = self._check_and_convert_to_float64(value)

    @property
    def V(self) -> np.float64:
        """get volume"""
        return self._volume

    @V.setter
    def V(self, value: np.float64) -> None:
        """set volume"""
        self._volume = self._check_and_convert_to_float64(value)

    @property
    def S(self) -> np.float64:
        """get square"""
        return self._square

    @S.setter
    def S(self, value: np.float64) -> None:
        """set square"""
        self._square = self._check_and_convert_to_float64(value)

    @property
    def M(self) -> np.float64:
        """get mass"""
        return self._mass

    @M.setter
    def M(self, value: np.float64) -> None:
        """set mass"""
        self._mass = self._check_and_convert_to_float64(value)

    @property
    def v(self) -> np.float64:
        """get speed"""
        return self._speed

    @v.setter
    def v(self, value: np.float64) -> None:
        """set speed"""
        self._speed = self._check_and_convert_to_float64(value)

    @property
    def a(self) -> np.float64:
        """get acceleration"""
        return self._acceleration

    @a.setter
    def a(self, value: np.float64) -> None:
        """set acceleration"""
        self._acceleration = self._check_and_convert_to_float64(value)

    @property
    def position(self) -> np.float64:
        """get position"""
        return self._position

    @position.setter
    def position(self, value: np.float64) -> None:
        """set position"""
        self._position = self._check_and_convert_to_float64(value)

    @property
    def r(self) -> np.float64:
        """get radius"""
        return self._radius

    @r.setter
    def r(self, value: np.float64) -> None:
        """set radius"""
        self._radius = self._check_and_convert_to_float64(value)

    @property
    def color(self) -> dict:
        """get color"""
        return self._color

    @color.setter
    def color(self, value: Color) -> None:
        """set color"""
        if not isinstance(value, Color):
            raise TypeError('Expected Color object')
        self._color = value

    @property
    def state(self) -> ObjectState:
        """get state"""
        return self._state

    @state.setter
    def state(self, value: ObjectState) -> None:
        """set state"""
        if not isinstance(value, ObjectState):
            raise TypeError('Expected ObjectState object')
        self._state = value

    @property
    def is_collision(self) -> bool:
        """get is_collision"""
        return self._is_collision

    @is_collision.setter
    def is_collision(self, value: bool) -> None:
        """set is_collision"""
        self._is_collision = value

    @property
    def is_collision_with_static(self) -> bool:
        return self._is_collision_with_static

    @is_collision_with_static.setter
    def is_collision_with_static(self, value: bool) -> None:
        self._is_collision_with_static = value

    @property
    def is_collision_with_dynamic(self) -> bool:
        return self._is_collision_with_dynamic

    @is_collision_with_dynamic.setter
    def is_collision_with_dynamic(self, value: bool) -> None:
        self._is_collision_with_dynamic = value

    @staticmethod
    def _check_and_convert_to_float64(value: Union[float, int, Any]) -> np.float64:
        if isinstance(value, (float, int)):
            return value
        else:
            return np.float64(value)
