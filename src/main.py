import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('IIT Delhi')
		self.clock = pygame.time.Clock()

		# Create a level
		self.level = Level()
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if self.level.playing==False:
					self.level.start_button.handle_event(event)

				elif self.level.player.completed:
					self.level.next_level_button.handle_event(event)
					self.level.quit_button.handle_event(event)

				elif self.level.player.failed:
					self.level.restart_button.handle_event(event)
					self.level.quit_button.handle_event(event)

				elif self.level.player.pause:
					self.level.restart_button.handle_event(event)
					self.level.resume_button.handle_event(event)
					self.level.quit_button.handle_event(event)

				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('#9be650')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()	