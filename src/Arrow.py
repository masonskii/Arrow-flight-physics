import numpy as np
import matplotlib.pyplot as plt

from typing import Any, Tuple, Union

from src.Physic.Object import Object

class Arrow(Object):
    def __init__(self) -> None:
        super().__init__()

        self._state: list = np.zeros(3).tolist()
        self._trajectory_x = []
        self._trajectory_y = []

    @property
    def state(self) -> list:
        return self._state
    
    @state.setter
    def state(self, state: list) -> None:
        if not isinstance(state, list):
            raise TypeError('Expected ObjectState object')
        self._state = state

    @property
    def trajectory_x(self) -> list:
        return self._trajectory_x
    
    @trajectory_x.setter
    def trajectory_x(self, trajectory_x: list) -> None:
        if not isinstance(trajectory_x, list):
            raise TypeError('Expected list')
        self._trajectory_x = trajectory_x
        
    @property
    def trajectory_y(self) -> list:
        return self._trajectory_y
    
    @trajectory_y.setter
    def trajectory_y(self, trajectory_y: list) -> None:
        if not isinstance(trajectory_y, list):
            raise TypeError('Expected list')
        self._trajectory_y = trajectory_y

    def draw(self) -> None:
        plt.plot(self.trajectory_x)
        plt.plot(self.trajectory_y)
        plt.show()
    def draw_3d(self) -> None:
        ax = plt.figure().add_subplot(projection='3d')

        ax.plot(self.trajectory_x, self.trajectory_y,zs=0, zdir='z', label='trajectory in (x, y)')
        ax.legend()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
    def __str__(self) -> str:
        return (f"flight time = {self.state[0]}, max height = {self.state[1]} distance = {self.state[2]}")
    
    def fly(self, 
            speed: Union[float, int, Any],
            mass: Union[float, int, Any],
            angle: Union[float, int, Any]
    ) -> Tuple[
        np.float64, np.float64, np.float64, 
        list[np.float64], 
        list[np.float64]
    ]:
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

        self._trajectory_x = trajectory_x
        self._trajectory_y = trajectory_y
        self._state[0] = flight_time
        self._state[1] = max_height
        self._state[2] = distance

        return [flight_time, max_height, distance, trajectory_x, trajectory_y]
