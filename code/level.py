from typing import Iterable
import pygame
from pygame.sprite import AbstractGroup 
from settings import *
from player import Player
from road import Road
from hostel import Hostel
from yulu_stand import YuluStand
from tree import Tree
from bank import Bank
from tennis import Tennis
from cycle import Cycle
from rajdhani import Rajdhani
from sac import Sac
from hospital import Hospital
from football import Football
from basketball import Basketball
from racing import Racing
from amul import Amul
from bharti import Bharti
from mainb import MainB
from lhc import Lhc
from biotech import Biotech
from redsq import RedSq
from lib import Lib
from exhall import Exhall
from shop import Shop
from guesthouse import Guesthouse
from debug import debug

class Level:
    def __init__(self):

        # get the display surface 
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.player_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'h':
                    Road((x,y),[self.visible_sprites],False)
                if col == 'v':
                    Road((x,y),[self.visible_sprites],True)
                if col == 'G':
                    Hostel((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'Y':
                    YuluStand((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 't':
                    Tree((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'T':
                    Tennis((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'B':
                    Bank((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'R':
                    Rajdhani((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'C':
                    Cycle((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'S':
                    Sac((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'H':
                    Hospital((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'F':
                    Football((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'Bb':
                    Basketball((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'Rr':
                    Racing((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'A':
                    Amul((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'Cs':
                    Bharti((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'M':
                    MainB((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'Lh':
                    Lhc((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'Q':
                    RedSq((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'P':
                    Biotech((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'L':
                    Lib((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'E':
                    Exhall((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'I':
                    Shop((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'X':
                    Guesthouse((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.player_sprites, self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.player_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        # debug(player.rect.centerx+self.offset.x)
        debug(self.offset)
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)