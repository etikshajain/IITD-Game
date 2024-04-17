import pygame 
from config.map import *
from src.helpers import import_folder, wave_value

class Building(pygame.sprite.Sprite):
    def __init__(self,pos,groups, name, graphic):
        super().__init__(groups)
        self.name = name
        self.image = pygame.image.load(graphic).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)