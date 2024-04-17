import pygame
from config.map import * 
from src.helpers import *

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
		

	def show_text(self,exp,x,y, ui_bg):
		text_surf = self.font.render(str((exp)),False,TEXT_COLOR)
		text_rect = text_surf.get_rect(bottomright = (x,y))

		pygame.draw.rect(self.display_surface,ui_bg,text_rect.inflate(20,20))
		self.display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3)
	

	def show_coins(self,coins):
		text_surf = self.font.render(str(f'Coins:{coins}'),False,'black')
		x = 10
		y = 40
		text_rect = text_surf.get_rect(topleft = (x,y))
		self.display_surface.blit(text_surf,text_rect)

	def display(self,player):
		if player.energy<=ENERGY_BLINK_THRESHOLD:
			if wave_value()>0:
				self.show_bar(player.energy,player.stats['energy'],ENERGY_COLOR)
			else:
				self.show_bar(player.energy,player.stats['energy'],ENERGY_COLOR_LIGHT)
		else:
			self.show_bar(player.energy,player.stats['energy'],ENERGY_COLOR)

		self.show_coins(str(round(player.coins,0)))

		self.show_text('Level:'+str(player.level), self.display_surface.get_size()[0] - 20, 40, UI_BG_COLOR)
		if player.timer<=TIMER_BLINK_THRESHOLD:
			if wave_value():
				self.show_text('Timer: '+str(player.timer), self.display_surface.get_size()[0] - 20, 90, UI_BG_COLOR)
			else:
				self.show_text('Timer: '+str(player.timer), self.display_surface.get_size()[0] - 20, 90, UI_BG_COLOR_LIGHT)
		else:
			self.show_text('Timer: '+str(player.timer), self.display_surface.get_size()[0] - 20, 90, UI_BG_COLOR)

		yulu = round(player.stats['yulu_bill'],0)
		if player.coins - yulu <= YULU_BLINK_THRESHOLD and player.yulu==True:
			if wave_value()>0:
				self.show_text('Yulu Bill:'+str(yulu), self.display_surface.get_size()[0] - 20, self.display_surface.get_size()[1] - 20, UI_BG_COLOR)
			else:
				self.show_text('Yulu Bill:'+str(yulu), self.display_surface.get_size()[0] - 20, self.display_surface.get_size()[1] - 20, UI_BG_COLOR_LIGHT)
		else:
			self.show_text('Yulu Bill:'+str(yulu), self.display_surface.get_size()[0] - 20, self.display_surface.get_size()[1] - 20, UI_BG_COLOR)

		if player.started==False:
			self.show_text(str(LEVELS[int(player.level)-1]['first_message_on_top']), WIDTH//2, 40, UI_BG_COLOR)
		if player.started:
		    self.show_text(str(LEVELS[int(player.level)-1]['second_message_on_top']), WIDTH//2, 40, UI_BG_COLOR)