'''
Created on Sep 12, 2015

@author: mjchao
'''
import pygame
from Utils import convertToPixelArray, norm

#list of global parameter constants
IMG_WIDTH = 32
IMG_HEIGHT = 32

P = 100
N = 1
K = 2
T = 10000
E = 25000
IMG = pygame.image.load( "mona_lisa.bmp" )
IMG_PIXEL_ARRAY = convertToPixelArray( IMG )
IMG_PIXEL_ARRAY_NORM = norm( IMG_PIXEL_ARRAY )

OUTPUT_DIR = "mona_lisa"
