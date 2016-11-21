'''
Created on Sep 12, 2015

@author: mjchao
'''
from PIL import Image
from Utils import convertToPixelArray, norm

#list of global parameter constants


P = 100
N = 1
K = 1
T = 500000
E = 25000

#---Change when image changes---#
IMG = Image.open( "mona_lisa.bmp" ).convert("RGBA")
OUTPUT_DIR = "tmp"
IMG_WIDTH = 32
IMG_HEIGHT = 32
#--------------------------#

IMG_PIXEL_ARRAY = convertToPixelArray( IMG )
IMG_PIXEL_ARRAY_NORM = norm( IMG_PIXEL_ARRAY )
