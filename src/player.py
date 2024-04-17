import pygame 
from config.map import *
from src.helpers import import_folder, wave_value

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups, obstacle_sprites, visible_sprites, player_sprites):
        super().__init__(groups)
        self.name = 'player'
        self.image = pygame.image.load('./assets/map_mode/player/player_40.jpg').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

        # closest obstacle sprite
        self.closest_sprite = None

        # assets setup
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        #movement 
        self.direction = pygame.math.Vector2()
        self.yulu = False
        self.grass=False

        # dog cooldowns
        self.hurting = False # due to dog hit
        self.dog_attack_cooldown = 4000
        self.dog_attack_time = None

        #eating cooldown
        self.eating=False
        self.eating_cooldown=4000
        self.last_eating_time=None

        # stats
        self.stats = {'energy':100, 'yulu_bill':0}
        self.coins=STARTING_COINS
        self.energy = 100
        self.speed = SPEED
        self.yulu_speed = YULU_SPEED
        self.grass_speed = GRASS_SPEED

        # level stats
        self.level = 1
        self.next_checkpoint = CHECKPOINTS[self.level-1]
        self.ending_point = ENDING_POINT

        self.obstacle_sprites = obstacle_sprites
        self.visible_sprites = visible_sprites
        self.player_sprites = player_sprites

        # game status - failed, completed
        self.failed=False
        self.completed=False
    
    def import_player_assets(self):
        character_path = './assets/map_mode/player/'
        self.animations = {'up': [],'down': [],'left': [],'right': [],
			'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
			'right_yulu':[],'left_yulu':[],'up_yulu':[],'down_yulu':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
    
    def check_game_status(self):
        if self.energy==0 or self.coins<0 or self.stats['yulu_bill']>self.coins:
            self.failed=True
            return
        
    
    def get_status(self):
        # idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'yulu' in self.status:
                self.status = self.status + '_idle'

        if self.yulu:
            if not 'yulu' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_yulu')
                else:
                    self.status = self.status + '_yulu'
        else:
            if 'yulu' in self.status:
                self.status = self.status.replace('_yulu','')
    
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

    def input(self):
        keys = pygame.key.get_pressed()

        # movement input
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status='up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status='down'
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status='right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status='left'
        else:
            self.direction.x = 0
        
        # get pn yulu
        if keys[pygame.K_y]:
            #check if you're at yulu stand
            if self.closest_sprite is not None and self.closest_sprite.name=='yulu_stand':
                if self.yulu==False:
                    self.yulu=True
                    return

        # get off yulu        
        if keys[pygame.K_t]:
            #check if you're at yulu stand
            if self.closest_sprite is not None and self.closest_sprite.name=='yulu_stand':
                if self.yulu==True:
                    self.yulu=False
                    self.coins-=self.stats['yulu_bill']
                    self.stats['yulu_bill']=0
                    return
        
        # recharge energy from hospital
        if keys[pygame.K_h] and self.eating==False:
            #check if you're at yulu stand
            if self.closest_sprite is not None and self.closest_sprite.name=='hospital':
                self.last_eating_time = pygame.time.get_ticks()
                self.eating=True
                self.coins = max(0,self.coins-int(HOSPITAL_FEES))
                self.energy=100
        
        # recharge energy from rajdhani/amul/shop
        if keys[pygame.K_f] and self.eating==False:
            #check if you're at food stall
            if self.closest_sprite is not None:
                if self.closest_sprite.name=='rajdhani' or self.closest_sprite.name=='amul' or self.closest_sprite.name=='shop':
                    self.last_eating_time = pygame.time.get_ticks()
                    self.eating=True
                    self.coins = max(0,self.coins-int(FOOD_FEES))
                    self.energy=min(100,self.energy+FOOD_ENERGY)

        # reach next checkpoint
        if keys[pygame.K_SPACE]:
            #check if you're at cp
            if self.closest_sprite is not None:
                if self.closest_sprite.name==self.next_checkpoint:
                    self.coins+=POINTS[self.level-1]
                    self.level+=1
                    if self.level==len(CHECKPOINTS)+1:
                        self.completed=True
                    else:
                        self.next_checkpoint=CHECKPOINTS[self.level-1]
    
    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.hurting:
            if current_time-self.dog_attack_time >= self.dog_attack_cooldown:
                self.hurting = False
        
        if self.eating:
            if current_time-self.last_eating_time >= self.eating_cooldown:
                self.eating = False

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        if self.yulu:
            speed = self.yulu_speed
            self.energy = max(0,self.energy-YULU_ENERGY_RATE)
            self.stats['yulu_bill']+=YULU_BILL
            
        elif self.grass:
            speed = self.grass_speed
            self.energy = max(0,self.energy-GRASS_ENERGY_RATE)
        else:
            speed = self.speed
            self.energy = max(0,self.energy-ENERGY_RATE)
        
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')

    def check_proximity(self):
        # check for dog and grass collision(visible sprite collisions)
        c=0
        for sprite in self.visible_sprites:
            if sprite.name=='road':
                if sprite.rect.colliderect(self.rect):
                    c+=1
            # check dog hit
            if sprite.name=='dog' and sprite.rect.colliderect(self.rect) and self.hurting==False and self.yulu==False:
                self.energy = max(0,self.energy-DOG_BITE_ENERGY)
                self.dog_attack_time = pygame.time.get_ticks()
                self.hurting=True
            
            # check coin hit
            if sprite.name=='coin' and sprite.rect.colliderect(self.rect) and self.hurting==False:
                self.coins+=COIN_VALUE
                self.visible_sprites.remove(sprite)
                self.player_sprites.remove(sprite)


        if c==0:
            self.grass=True
        else:
            self.grass=False

        # offset
        offset=pygame.math.Vector2()
        offset.x = self.rect.centerx - self.half_width
        offset.y = self.rect.centery - self.half_height

        sprite_ = None
        for sprite in self.obstacle_sprites:
            # highlight starting and end points of current level
            if sprite.name == self.next_checkpoint:
                rect_highligh = pygame.Rect(sprite.rect.x-offset.x,sprite.rect.y-offset.y,sprite.rect.width,sprite.rect.height)
                pygame.draw.rect(self.display_surface,CHECKPOINT_COLOR,rect_highligh,5)

            # check if the sprite is near the player
            if self.grass==False and sprite.name != "tree":
                # check if the distance is <= 50px
                x1,y1 = self.rect.center
                d1 = max(self.rect.width,self.rect.height)
                x2,y2 = sprite.rect.center
                d2 = max(sprite.rect.width,sprite.rect.height)
                d3 = (((x1-x2)**2)+((y1-y2)**2))**0.5
                if d3<=(d1+d2)//2 + 20:
                    if self.yulu==False:
                        sprite_ = sprite
                    else:
                        if sprite.name=='yulu_stand':
                            sprite_=sprite
        
        self.closest_sprite = sprite_
        
        # highlight the closest sprite
        if sprite_ is not None:
            self.closest_sprite = sprite_
            rect_highligh = pygame.Rect(sprite_.rect.x-offset.x,sprite_.rect.y-offset.y,sprite_.rect.width,sprite_.rect.height)
            pygame.draw.rect(self.display_surface,HIGHLIGHT_COLOR,rect_highligh,5)

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: # moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: # moving up
                        self.rect.top = sprite.rect.bottom

    def update(self):
        self.check_game_status()
        if self.failed==False and self.completed==False:
            self.check_proximity()
            self.input()
            self.cooldowns()
            self.get_status()
            self.animate()
            self.move()
	