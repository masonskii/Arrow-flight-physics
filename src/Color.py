from dataclasses import dataclass

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
    