from src.physic import Color


import pytest

class TestColor:
    # Tests that a Color instance is created with valid RGB values
    def test_valid_RGB_values(self):
        color = Color(255, 0, 0)
        assert color.r == 255
        assert color.g == 0
        assert color.b == 0


    # Tests that the RGB values of a Color object can be accessed correctly
    def test_color_rgb_values(self):
        color = Color(255, 0, 128)
        assert color.r == 255
        assert color.g == 0
        assert color.b == 128


    # Tests that a TypeError is raised when creating a Color object with missing RGB values
    def test_missing_rgb_values(self):
        with pytest.raises(TypeError):
            Color(255, 0)


    # Tests that a TypeError is raised when creating a Color object with RGB values outside the valid range (0-255)
    def test_invalid_color_values(self):
        with pytest.raises(TypeError):
            Color(256, 0, 0)
            Color(0, 256, 0)
            Color(0, 0, 256)
            Color(-1, 0, 0)
            Color(0, -1, 0)
            Color(0, 0, -1)


    # Tests that creating a Color object with non-integer RGB values raises a TypeError
    def test_non_integer_RGB_values(self):
        with pytest.raises(TypeError):
            Color(1, 2, 3.5)


    # Tests that two Color objects with the same RGB values are equal
    def test_color_equality(self):
        c1 = Color(255, 0, 0)
        c2 = Color(255, 0, 0)
        assert c1 == c2


    # Tests that the string representation of a Color object matches the expected format.
    def test_color_string_representation(self):
        color = Color(255, 0, 128)
        assert str(color) == 'Color(r=255, g=0, b=128)'


    # Tests that the RGB values of a Color object are immutable
    def test_immutable_rgb_values(self):
        color = Color(255, 0, 0)
        with pytest.raises(AttributeError):
            color.r = 0
        with pytest.raises(AttributeError):
            color.g = 0
        with pytest.raises(AttributeError):
            color.b = 0


    # Tests that the Color object does not have any additional attributes or methods beyond those defined in the class.
    def test_no_additional_attributes_or_methods(self):
        color = Color(255, 255, 255)
        assert not hasattr(color, '__dict__')
        assert not hasattr(color, '__weakref__')
        assert not hasattr(color, '__module__')
        assert not hasattr(color, '__doc__')
        assert not hasattr(color, '__annotations__')
        assert not hasattr(color, '__new__')
        assert not hasattr(color, '__init__')
        assert not hasattr(color, '__repr__')
        assert not hasattr(color, '__hash__')


    # Tests that the hash value of a Color object is consistent with its RGB values
    def test_hash_value_consistent_with_RGB(self):
        c1 = Color(255, 0, 0)
        c2 = Color(255, 0, 0)
        c3 = Color(0, 255, 0)
        assert hash(c1) == hash(c2)
        assert hash(c1) != hash(c3)

