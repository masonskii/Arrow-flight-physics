from src.Physic.Physic import AbstractPhysic
from src.Color import Color
from src.Enums import ObjectState


import pytest

class TestAbstractPhysic:
    # Tests that all properties can be set and retrieved with valid values
    def test_set_and_get_all_properties_with_valid_values(self):
        obj = AbstractPhysic()
        obj.M = 10.0
        obj.v = 20.0
        obj.a = 30.0
        obj.position = 40.0
        obj.r = 50.0
        obj.S = 60.0
        obj.V = 70.0
        obj.p = 80.0
        obj.N = 90.0
        obj.E = 100.0
        obj.F = 110.0
        obj.pulse = 120.0
        obj.freq = 130.0
        obj.angle = 140.0
        obj.color = Color(255, 255, 255)
        obj.state = ObjectState.DYNAMIC
        obj.is_collision = True
        obj.is_collision_with_static = True
        obj.is_collision_with_dynamic = True
        assert obj.M == 10.0
        assert obj.v == 20.0
        assert obj.a == 30.0
        assert obj.position == 40.0
        assert obj.r == 50.0
        assert obj.S == 60.0
        assert obj.V == 70.0
        assert obj.p == 80.0
        assert obj.N == 90.0
        assert obj.E == 100.0
        assert obj.F == 110.0
        assert obj.pulse == 120.0
        assert obj.freq == 130.0
        assert obj.angle == 140.0
        assert obj.color == Color(255, 255, 255)
        assert obj.state == ObjectState.DYNAMIC
        assert obj.is_collision == True
        assert obj.is_collision_with_static == True
        assert obj.is_collision_with_dynamic == True

    # Tests that the color property can be set and retrieved with a valid Color object
    def test_set_and_get_color_with_valid_value(self):
        obj = AbstractPhysic()
        obj.color = Color(255, 255, 255)
        assert obj.color == Color(255, 255, 255)

    # Tests that the state property can be set and retrieved with a valid ObjectState object
    def test_set_and_get_state_with_valid_value(self):
        obj = AbstractPhysic()
        obj.state = ObjectState.DYNAMIC
        assert obj.state == ObjectState.DYNAMIC

    # Tests that the is_collision property can be set and retrieved with a valid boolean value
    def test_set_and_get_is_collision_with_valid_value(self):
        obj = AbstractPhysic()
        obj.is_collision = True
        assert obj.is_collision == True