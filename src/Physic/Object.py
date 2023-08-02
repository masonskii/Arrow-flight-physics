from .Physic import Physic



class Object(Physic):
    def __init__(self) -> None:
        super().__init__()

    def draw(self) -> None:
        raise NotImplementedError("Subclasses of Figure should implement the 'draw' method.")
    
    def draw_3d(self) -> None:
        raise NotImplementedError("Subclasses of Figure should implement the 'draw' method.")
    def fly(self) -> None:
        raise NotImplementedError("Subclasses of Figure should implement the 'fly' method.")
    
    def move(self) -> None:
        raise NotImplementedError("Subclasses of Figure should implement the 'move' method.")
    