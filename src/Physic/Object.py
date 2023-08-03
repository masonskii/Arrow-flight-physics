from .Physic import Physic



class Object(Physic):
    """
    This class represents an object with physics properties.
    
    Attributes:
        None
    
    Methods:
        fly(): Subclasses of Object should implement the 'fly' method.
        move(): Subclasses of Object should implement the 'move' method.
        check_collision(obj: object) -> bool: Subclasses of Object should implement the 'check_collision' method.
    """
    def __init__(self) -> None:
        super().__init__()

    def fly(self) -> None:
        raise NotImplementedError("Subclasses of Object should implement the 'fly' method.")
    
    def move(self) -> None:
        raise NotImplementedError("Subclasses of Object should implement the 'move' method.")
    
    def check_collision(self, obj: object) -> bool:
        raise NotImplementedError("Subclasses of Object should implement the 'check_collision' method.")