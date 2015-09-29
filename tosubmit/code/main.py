import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode( (100, 100) )

coordinates = [ (0,0) , (100,0) , (100,100) ]
surface = pygame.Surface( (100,100) , flags = pygame.SRCALPHA )
#surface.set_alpha( 255 )
pygame.draw.polygon( surface , (255,0,0,255) , coordinates )
pygame.draw.polygon( surface , (0,0,255,150) , coordinates )
screen.blit( surface , (0,0) )

state = 0
while state == 0:
    pygame.display.update()
        
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            state = 1
            break