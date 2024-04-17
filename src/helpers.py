import pygame
from os import walk
from math import sin

def import_folder(path):
    surface_list = []
    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            if full_path.split('.')[-1]!='jpg':
                continue
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list

def wave_value():
    value = sin(pygame.time.get_ticks())
    if(value>=0):
        return 255
    return 0