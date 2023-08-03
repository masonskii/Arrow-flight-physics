import numpy as np
import matplotlib.pyplot as plt


from src.Arrow import Arrow
from src.Bow import Bow
from src.Physic.Physic import Physic
class PhysicModel(Physic):
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

    def __str__(self) -> str:
        return (f"flight time = {self.state[0]}, max height = {self.state[1]} distance = {self.state[2]}")
    
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

    def shot(self, x0: np.int64, y0: np.int64, arrow: Arrow, bow: Bow) -> None:
        time_step: np.float64 = np.float64(0.00001)
        
        # Lists to store trajectory data
        self.trajectory_x.append(x0)
        self.trajectory_y.append(y0)

        self.angle = np.radians(bow.angle)

        self.v = self.calculate_velocity(arrow.mass, bow.force)
        self.M = arrow.mass

        vx: np.float64 = self.v * np.cos(self.angle)
        vy:np.float64 = self.v * np.sin(self.angle)
        
        x: np.float64 = x0
        y: np.float64 = y0
        while not self.check_collision(y):

            # Calculate speed components
            v = np.sqrt(vx ** 2 + vy ** 2)
            dx = (arrow.air_resistance * vx * v) * time_step
            dy = (vy * v - self.g) * time_step

            # Update position
            x += dx
            y += dy

            # Update speed
            vx -= (arrow.air_resistance * vx * v) / vx * time_step
            vy -= (self.g + (arrow.air_resistance * vy * v)) * time_step

            # Append current position to trajectory lists
            self.trajectory_x.append(x)
            self.trajectory_y.append(y)
            """
            #TODO::  next step in the function 
            if self.check_collision(y + vy):
                # check next points
                v = np.sqrt(vx ** 2 + vy ** 2)
                dx = (arrow.air_resistance * vx * v) * time_step
                dy = (vy * v - self.g) * time_step
                self.trajectory_x.append(x + dx)
                self.trajectory_y.append(y + dy)
            """

        horizontal_speed: np.float64 = self.v * np.cos(self.angle)
        vertical_speed:  np.float64 = self.v * np.sin(self.angle)

        self.state[0] = (2 * vertical_speed) / self.g

        self.state[1] = (np.power(vertical_speed, 2)) / (2 * self.g)
        self.state[2] = horizontal_speed * self.state[0]

    @staticmethod
    def check_collision(y: np.float64) -> bool:
        if y <= 0 :
            return True
        return False