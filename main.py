import pygame
from pygame import mixer
from server.network import Network
from config.main import *
from config.fighter import SWORD_DAMAGE

mixer.init()
pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

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
n = Network()
fighter_1 = n.getPlayer() # connect via socket
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

  #show health stats
  if fighter_1.pid == 1:
    draw_health_bar(fighter_1.health, HEALTH_BAR_X_OFFSET, HEALTH_BAR_Y_OFFSET)
    if fighter_2 is not None:
      draw_health_bar(fighter_2.health, SCREEN_WIDTH - 404 - HEALTH_BAR_X_OFFSET, HEALTH_BAR_Y_OFFSET)
  else:
    draw_health_bar(fighter_1.health, SCREEN_WIDTH - 404 - HEALTH_BAR_X_OFFSET, HEALTH_BAR_Y_OFFSET)
    if fighter_2 is not None:
      draw_health_bar(fighter_2.health, HEALTH_BAR_X_OFFSET, HEALTH_BAR_Y_OFFSET)

  #update countdown
  if fighter_2 is not None:
    if intro_count <= 0 and (not round_over): #move player
      fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
    elif intro_count > 0:
      #display count timer
      draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
      #update count timer
      if (pygame.time.get_ticks() - last_count_update) >= 1000:
        intro_count -= 1
        last_count_update = pygame.time.get_ticks()
  
  if fighter_2 is not None: # update health status
    if fighter_2.hit == True and fighter_1.attacked_opo == True:
      # print(fighter_1.pid, "hit completed")
      fighter_1.attacked_opo = False
      sword_attack.play()

    if fighter_2.attacked_opo and fighter_1.hit == False:
      # print(fighter_1.pid, "hit ack")
      sword_attack.play()
      fighter_1.hit = True
      fighter_1.health -= SWORD_DAMAGE
  
  #update fighters
  fighter_1.update()
  if fighter_2 is not None:
    fighter_2.update()

  #draw fighters
  fighter_1.draw(screen,p1_animation_list[fighter_1.action][fighter_1.frame_index])
  if fighter_2 is not None:
    fighter_2.draw(screen,p2_animation_list[fighter_2.action][fighter_2.frame_index])

  # see if the round is over or not
  if fighter_2 is not None and (not round_over):
    if (not fighter_1.alive) or (not fighter_2.alive) :
      round_over = True

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

#exit pygame
pygame.quit()