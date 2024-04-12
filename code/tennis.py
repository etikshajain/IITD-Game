import pygame 
from settings import *

class Tennis(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.name = 'tennis'
		self.image = pygame.image.load('../graphics/grounds/tennis.jpg').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)