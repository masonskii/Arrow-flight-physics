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
    
    