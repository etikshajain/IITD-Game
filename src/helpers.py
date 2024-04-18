import pygame
from os import walk
from math import sin

def wave_value():
    value = sin(pygame.time.get_ticks())
    if(value>=0):
        return 255
    return 0