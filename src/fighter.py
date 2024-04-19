import pygame
from config.fighter import *

class Fighter():
  def __init__(self, pid, x, y, flip, data, animation_list):
    self.pid = pid # player id
    self.player_alias = "None"
    self.size = data[0]
    self.image_scale = data[1]
    self.offset = data[2]
    self.flip = flip
    self.animation_list = animation_list
    self.action = 0 #0:idle #1:walk #2:run #3:attack1 #4: attack2 #5: attack3 #6:defense #7:jump #8:hit #9:death
    self.frame_index = 0
    self.update_time = pygame.time.get_ticks()
    self.rect = pygame.Rect((x, y, 80, 240))
    self.vel_y = 0
    self.running = False
    self.jump = False
    self.sword_power = 0
    self.attacking = False
    self.attacked_opo = False
    self.attack_type = 0
    self.attack_cooldown = 0
    self.blocking= False
    self.block_cooldown = 0
    self.attack_blocked = False
    self.hit = False
    self.health = 100.0
    self.alive = True

  def move(self, screen_width, screen_height, surface, target, round_over):
    dx = 0
    dy = 0
    self.running = False
    self.attack_type = 0
    
    key = pygame.key.get_pressed()

    #can only perform other actions if not currently attacking
    if self.attacking == False and self.alive == True and round_over == False:
      if key[pygame.K_LEFT]:
        dx = -SPEED
        self.running = True
      if key[pygame.K_RIGHT]:
        dx = SPEED
        self.running = True
      #jump
      if key[pygame.K_UP] and self.jump == False:
        self.vel_y = -JUMP_Y
        self.jump = True
      #attack
      if key[pygame.K_z] or key[pygame.K_c]:
        self.attack(target)
        #determine attack type
        if key[pygame.K_c]:
          self.attack_type = 1
        if key[pygame.K_z]:
          self.attack_type = 2
      #block
      if key[pygame.K_x]: 
        self.block(target)
    
    #apply gravity
    self.vel_y += GRAVITY
    dy += self.vel_y

    #ensure player stays on screen
    if self.rect.left + dx < 0:
      dx = -self.rect.left
    if self.rect.right + dx > screen_width:
      dx = screen_width - self.rect.right
    if self.rect.bottom + dy > screen_height - 50:
      self.vel_y = 0
      self.jump = False
      dy = screen_height - 50 - self.rect.bottom

    #ensure players face each other
    if target is not None:
      if target.rect.centerx > self.rect.centerx:
        self.flip = False
      else:
        self.flip = True

    #attack cooldown
    if self.attack_cooldown > 0:
      self.attack_cooldown -= 1
    #block cooldown
    if self.block_cooldown >0:
      self.block_cooldown-=1

    #update player position
    self.rect.x += dx
    self.rect.y += dy


  def update(self):
    #determine action the player is performing
    if self.health <= 0:
      self.health = 0
      self.alive = False
      self.update_action(9) #death
    elif self.hit == True:
      self.update_action(8) #hit
    elif self.attacking == True:
      if self.attack_type == 1:
        self.update_action(3) #attack1
      elif self.attack_type == 2:
        self.update_action(4) #attack2
    elif self.blocking == True: #block
      self.update_action(6)
    elif self.jump == True:
      self.update_action(7) #jump
    elif self.running == True:
      self.update_action(2) #run
    else:
      self.update_action(0) #idle

    animation_cooldown = ANIMATION_COOLDOWN
    #check if enough time has passed since the last update
    if pygame.time.get_ticks() - self.update_time > animation_cooldown:
      self.frame_index += 1
      self.update_time = pygame.time.get_ticks()
    #check if the animation has finished
    if self.frame_index >= self.animation_list[self.action]:
      #if the player is dead then end the animation
      if self.alive == False:
        self.frame_index = self.animation_list[self.action] - 1
      else:
        self.frame_index = 0
        #check if an attack was executed
        if self.action == 3 or self.action == 4:
          self.attacking = False
          self.attack_cooldown = ATTACK_COOLDOWN
        #check if the player blocked the move
        if self.action == 6:
          self.blocking= False
          self.block_cooldown= BLOCK_COOLDOWN
        #check if damage was taken
        if self.action == 8:
          self.hit = False
          #if the player was in the middle of an attack, then the attack is stopped
          self.attacking = False
          self.attack_cooldown = ATTACK_COOLDOWN

  def attack(self, target):
    if self.attack_cooldown == 0:
      #execute attack
      self.attacking = True
      attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect):
        # print(self.pid, "hit sent")
        # pygame.draw.rect(surface,(0,255,0),attacking_rect)
        if target.blocking == True:
          self.attack_blocked = True
        else:
          self.attacked_opo = True

  def block(self,target):
      if self.block_cooldown == 0:
        self.blocking= True
  
  def update_action(self, new_action):
    if new_action != self.action:
      self.action = new_action
      self.frame_index = 0
      self.update_time = pygame.time.get_ticks()

  def draw(self, surface, image):
    if image is None :
      return
    img = pygame.transform.flip(image, self.flip, False)
    surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))
    # pygame.draw.rect(surface,(255,0,0),self.rect)