import pygame, sys
from pygame import mixer
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
from config.main import *
from config.fighter import MIN_SCORE,MAX_SCORE,MIN_SWORD_DAMAGE,MAX_SWORD_DAMAGE

class Game:
    def __init__(self):
          
        # general setup
        pygame.init()
        mixer.init()
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
                    self.display_text(f'Welcome to #GAME_NAME',200)
                    self.start_button.draw()

                elif self.player.failed:
                    print("show failed screen")
                    # self.display_text(f'UhOhhhh!! You Lost!!',200)
                    self.quit_button.draw()
                
                elif self.player.completed==True:
                    return self.player.score

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
                    return self.player.score
                

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


    def display_text(self, text, ycoord):
        text_surf = pygame.font.Font(UI_FONT,30).render(str((text)),False,'black')
        text_rect = text_surf.get_rect(center = (WIDTH/2,ycoord))
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
    score = game.run()
    n = Network()
    fighter_1 = n.getPlayer() # connect via socket
    fighter_1.sword_power = MIN_SWORD_DAMAGE + ((score-MIN_SCORE)*(MAX_SWORD_DAMAGE-MIN_SWORD_DAMAGE)/(MAX_SCORE-MIN_SCORE))
    while True:
        fighter_2 = n.send(fighter_1)
        if fighter_2 is not None:
            break
        else:
            game.display_text(f'Amazing!! You completed before time!!',200)
            game.display_text(f'but your partner is slow :)',300)
            game.display_text(f'waiting for him/her to finish the round 1',400)
            pygame.display.update()
            game.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Brawl mode")
    clock = pygame.time.Clock()

    #define game variables
    intro_count = INTRO_CNT
    last_count_update = pygame.time.get_ticks()
    round_over = False

    pygame.mixer.music.load(VSMODE_BACKGROUND_AUDIO)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0, 5000)
    sword_attack = pygame.mixer.Sound(SWORD_ATTACK_AUDIO)
    sword_attack.set_volume(0.8)
    sword_clash = pygame.mixer.Sound(SWORD_CLASH_AUDIO)
    sword_clash.set_volume(0.8)

    bg_image = pygame.image.load(VSMODE_BACKGROUND).convert_alpha()
    count_font = pygame.font.Font(COUNTDOWN_FONT, 80)

    #function for drawing text
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    #function for drawing background
    def draw_bg():
        scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaled_bg, (0, 0))

    #function for drawing fighter health bars
    def draw_health_bar(health, x, y):
        ratio = health / 100
        pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
        pygame.draw.rect(screen, RED, (x, y, 400, 30))
        pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

    def load_images(sprite_sheet, animation_steps):
    #extract images from spritesheet
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * 128, y * 128, 128, 128)
                temp_img_list.append(pygame.transform.scale(temp_img, (128 * CHARACTER_SCALE,128 * CHARACTER_SCALE)))
            animation_list.append(temp_img_list)
        return animation_list

    #load spritesheets
    samura1_sheet = pygame.image.load(SAMURAI1_SHEET).convert_alpha()
    samura2_sheet = pygame.image.load(SAMURAI2_SHEET).convert_alpha()

    run = True
    if fighter_1.pid == 1:
        p1_animation_list = load_images(samura1_sheet,SAMURAI1_ANIMATION_LIST)
        p2_animation_list = load_images(samura2_sheet,SAMURAI2_ANIMATION_LIST)
    else:
        p1_animation_list = load_images(samura2_sheet,SAMURAI2_ANIMATION_LIST)
        p2_animation_list = load_images(samura1_sheet,SAMURAI1_ANIMATION_LIST)

    while run:
        clock.tick(FPS)
        draw_bg()
        fighter_2 = n.send(fighter_1) # send data to server
    
        #check for blocked_attack
        if fighter_2 is not None:
            if fighter_1.attack_blocked == True or fighter_2.attack_blocked == True:
                sword_clash.play()
                fighter_1.attack_blocked = False
                fighter_2.attack_blocked = False

        #show health stats
        if fighter_1.pid == 1:
            draw_health_bar(fighter_1.health, HEALTH_BAR_X_OFFSET, HEALTH_BAR_Y_OFFSET)
            draw_health_bar(fighter_2.health, SCREEN_WIDTH - 404 - HEALTH_BAR_X_OFFSET, HEALTH_BAR_Y_OFFSET)
        else:
            draw_health_bar(fighter_1.health, SCREEN_WIDTH - 404 - HEALTH_BAR_X_OFFSET, HEALTH_BAR_Y_OFFSET)
            draw_health_bar(fighter_2.health, HEALTH_BAR_X_OFFSET, HEALTH_BAR_Y_OFFSET)

        #update countdown
        if intro_count <= 0 and (not round_over): #move player
            fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
        elif intro_count > 0:
            #display count timer
            draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
            #update count timer
            if (pygame.time.get_ticks() - last_count_update) >= 1000:
                intro_count -= 1
                last_count_update = pygame.time.get_ticks()
    
        if fighter_2.hit == True and fighter_1.attacked_opo == True:
            # print(fighter_1.pid, "hit completed")
            fighter_1.attacked_opo = False
            sword_attack.play()

        if fighter_2.attacked_opo and fighter_1.hit == False:
            # print(fighter_1.pid, "hit ack")
            sword_attack.play()
            fighter_1.hit = True
            fighter_1.health -= fighter_2.sword_power
    
        #update fighters
        fighter_1.update()
        fighter_2.update()

        #draw fighters
        fighter_1.draw(screen,p1_animation_list[fighter_1.action][fighter_1.frame_index])
        fighter_2.draw(screen,p2_animation_list[fighter_2.action][fighter_2.frame_index])

        # see if the round is over or not
        if (not round_over):
            if (not fighter_1.alive) or (not fighter_2.alive) :
                round_over = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    #exit pygame
    pygame.quit()