import pygame 
from settings import *

class Road(pygame.sprite.Sprite):
	def __init__(self,pos,groups, dir):
		super().__init__(groups)
		if dir:
			self.image = pygame.image.load('../graphics/road/road_v_64.jpg').convert_alpha()
		else:
			self.image = pygame.image.load('../graphics/road/road_h_64.jpg').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)