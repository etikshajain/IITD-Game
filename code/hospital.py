import pygame 
from settings import *

class Hospital(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.name = 'hospital'
		self.image = pygame.image.load('../graphics/buildings/hospi.jpg').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)