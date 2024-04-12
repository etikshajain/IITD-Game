import pygame 
from settings import *

class Football(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.name = 'football'
		self.image = pygame.image.load('../graphics/grounds/football.jpg').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)