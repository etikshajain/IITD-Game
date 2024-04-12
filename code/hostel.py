import pygame 
from settings import *

class Hostel(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.image.load('../graphics/hostel/hostell_192.jpg').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)