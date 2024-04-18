import pygame, sys
from config.map import *
from src.helpers import *
from src.player import Player
from src.road import Road
from src.dog import Dog
from src.coin import Coin
from src.landmark import Landmark
from src.building import Building
from src.ui import UI
from src.button import Button
import sys
from src.debug import debug
from server.network import Network

class Game:
    def __init__(self):
          
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('IIT Delhi')
        self.clock = pygame.time.Clock()

        # get the display surface 
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.player_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()
        self.place_random_dogs()
        self.place_random_coins()

        # game status
        self.playing=False
        self.player_alive=False
        self.complete=False

        #button
        self.start_button = Button(WIDTH//2, 300, 200, 50, "Start", 'black', self.start_game)
        self.quit_button = Button(WIDTH//2, 400, 200, 50, "Quit", 'black', self.quit_game)

        #user interface
        self.timer=TOTAL_TIMER
        self.ui = UI()
        
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.playing==False:
                    self.start_button.handle_event(event)

                elif self.player.failed:
                    self.quit_button.handle_event(event)
            
            if self.timer>0:
                self.screen.fill('#9be650')
                if self.playing==False:
                    # start screen
                    self.display_text(f'Welcome to #GAME_NAME')
                    self.start_button.draw()

                elif self.player.failed:
                    #print("show failed screen")
                    self.display_text(f'UhOhhhh!! You Lost!!')
                    self.quit_button.draw()
                
                elif self.player.completed==True:
                    self.timer-=1
                    self.display_text(f'Amazing!! You completed before time!!!!')
                    self.ui.display_time(self.timer)

                elif self.playing:
                    # update and draw the game
                    self.timer-=1
                    self.visible_sprites.custom_draw(self.player)
                    self.player_sprites.custom_draw(self.player)
                    self.ui.display(self.player)
                    self.ui.display_time(self.timer)
                    self.visible_sprites.update()
            
            else:
                self.complete=True
                if self.player.failed==False:
                    self.player_alive=True
                    print("move to battle area")
                

            pygame.display.update()
            self.clock.tick(FPS)

            
    

    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col.isdigit():
                    Landmark((x,y),[self.visible_sprites,self.obstacle_sprites], HOSTELS[int(col)])
                if col == 'h':
                    Road((x,y),[self.visible_sprites],False)
                if col == 'v':
                    Road((x,y),[self.visible_sprites],True)
                if col[0] == 'G':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'hostel'+str(col[1:]), './assets/map_mode/hostel/hostell_192.jpg')
                if col == 'Y':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'yulu_stand', './assets/map_mode/buildings/yulu_64.jpg')
                if col == 't':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'tree', './assets/map_mode/tree/tree_50.jpg')
                if col == 'T':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'tennis', './assets/map_mode/grounds/tennis.jpg')
                if col == 'B':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'bank', './assets/map_mode/buildings/bank_128.jpg')
                if col == 'R':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'rajdhani', './assets/map_mode/buildings/rajdhani.jpg')
                if col == 'C':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'cycle_shop', './assets/map_mode/buildings/cycle.jpg')
                if col == 'S':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'sac', './assets/map_mode/buildings/sac.jpg')
                if col == 'H':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'hospital', './assets/map_mode/buildings/hospi.jpg')
                if col == 'F':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'football', './assets/map_mode/grounds/football.jpg')
                if col == 'Bb':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'basketball', './assets/map_mode/grounds/bb.jpg')
                if col == 'Rr':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'racing', './assets/map_mode/grounds/racing.jpg')
                if col == 'A':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'amul', './assets/map_mode/buildings/amul.jpg')
                if col == 'Cs':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'bharti', './assets/map_mode/buildings/bharti.jpg')
                if col == 'M':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'main_building', './assets/map_mode/buildings/main.jpg')
                if col == 'Lh':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'lhc', './assets/map_mode/buildings/lhc.jpg')
                if col == 'Q':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'red_square', './assets/map_mode/buildings/parkk.jpg')
                if col == 'P':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'biotech', './assets/map_mode/buildings/park.jpg')
                if col == 'L':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'lib', './assets/map_mode/buildings/lib.jpg')
                if col == 'E':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'exhall', './assets/map_mode/buildings/exhall.jpg')
                if col == 'I':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'shop', './assets/map_mode/buildings/shop.jpg')
                if col == 'X':
                    Building((x,y),[self.visible_sprites,self.obstacle_sprites], 'guesthouse', './assets/map_mode/buildings/guesthouse.jpg')
                if col == 'D':
                    Road((x,y),[self.visible_sprites],False)
                    Dog((x,y),[self.player_sprites, self.visible_sprites], self.visible_sprites)
                if col == 'c':
                    Road((x,y),[self.visible_sprites],True)
                    Coin((x,y),[self.player_sprites, self.visible_sprites])
                if col == 'p':
                    print(x,y)
                    self.player = Player((x,y),[self.player_sprites, self.visible_sprites], self.obstacle_sprites, self.visible_sprites, self.player_sprites)
    
    def place_random_dogs(self):
        # possible dog positions
        dog_count=5
        vertical_road_positions =[]
        horizontal_road_positions =[]
        return

    def place_random_coins(self):
        return


    def display_text(self, text):
        text_surf = pygame.font.Font(UI_FONT,30).render(str((text)),False,'black')
        text_rect = text_surf.get_rect(center = (WIDTH/2,200))
        # pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20))
        self.display_surface.blit(text_surf,text_rect)
        # pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3)

    
    def start_game(self):
        self.playing=True
        
    
    def quit_game(self):
        pygame.quit()
        sys.exit()

        
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
    
    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.rect.center)

        # flicker on dog hit
        if self.hurting:
            alpha = wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        # debug(player.rect.centerx+self.offset.x)
        debug(self.offset)
        for sprite in self.sprites():
            if sprite.name!='landmark':
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)
            else:
                offset_pos = sprite.rect.topleft - self.offset
                sprite.rectt = sprite.text_surface.get_rect(topleft = offset_pos)
                pygame.draw.rect(self.display_surface,UI_BG_COLOR,sprite.rectt)
                self.display_surface.blit(sprite.text_surface,sprite.rectt)
                pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,sprite.rectt,1)

if __name__ == '__main__':
    game = Game()
    game.run()	