import sys
from src.ArrowFlying import ArrowFlying
 
print(sys.version)



arrow = ArrowFlying()

fl_time, mx_height, distance, trajectory_x, trajectory_y = arrow.start_flight(70.0, 0.5, 80.0)
# Output result values
print(fl_time)
print(mx_height)
print(distance)

# Output trajectory points
for x, y in zip(trajectory_x, trajectory_y):
    print(f"x: {x:.2f}, y: {y:.2f}")