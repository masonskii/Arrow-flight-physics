import pytest

import src

def test_happy_path_acceleration_set(self):
    """Tests that acceleration returns the correct value when it has been set 
    """
    obj = src.physic.Physic()
    obj.acceleration = 5.0
    assert obj.acceleration == 5.0
    
def test_edge_case_acceleration_not_set(self):
    """Tests that acceleration returns 0.0 when it has not been set
    """
    obj = src.physic.Physic()
    assert obj.acceleration == 0.0
    
def test_edge_case_acceleration_negative(self):
    """Tests that acceleration returns 0.0 when it is set to a negative value
    """
    obj = src.physic.Physic()
    obj.acceleration = -5.0
    assert obj.acceleration == 0.0
    
def test_other_acceleration_large_value(self):
    """Tests that setting acceleration to a very large value does not cause any issues
    """
    obj = src.physic.Physic()
    obj.acceleration = 1e10
    assert obj.acceleration == 1e10
    
def test_other_acceleration_small_value(self):
    """Tests that setting acceleration to a very small value does not cause any issues
    """
    obj = src.physic.Physic()
    obj.acceleration = 1e-10
    assert obj.acceleration == 1e-10
    
def test_other_acceleration_non_float_value(self):
    """ Tests that setting acceleration to a non-float value raises a TypeError
    """
    obj = src.physic.Physic()
    with pytest.raises(TypeError):
        obj.acceleration = 'not a float'