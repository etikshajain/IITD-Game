import pygame 
from settings import *

class Rajdhani(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.image.load('../graphics/buildings/rajdhani.jpg').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)