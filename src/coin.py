import pygame 
from config.map import *

class Coin(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.name = 'coin'
        self.image = pygame.image.load('./assets/map_mode/coinn.jpg').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)