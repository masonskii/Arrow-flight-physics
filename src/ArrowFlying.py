import numpy as np

from typing import Any, Tuple, Union

from src.AbstractPhysic import AbstractPhysic

class ArrowFlying(AbstractPhysic):
    def __init__(self) -> None:
        super().__init__()
        
    def start_flight(self, speed: Union[float, int, Any],
                     mass: Union[float, int, Any],
                     angle: Union[float, int, Any]
                     ) -> Tuple[np.float64, np.float64, np.float64, list[np.float64], list[np.float64]]:
        # Constants
        g: np.float16 = np.float16(9.8)  # Acceleration due to gravity
        
        # Time step for numerical integration (adjust for accuracy)
        time_step: np.float16 = np.float16(0.001)
        air_resistance: np.float64 = np.float64(0.001)  # coefficient of air

        # Initial conditions
        x: np.float64 = np.float64(0.0)
        y: np.float64 = np.float64(1.5)

        # Lists to store trajectory data
        trajectory_x: list[np.float64] = [x]
        trajectory_y: list[np.float64] = [y]
        
        self.angle = np.radians(angle)

        self.v = speed
        self.M = mass

        vx = self.v * np.cos(self.angle)
        vy = self.v * np.sin(self.angle)
        while y >= 0:
            
            # Calculate speed components
            v = np.sqrt(vx ** 2 + vy ** 2)
            dx = (air_resistance * vx * v) * time_step
            dy = (vy * v - g) * time_step

            # Update position
            x += dx
            y += dy

            # Update speed
            vx -= (air_resistance * vx * v) / vx * time_step
            vy -= (g + (air_resistance * vy * v)) * time_step

            # Append current position to trajectory lists
            trajectory_x.append(x)
            trajectory_y.append(y)

        horizontal_speed = self.v * np.cos(self.angle)
        vertical_speed = self.v * np.sin(self.angle)

        flight_time = (2 * vertical_speed) / g

        max_height = (np.power(vertical_speed, 2)) / (2 * g)
        distance = horizontal_speed * flight_time

        return [flight_time, max_height, distance, trajectory_x, trajectory_y]
