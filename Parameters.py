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
N = 10
K = 100
T = 250
E = 25000
IMG = pygame.image.load( "mona_lisa.bmp" )
IMG_PIXEL_ARRAY = convertToPixelArray( IMG )

OUTPUT_DIR = "mona_lisa"
