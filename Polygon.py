'''
Created on Sep 12, 2015

@author: mjchao
'''

import pygame
from pygame.locals import *
from random import randint , uniform
from base64 import test1

'''
Represents a polygon with some vertices and filled with a given color.
Vertices are specified as ordered pairs of floats. The color is
specified as a tuple with four integers: (r, g, b, a).

'''
class Polygon:
    
    
    @staticmethod
    def rand_triangle( maxX , maxY ):
        x1 = randint( 0 , maxX )
        y1 = randint( 0 , maxY )
        x2 = randint( 0 , maxX )
        y2 = randint( 0 , maxY )
        x3 = randint( 0 , maxX )
        y3 = randint( 0 , maxY )
        r = randint( 0 , 255 )
        g = randint( 0 , 255 )
        b = randint( 0 , 255 )
        a = uniform( 0 , 1 )
        return Polygon( [ (x1 , y1) , (x2 , y2) , (x3 , y3) ] , (r, g, b, a) )
    
    '''
    Creates a polygon.
    '''
    def __init__( self , vertices = [ (0,0) , (0,0) , (0,0) ] , color = (0 , 0 , 0 , 0) ):
        self._vertices = vertices
        self._color = color
        
    '''
    Draws this polygon onto the screen.
    '''
    def draw( self , display ):
        surface = pygame.surface.Surface( (500, 500) , flags = pygame.SRCALPHA )
        surface.set_alpha( self._color[ 3 ] )
        pygame.draw.polygon( surface , self._color[0:3] , self._vertices )
        display.blit( surface , (0, 0) )
        
    def __str__( self ):
        return "Polygon { Vertices = " + str( self._vertices ) + ", Color = " + str( self._color ) + "}"

'''
Unit testing
'''
def main():
    test1 = Polygon.rand_triangle( 100 , 100 )
    test2 = Polygon( [ (0, 0) , (0 , 10) , (10, 10) ] , (0 , 0 , 0 , 1 ) )
    pygame.init()
    screen = pygame.display.set_mode( (100, 100) )
    screen.fill( (255, 255, 255) )
    test1.draw( screen )
    test2.draw( screen )
    pygame.display.update()
    
    print test1
    print test2
    state = 0
    while state == 0:
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 1
                break
    
    
if __name__ == "__main__" : main()