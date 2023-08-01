import sys
from src.physic import Physic
 
print(sys.version)



ph = Physic()

fl_time,mx_height,distance, trajectory_x, trajectory_y = ph.start_flight(10.0, 10.0, 45.0)
# Output result values
print(fl_time)
print(mx_height)
print(distance)

# Output trajectory points
for x, y in zip(trajectory_x, trajectory_y):
    print(f"x: {x:.2f}, y: {y:.2f}")