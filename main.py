"""
This code snippet simulates the flight of an arrow shot from a bow using a physics model. It calculates the trajectory of the arrow and displays it in a graph.

Inputs:
- Arrow object: contains information about the arrow, such as mass and air resistance.
- Bow object: contains information about the bow, such as angle and force.
- Start points: a list with two integers representing the starting coordinates of the arrow.

Outputs:
- Flight time, max height, and distance of the arrow printed to the console.
- Graph of the arrow's trajectory displayed in a window.

Additional aspects:
- The physics model takes into account the mass and air resistance of the arrow, as well as the force and angle of the bow.
- The trajectory is calculated using a while loop that updates the position and speed of the arrow at each time step.
- The check_collision() method is used to determine if the arrow has hit the ground.
- The draw_3d() method can be used to display a 3D graph of the arrow's trajectory.

"""

import sys
import numpy as np
from src.Arrow import Arrow
from src.Bow import Bow
from src.Physic.Model import PhysicModel
from src.Color import Color
from ui.models.ui_main import Window
from ui.settings import *
print(sys.version)

arrow = Arrow()
bow = Bow(45.0)
start_points = [0, 1]
model = PhysicModel(arrow, bow)
model.shot(
    start_points[0],
    start_points[1],
)
window = Window(WIDTH, HEIGHT, "Window", Color(255,255,255),arrow,bow, 60)
window.draw_arrow(0, HEIGHT - 60, 50, 15, WIDTH - 100, HEIGHT - 60)
window.run()