import sys
from src.Arrow import Arrow
print(sys.version)



arrow = Arrow()

fl_time, mx_height, distance, trajectory_x, trajectory_y = arrow.fly(50.0, 0.2, 45.0)

print(arrow.__str__())
arrow.draw()