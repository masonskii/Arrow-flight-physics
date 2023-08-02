from enum import Enum

class ObjectState(Enum):
    '''
    ObjectState is an enumeration class that represents the state of an object.
    
    Attributes:
        STATIC (int): represents a static object.
        DYNAMIC (int): represents a dynamic object.
        MOVING (int): represents a moving object.
        JUMPING (int): represents a jumping object.
        FALLING (int): represents a falling object.
        EXPLODING (int): represents an exploding object.
        INACTIVE (int): represents an inactive object.
        ACTIVE (int): represents an active object.
        HIDDEN (int): represents a hidden object.
        DESTROYED (int): represents a destroyed object.
    '''
    STATIC = 1
    DYNAMIC = 2
    MOVING = 3
    JUMPING = 4
    FALLING = 5
    EXPLODING = 6
    INACTIVE = 7
    ACTIVE = 8
    HIDDEN = 9
    DESTROYED = 10