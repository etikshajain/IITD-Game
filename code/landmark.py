import pygame 
from settings import *

class Landmark(pygame.sprite.Sprite):
	def __init__(self,pos,groups, text):
		super().__init__(groups)
		self.name = 'landmark'
		font = pygame.font.SysFont(None, 32)  # Start with a default font size
		text_width, text_height = font.size(text)
		while text_width > TILESIZE or text_height > TILESIZE:
			font = pygame.font.SysFont(None, font.get_height() - 1)
			text_width, text_height = font.size(text)
		text_surface = font.render(text, True, 'black')
		self.rect = text_surface.get_rect(bottomright = pos)