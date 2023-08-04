import pygame
import numpy as np
from pygame.locals import *
from src.Color import Color
from src.Arrow import Arrow
from src.Bow import Bow
from src.Physic.Model import PhysicModel
from ui.settings import HEIGHT
class Figure:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self._speed: np.float64 =np.float64(10)
    @property
    def speed(self) -> None:
        return self._speed
    
    @speed.setter
    def speed(self, value: np.float64) -> None:
        self._speed = value

    def update(self, dest_x, dest_y,):
        if self.rect.x < dest_x:
            self.rect.x += self.speed
        elif self.rect.x > dest_x:
            self.rect.x -= self.speed
        
        if self.rect.y < dest_y:
            self.rect.y += self.speed
        elif self.rect.y > dest_y:
            self.rect.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x, self.rect.y, self.rect.width, self.rect.height))

class Window:
    def __init__(self, w: np.int64, h: np.int64, t: str, color: Color, arrow: Arrow, bow: Bow, fps:np.int64=60,) -> None:
        self._width: np.int64 = w
        self._height: np.int64 = h
        self._title: str = t
        self._FPS: np.int64 = fps
        self._is_running: bool = False
        self._color: Color = color
        self.clock = pygame.time.Clock()
        self._sub_obj: list[Figure] = []
        self._arrow: Arrow = arrow
        self._bow: Bow = bow
        self._model = PhysicModel(arrow, bow)
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height), HWSURFACE|DOUBLEBUF|RESIZABLE)
        pygame.display.set_caption(self.title)

    @property
    def sub_obj(self) -> list:
        return self._sub_obj
    @sub_obj.setter
    def sub_obj(self, value: list) -> None:
        self._sub_obj = value
    
    def rect_append(self, value: pygame.Rect) -> None:
        self._sub_obj.append(value)

    @property
    def fps(self) -> np.int64:
        return self._FPS
        
    @property
    def is_running(self) -> bool:
        return self._is_running
    
    @property
    def color(self) -> Color:
        return self._color

    @property
    def width(self) -> np.int64:
        return self._width
    
    @property
    def height(self) -> np.int64:
        return self._height
    
    @property
    def title(self) -> str:
        return self._title
    
    @width.setter
    def width(self, value: np.int64) -> None:
        self._width = value
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

    @height.setter
    def height(self, value: np.int64) -> None:
        self._height = value
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
    
    @title.setter
    def title(self, value: str) -> None:
        self._title = value
        pygame.display.set_caption(self.title)

    @is_running.setter
    def is_running(self, value: bool) -> None:
        self._is_running = value

    @fps.setter
    def fps(self, value: np.int64) -> None:
        self._FPS = value
        pygame.time.set_timer(pygame.USEREVENT, self.fps)

    @color.setter
    def color(self, value: Color) -> None:
        self._color = value
        self.screen.fill((self.color.r, self.color.g, self.color.b))
        pygame.display.flip()

    def draw_arrow(self, x0: np.float64, y0: np.float64,w: np.float64,h: np.float64, dest_x, dest_y) -> None:
        new_rect:pygame.Rect = Figure(x0, y0,w,h)
        self.rect_append(new_rect)

    def update(self, obj=None) -> None:
        if obj: 
            pygame.display.update(obj)
        else:
            pygame.display.update()
    
    def render(self) -> None:
        self.screen.fill((self.color.r, self.color.g, self.color.b))
        pygame.display.flip()

    def run(self) -> None:
        self.is_running = True
        v = self._model.calculate_velocity(self._model.arrow.mass, self._model.bow.force)
        vx = v*np.cos(self._model.bow.angle)
        vy = v*np.sin(self._model.bow.angle)
        while self.is_running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            self.screen.fill((self.color.r, self.color.g, self.color.b))
            pygame.draw.line(self.screen,(0,0,0),(0,self.height - 20),(self.width, self.height - 20),width=20)
            self._model.shot(0, 600 - 60)
            for obj in self.sub_obj:
                obj.update(self._model.trajectory_x[-1], self._model.trajectory_y[-1])
                obj.draw(self.screen)
            
            self.update()
            pygame.display.flip()

    def move(self, x: np.float64, y: np.float64) -> None:
        pass

    def close(self) -> None:
        pygame.quit()
    
    def __del__(self) -> None:
        self.close()
    
    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return self.title
    
    def __len__(self) -> int:
        return 0
    
    
