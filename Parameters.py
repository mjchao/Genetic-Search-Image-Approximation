'''
Created on Sep 12, 2015

@author: mjchao
'''
import pygame
from Utils import convertToPixelArray

#list of global parameter constants
IMG_WIDTH = 32
IMG_HEIGHT = 32

P = 100
N = 100
K = 50
T = 500
E = 25000
IMG = pygame.image.load( "mona_lisa.bmp" )
IMG_PIXEL_ARRAY = convertToPixelArray( IMG )