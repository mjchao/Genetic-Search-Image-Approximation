'''
Created on Sep 12, 2015

@author: mjchao
'''
import pygame
from Utils import convertToPixelArray, norm

#list of global parameter constants


P = 100
N = 1
K = 1
T = 500000
E = 500000

#---Change when image changes---#
IMG = pygame.image.load( "darwin.jpg" )
OUTPUT_DIR = "darwin"
IMG_WIDTH = 256
IMG_HEIGHT = 256
#-------------------------#

IMG_PIXEL_ARRAY = convertToPixelArray( IMG )
IMG_PIXEL_ARRAY_NORM = norm( IMG_PIXEL_ARRAY )
