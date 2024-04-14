import pygame
from settings import * 

class UI:
	def __init__(self):
		
		# general 
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

		# bar setup
		self.energy_bar_rect = pygame.Rect(10,10,ENERGY_BAR_WIDTH,BAR_HEIGHT)


	def show_bar(self,current,max_amount,color):
		energy_bar_rect = pygame.Rect(10,10,ENERGY_BAR_WIDTH,BAR_HEIGHT)
		# draw bg 
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,energy_bar_rect)

		# converting stat to pixel
		ratio = current / max_amount
		current_width = energy_bar_rect.width * ratio
		current_rect = energy_bar_rect.copy()
		current_rect.width = current_width

		# drawing the bar
		pygame.draw.rect(self.display_surface,color,current_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,energy_bar_rect,3)
		

	def show_text(self,exp,x,y):
		text_surf = self.font.render(str((exp)),False,TEXT_COLOR)
		text_rect = text_surf.get_rect(bottomright = (x,y))

		pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20))
		self.display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3)
	

	def show_coins(self,coins):
		text_surf = self.font.render(str(f'Coins:{coins}'),False,'black')
		x = 10
		y = 40
		text_rect = text_surf.get_rect(topleft = (x,y))
		self.display_surface.blit(text_surf,text_rect)

	def display(self,player):
		self.show_bar(player.energy,player.stats['energy'],ENERGY_COLOR)
		self.show_coins(player.stats['coins'])

		self.show_text('Level:'+str(player.stats['level']), self.display_surface.get_size()[0] - 20, 40)
		self.show_text('Yulu Bill:'+str(player.stats['yulu_bill']), self.display_surface.get_size()[0] - 20, self.display_surface.get_size()[1] - 20)