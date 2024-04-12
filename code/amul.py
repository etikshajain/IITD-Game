import pygame 
from settings import *

class Amul(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.name = 'amul'
		self.image = pygame.image.load('../graphics/buildings/amul.jpg').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)