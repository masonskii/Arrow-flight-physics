This is a physics simulation library that can be used to simulate the motion of objects in 2D. The library includes classes for representing physical objects, such as balls, blocks, and springs. It also includes methods for calculating the forces acting on objects, such as gravity, friction, and air resistance. The library can be used to simulate a variety of physical phenomena, such as projectile motion, bouncing balls, and falling objects.

To use the library, first create an instance of the Physic class. Then, you can set the mass, speed, acceleration, position, radius, color, state, and collision properties of the object. Once you have created the object, you can use the start_flight() method to simulate its motion. The start_flight() method takes three arguments: the speed of the object, the mass of the object, and the launch angle. The method returns a tuple containing the flight time, maximum height, distance traveled, and a list of x and y coordinates of the object's trajectory.

Here is an example of how to use the library to simulate the motion of a projectile:

## Getting Started

To get started with the simulation, you will need to install the following dependencies:

* Python 3.6 or higher
* NumPy
* Matplotlib

```py
import sys
from src.Arrow import Arrow
from src.Bow import Bow
from src.Physic.Model import PhysicModel

print(sys.version)

arrow = Arrow()
bow = Bow(45.0)
start_points = [0, 1]
model = PhysicModel()
model.shot(start_points[0], start_points[1], arrow=arrow, bow=bow)
print(model.__str__())
model.draw()
```

This code will create a Physic object and set its mass, speed, and launch angle. Then, it will start the simulation and print the results. The results will include the flight time, maximum height, distance traveled, and a list of x and y coordinates of the object's trajectory.

## Physics Engine

The physics engine in this simulation uses the following equations to simulate the motion of objects:

* **Newton's Second Law:** The acceleration of an object is equal to the net force acting on the object divided by the mass of the object.
* **Projectile Motion:** The motion of a projectile is governed by the equations of projectile motion.
* **Hooke's Law:** The force exerted by a spring is proportional to the extension of the spring.

## License

The simulation is licensed under the MIT License.