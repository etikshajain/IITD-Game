import pygame 
from settings import *

class Bharti(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.name = 'bharti'
		self.image = pygame.image.load('../graphics/buildings/bharti.jpg').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)