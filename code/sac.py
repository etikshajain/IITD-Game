import pygame 
from settings import *

class Sac(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.name = 'sac'
		self.image = pygame.image.load('../graphics/buildings/sac.jpg').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)