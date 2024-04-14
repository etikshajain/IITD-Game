import pygame 
from settings import *
from helpers import import_folder, wave_value

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups, obstacle_sprites, visible_sprites):
        super().__init__(groups)
        self.name = 'player'
        self.image = pygame.image.load('../graphics/player/player_40.jpg').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        #TODO: coin collision
        #TODO: dog collision

        # graphics setup
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        #movement 
        self.direction = pygame.math.Vector2()
        self.yulu = False
        self.grass=False
        self.hurting = False # due to dog hit
        self.dog_attack_cooldown = 4000
        self.dog_attack_time = None

        # stats
        self.stats = {'energy':100, 'coins':0, 'level':1, 'timer':1, 'speed':5, 'yulu_speed':8, 'grass_speed':2}
        self.energy = 80
        self.coins = self.stats['coins']
        self.level = self.stats['level']
        self.timer = self.stats['timer']
        self.speed = self.stats['speed']
        self.yulu_speed = self.stats['yulu_speed']
        self.grass_speed = self.stats['grass_speed']

        self.obstacle_sprites = obstacle_sprites
        self.visible_sprites = visible_sprites
    
    def import_player_assets(self):
        character_path = '../graphics/player/'
        self.animations = {'up': [],'down': [],'left': [],'right': [],
			'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
			'right_yulu':[],'left_yulu':[],'up_yulu':[],'down_yulu':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
    
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
        
        # yulu input
        if keys[pygame.K_y]:
            #check if you're at yulu stand
            for sprite in self.obstacle_sprites:
                if sprite.name=='yulu_stand':
                    if abs(self.rect.centerx-sprite.rect.centerx)<=100 and abs(self.rect.centery-sprite.rect.centery)<=100:
                        if(self.yulu==False):
                            self.yulu=True
                        return
                    
        if keys[pygame.K_t]:
            #check if you're at yulu stand
            for sprite in self.obstacle_sprites:
                if sprite.name=='yulu_stand':
                    if abs(self.rect.centerx-sprite.rect.centerx)<=100 and abs(self.rect.centery-sprite.rect.centery)<=100:
                        if(self.yulu==True):
                            self.yulu=False
                        return
    
    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.hurting:
            if current_time-self.dog_attack_time >= self.dog_attack_cooldown:
                self.hurting = False

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        if self.yulu:
            self.rect.x += self.direction.x * self.yulu_speed
            self.collision('horizontal')
            self.rect.y += self.direction.y * self.yulu_speed
            self.collision('vertical')
            self.energy -= ((1/self.yulu_speed)/10)
        elif self.grass:
            self.rect.x += self.direction.x * self.grass_speed
            self.collision('horizontal')
            self.rect.y += self.direction.y * self.grass_speed
            self.collision('vertical')
            self.energy -= ((1/self.grass_speed)/10)
        else:
            self.rect.x += self.direction.x * self.speed
            self.collision('horizontal')
            self.rect.y += self.direction.y * self.speed
            self.collision('vertical')
            self.energy -= ((1/self.speed)/10)

    def collision(self,direction):
        # check for dog and grass collision
        c=0
        for sprite in self.visible_sprites:
            if sprite.name=='road':
                if sprite.rect.colliderect(self.rect):
                    c+=1
            if sprite.name=='dog' and sprite.rect.colliderect(self.rect) and self.hurting==False and self.yulu==False:
                self.energy -= 5
                self.dog_attack_time = pygame.time.get_ticks()
                self.hurting=True

        if c==0:
            self.grass=True
        else:
            self.grass=False

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
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move()
	