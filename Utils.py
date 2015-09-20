'''
Created on Sep 19, 2015

@author: mjchao
'''
import pygame
import numpy

## Renders a polygon object (list of points and an RGBA tuple) on an image buffer (surface)
def renderPolygon(image_buffer, polygon):
    pygame.draw.polygon(image_buffer, polygon.color, polygon.listOfPoints, 0)


## Converts an image surface to a pixel array
def convertToPixelArray(image_surface):
    return pygame.surfarray.pixels3d(image_surface).reshape(image_surface.get_width() * image_surface.get_height() * 3)/255.0


## Returns Euclidean distance between two pixel arrays
def euclideanDistance(PixelArray1, PixelArray2):
    return numpy.linalg.norm(PixelArray1 - PixelArray2)


## Returns an image surface read from a file
def loadImage(filename):
    return pygame.image.load(filename)

'''
Saves a surface  
'''
def save_surface( image , filename ):
    pygame.image.save( image , filename )

def display():
    pass
