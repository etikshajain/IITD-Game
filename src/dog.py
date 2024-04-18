import pygame 
from config.map import *

class Dog(pygame.sprite.Sprite):
    def __init__(self,pos,groups, visible_sprites):
        super().__init__(groups)
        self.name = 'dog'
        self.image = pygame.image.load('./assets/map_mode/dog/dogo.jpg').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.visible_sprites = visible_sprites

        # cooldowns
        self.hit = False
        self.hit_cooldown = 200
        self.hit_time = None

        #movement 
        self.direction = pygame.math.Vector2()
        self.direction.x=1

        # stats
        self.speed = DOG_SPEED
    
    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.hit:
            if current_time-self.hit_time >= self.hit_cooldown:
                self.hit = False

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        if self.hit:
            return
        self.rect.x += self.direction.x * self.speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed
        self.collision('vertical')

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.visible_sprites:
                if sprite.rect.colliderect(self.rect) and sprite.name!='dog' and sprite.name!='player' and sprite.name !='road' and self.hit==False:
                    self.hit=True
                    self.hit_time=pygame.time.get_ticks()
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left
                        self.direction.x=-1
                    elif self.direction.x < 0: # moving left
                        self.rect.left = sprite.rect.right
                        self.direction.x=1

        if direction == 'vertical':
            for sprite in self.visible_sprites:
                if sprite.rect.colliderect(self.rect) and sprite.name!='dog' and sprite.name!='player' and sprite.name !='road' and self.hit==False:
                    self.hit=True
                    self.hit_time=pygame.time.get_ticks()
                    if self.direction.y > 0: # moving down
                        self.direction.y=-1
                        self.rect.bottom = sprite.rect.top
                    elif self.direction.y < 0: # moving up
                        self.direction.y=1
                        self.rect.top = sprite.rect.bottom

    def update(self):
        self.cooldowns()
        self.move()
	