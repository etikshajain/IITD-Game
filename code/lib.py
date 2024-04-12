import pygame 
from settings import *

class Lib(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.name = 'library'
		self.image = pygame.image.load('../graphics/buildings/lib.jpg').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)