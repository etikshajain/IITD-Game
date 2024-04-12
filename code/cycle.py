import pygame 
from settings import *

class Cycle(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.name = 'cycle_shop'
		self.image = pygame.image.load('../graphics/buildings/cycle.jpg').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)