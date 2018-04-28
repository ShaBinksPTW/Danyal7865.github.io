import pygame
from pygame.locals import *


pygame.init()

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
robloxnoob = pygame.image.load('robloxnoob.png')
tide_pod = pygame.image.load('tidepod.jpg')
pygame.display.update()
crashed = False
x =  (0)
y =  (0)
x2 = (400)
y2 = (300)
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    game_display.fill((255,255,255))
    game_display.blit(tide_pod, (x,y))
    game_display.blit(robloxnoob, (x2,y2))
    pygame.display.update()         
    x = x + 1
    y = y + 1 
    x2 = x2 - 1
    y2 = y2 - 1
                                        