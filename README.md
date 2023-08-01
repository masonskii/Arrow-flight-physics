# Arrow-flight-physics

Arrow flight physics

This is a physics library that can be used to simulate the motion of objects. It includes classes for representing physical objects, such as balls and projectiles, as well as methods for calculating their motion.

The library is written in Python and uses the NumPy library for numerical calculations. It is designed to be easy to use and understand, with a clean and well-documented API.

To get started with the library, you can create a new object of the `Physic` class. This class represents a physical object and has properties such as mass, speed, acceleration, position, radius, color, state, and collision properties.

You can then use the methods of the `Physic` class to calculate the motion of the object. For example, the `start_flight` method can be used to calculate the trajectory of a projectile.

The following code snippet shows how to use the `Physic` class to calculate the trajectory of a projectile:

```python
import physic

ph = physic.Physic()

fl_time,mx_height,distance, trajectory_x, trajectory_y = ph.start_flight(10.0, 10.0, 45.0)
# Output result values
print(fl_time)
print(mx_height)
print(distance)

# Output trajectory points
for x, y in zip(trajectory_x, trajectory_y):
    print(f"x: {x:.2f}, y: {y:.2f}")
```

This code will create a new object of the `Physic` class and then use the `start_flight` method to calculate the trajectory of a projectile that is launched with a speed of 10.0 meters per second and an angle of 45 degrees. The results of the calculation will be printed to the console.
