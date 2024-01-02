import pygame
import abc

class AbstractGameObj(abc.ABC):
    
    name: str
    image_name: str
    image: pygame.surface.Surface
    type_name: str
    def __init__(self, name: str, texture_registry: str, image_name: str=""): pass
    def render(self): pass