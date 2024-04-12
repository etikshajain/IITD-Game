import pygame 
from settings import *

class Shop(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.name = 'shop'
		self.image = pygame.image.load('../graphics/buildings/ice.jpg').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)