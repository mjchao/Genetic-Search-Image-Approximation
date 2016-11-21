'''
Created on Sep 19, 2015

@author: mjchao
'''
import numpy
from PIL import Image, ImageDraw

## Converts an image surface to a pixel array
def convertToPixelArray(image_surface):
    rtn = []
    for data in image_surface.getdata():
        rtn.append(data[0])
        rtn.append(data[1])
        rtn.append(data[2])
    return numpy.array(rtn) / 255.0

## Returns Euclidean distance between two pixel arrays
def euclideanDistance(PixelArray1, PixelArray2):
    return numpy.linalg.norm(PixelArray1 - PixelArray2)

#Returns the norm |s| of a pixel array s
def norm( pixelArray ):
    return numpy.linalg.norm( pixelArray )


## Returns an image surface read from a file
def loadImage(filename):
    return Image.open(filename)

'''
Saves a surface  
'''
def save_surface( image , filename ):
    image.save(filename)

