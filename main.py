import sys
import random
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