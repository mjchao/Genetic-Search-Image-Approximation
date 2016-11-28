'''
Created on Sep 12, 2015

@author: mjchao
'''
from PIL import Image
from Utils import convertToPixelArray, norm

#list of global parameter constants


P = 200
N = 1
K = 1
T = 100000000
E = 25000

#---Change when image changes---#
IMG = Image.open( "mjchao.jpg" ).convert("RGBA")
OUTPUT_DIR = "tmp2"
IMG_WIDTH = 96
IMG_HEIGHT = 128
#--------------------------#

IMG_PIXEL_ARRAY = convertToPixelArray( IMG )
IMG_PIXEL_ARRAY_NORM = norm( IMG_PIXEL_ARRAY )
