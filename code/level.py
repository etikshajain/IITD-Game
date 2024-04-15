from typing import Iterable
import pygame
from pygame.sprite import AbstractGroup 
from settings import *
from player import Player
from road import Road
from dog import Dog
from coin import Coin
from landmark import Landmark
from building import Building
from ui import UI
from button import Button
import sys
from debug import debug

class Level:
    def __init__(self):
        # get the display surface 
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.player_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # player stats
        self.coins=STARTING_COINS
        self.level=1

        # sprite setup
        self.create_map()
        self.place_random_dogs()
        self.place_random_coins()

        # game status
        self.playing=False

        #button
        self.start_button = Button(WIDTH//2, 300, 200, 50, "Start", 'black', self.start_game)
        self.restart_button = Button(WIDTH//2, 300, 200, 50, "Restart", 'black', self.restart_game)
        self.quit_button = Button(WIDTH//2, 400, 200, 50, "Quit", 'black', self.quit_game)
        self.next_level_button = Button(WIDTH//2, 300, 300, 50, "Next Level", 'black', self.next_level_game)
        self.resume_button = Button(WIDTH//2, 500, 200, 50, "Resume", 'black', self.resume_game)

        #user interface
        self.ui = UI()

    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                # if col.isdigit():
                #     Landmark((x,y),[self.visible_sprites,self.obstacle_sprites], HOSTELS[int(col)])
                if col == 'h':
                    Road((x,y),[self.visible_sprites],False)
                if col == 'v':
                    Road((x,y),[self.visible_sprites],True)
                if col[0] == 'G':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'hostel'+str(col[1:]), '../graphics/hostel/hostell_192.jpg')
                if col == 'Y':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'yulu_stand', '../graphics/buildings/yulu_64.jpg')
                if col == 't':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'tree', '../graphics/tree/tree_50.jpg')
                if col == 'T':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'tennis', '../graphics/grounds/tennis.jpg')
                if col == 'B':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'bank', '../graphics/buildings/bank_128.jpg')
                if col == 'R':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'rajdhani', '../graphics/buildings/rajdhani.jpg')
                if col == 'C':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'cycle_shop', '../graphics/buildings/cycle.jpg')
                if col == 'S':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'sac', '../graphics/buildings/sac.jpg')
                if col == 'H':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'hospital', '../graphics/buildings/hospi.jpg')
                if col == 'F':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'football', '../graphics/grounds/football.jpg')
                if col == 'Bb':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'basketball', '../graphics/grounds/bb.jpg')
                if col == 'Rr':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'racing', '../graphics/grounds/racing.jpg')
                if col == 'A':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'amul', '../graphics/buildings/amul.jpg')
                if col == 'Cs':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'bharti', '../graphics/buildings/bharti.jpg')
                if col == 'M':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'main_building', '../graphics/buildings/main.jpg')
                if col == 'Lh':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'lhc', '../graphics/buildings/lhc.jpg')
                if col == 'Q':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'red_square', '../graphics/buildings/parkk.jpg')
                if col == 'P':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'biotech', '../graphics/buildings/park.jpg')
                if col == 'L':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'lib', '../graphics/buildings/lib.jpg')
                if col == 'E':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'exhall', '../graphics/buildings/exhall.jpg')
                if col == 'I':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'shop', '../graphics/buildings/shop.jpg')
                if col == 'X':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'guesthouse', '../graphics/buildings/guesthouse.jpg')
                if col == 'D':
                    Road((x,y),[self.visible_sprites],False)
                    Dog((x,y),[self.player_sprites, self.visible_sprites], self.visible_sprites)
                if col == 'c':
                    Road((x,y),[self.visible_sprites],True)
                    Coin((x,y),[self.player_sprites, self.visible_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.player_sprites, self.visible_sprites], self.obstacle_sprites, self.visible_sprites, self.player_sprites, self.coins, self.level)
    
    def place_random_dogs(self):
        # possible dog positions
        dog_count=5
        vertical_road_positions =[]
        horizontal_road_positions =[]
        return

    def place_random_coins(self):
        return
    
    # def input(self):
    #     keys = pygame.key.get_pressed()

    #     # start game
    #     if keys[pygame.K_RSHIFT]:
    #         if self.playing==False:
    #             self.playing=True
    #             self.player.playing=True
    #     if keys[pygame.K_LSHIFT]:
    #         if self.player.pause==True:
    #             self.player.pause=False
    #             self.player.playing=True

    def display_text(self, text):
        text_surf = pygame.font.Font(UI_FONT,30).render(str((text)),False,'black')
        text_rect = text_surf.get_rect(center = (WIDTH/2,200))
        # pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20))
        self.display_surface.blit(text_surf,text_rect)
        # pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3)

    def run(self):
        # self.input()
        if self.playing==False:
            # start screen
            self.display_text(f'Welcome to Level:{self.level}')
            self.start_button.draw()

        elif self.player.completed:
            # print("show completed screen")
            self.display_text(f'Wohooo!! Mission Complete!!')
            self.next_level_button.draw()
            self.quit_button.draw()

        elif self.player.failed:
            #print("show failed screen")
            self.display_text(f'UhOhhhh!! Mission Failed!!')
            self.restart_button.draw()
            self.quit_button.draw()

        elif self.player.pause:
            # print("show pause screen")
            self.display_text(f'Game Paused')
            self.restart_button.draw()
            self.resume_button.draw()
            self.quit_button.draw()

        elif self.player.playing:
            # update and draw the game
            self.visible_sprites.custom_draw(self.player)
            self.player_sprites.custom_draw(self.player)
            self.visible_sprites.update()
            self.ui.display(self.player)

    
    def start_game(self):
        self.playing=True
        self.player.playing=True
    
    def restart_game(self):
        self.coins=STARTING_COINS
        self.level=1
        self.playing=False
        # sprite setup
        self.visible_sprites = YSortCameraGroup()
        self.player_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()
        self.place_random_dogs()
        self.place_random_coins()
        
    
    def quit_game(self):
        pygame.quit()
        sys.exit()
    
    def next_level_game(self):
        self.level+=1
        self.coins=self.player.coins
        self.playing=False
        # sprite setup
        self.visible_sprites = YSortCameraGroup()
        self.player_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()
        self.place_random_dogs()
        self.place_random_coins()
        return
    
    def resume_game(self):
        self.player.playing=True
        self.player.pause=False

        
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