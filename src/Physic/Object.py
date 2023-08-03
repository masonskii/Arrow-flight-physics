from .Physic import Physic



class Object(Physic):
    def __init__(self) -> None:
        super().__init__()

    def fly(self) -> None:
        raise NotImplementedError("Subclasses of Object should implement the 'fly' method.")
    
    def move(self) -> None:
        raise NotImplementedError("Subclasses of Object should implement the 'move' method.")
    
    def check_collision(self, obj: object) -> bool:
        raise NotImplementedError("Subclasses of Object should implement the 'check_collision' method.")