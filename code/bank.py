import pygame 
from settings import *

class Bank(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.image.load('../graphics/buildings/bank_128.jpg').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)