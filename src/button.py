import pygame 
from config.map import *

class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        self.rect = pygame.Rect(x-width/2, y-height/2, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        text_surface = pygame.font.Font(UI_FONT,UI_FONT_SIZE).render(self.text, True, 'green')
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()