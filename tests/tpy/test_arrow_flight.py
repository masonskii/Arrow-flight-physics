from src.Arrow import ArrowFlying
import numpy as np


import pytest

class TestArrowFlying:
    # Tests that start_flight method returns valid output with valid input values
    def test_start_flight_valid_input(self):
        arrow = ArrowFlying()
        result = arrow.start_flight(10, 0.1, 45)
        assert isinstance(result[0], np.float64)
        assert isinstance(result[1], np.float64)
        assert isinstance(result[2], np.float64)
        assert isinstance(result[3], list)
        assert isinstance(result[4], list)

    # Tests that start_flight method returns flight time greater than zero
    def test_start_flight_flight_time_greater_than_zero(self):
        arrow = ArrowFlying()
        result = arrow.start_flight(10, 0.1, 45)
        assert result[0] > 0

    # Tests that start_flight method returns max height greater than zero
    def test_start_flight_max_height_greater_than_zero(self):
        arrow = ArrowFlying()
        result = arrow.start_flight(10, 0.1, 45)
        assert result[1] > 0

    # Tests that start_flight method returns distance greater than zero
    def test_start_flight_distance_greater_than_zero(self):
        arrow = ArrowFlying()
        result = arrow.start_flight(10, 0.1, 45)
        assert result[2] > 0

    # Tests that start_flight method returns trajectory_x list with at least one element
    def test_start_flight_trajectory_x_has_at_least_one_element(self):
        arrow = ArrowFlying()
        result = arrow.start_flight(10, 0.1, 45)
        assert len(result[3]) >= 1

    # Tests that start_flight method returns trajectory_y list with at least one element
    def test_start_flight_trajectory_y_has_at_least_one_element(self):
        arrow = ArrowFlying()
        result = arrow.start_flight(10, 0.1, 45)
        assert len(result[4]) >= 1

    # Tests that start_flight method returns valid output with zero speed
    def test_start_flight_zero_speed(self):
        arrow = ArrowFlying()
        result = arrow.start_flight(0, 0.1, 45)
        assert isinstance(result[0], np.float64)
        assert isinstance(result[1], np.float64)
        assert isinstance(result[2], np.float64)
        assert isinstance(result[3], list)
        assert isinstance(result[4], list)

    # Tests that start_flight method returns valid output with zero mass
    def test_start_flight_zero_mass(self):
        arrow = ArrowFlying()
        result = arrow.start_flight(10, 0, 45)
        assert isinstance(result[0], np.float64)
        assert isinstance(result[1], np.float64)
        assert isinstance(result[2], np.float64)
        assert isinstance(result[3], list)
        assert isinstance(result[4], list)

    # Tests that start_flight method returns valid output with zero angle
    def test_start_flight_zero_angle(self):
        arrow = ArrowFlying()
        result = arrow.start_flight(10, 0.1, 0)
        assert isinstance(result[0], np.float64)
        assert isinstance(result[1], np.float64)
        assert isinstance(result[2], np.float64)
        assert isinstance(result[3], list)
        assert isinstance(result[4], list)