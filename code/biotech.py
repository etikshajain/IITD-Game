import pygame 
from settings import *

class Biotech(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.name = 'biotech'
		self.image = pygame.image.load('../graphics/buildings/park.jpg').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)