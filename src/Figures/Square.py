from .Figure import Figure

class Square(Figure):
    def __init__(self, side):
        super().__init__()
        self.add_side(side)

    def perimeter(self):
        return 4 * self.sides[0]

    def area(self):
        return self.sides[0] ** 2   
    