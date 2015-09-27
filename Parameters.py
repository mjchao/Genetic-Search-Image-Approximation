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
<<<<<<< HEAD
IMG = pygame.image.load( "haystack.png" )
OUTPUT_DIR = "haystack"
IMG_WIDTH = 128
IMG_HEIGHT = 128
#-------------------------#

IMG_PIXEL_ARRAY = convertToPixelArray( IMG )
IMG_PIXEL_ARRAY_NORM = norm( IMG_PIXEL_ARRAY )
