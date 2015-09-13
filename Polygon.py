'''
Created on Sep 12, 2015

@author: mjchao
'''

import pygame
from Parameters import IMG_WIDTH , IMG_HEIGHT
from pygame.locals import QUIT , KEYDOWN , K_ESCAPE
from random import randint , uniform

'''
Represents a polygon with some vertices and filled with a given color.
Vertices are specified as ordered pairs of floats. The color is
specified as a tuple with four integers: (r, g, b, a).

'''
class Polygon( object ):
    
    '''
    Returns a random coordinate (x, y) with x value in range
    [0 , maxX) , [0 , maxY)
    '''
    @staticmethod
    def rand_xy( maxX , maxY ):
        return ( randint( 0 , maxX ) , randint( 0 , maxY ) )
    
    '''
    Returns a random (r, g, b, a) value
    '''
    @staticmethod
    def rand_rgba():
        return ( randint( 0 , 256 ) , randint( 0 , 256 ) , randint( 0 , 256 ) , uniform( 0 , 1 ) )
    
    '''
    Returns a random triangle
    '''
    @staticmethod
    def rand_triangle( maxX , maxY ):
        return Polygon.rand_n_gon( 3 , maxX , maxY )
    
    '''
    Returns a random n-gon with n vertices. The vertices may not be in the
    correct order, though.
    '''
    @staticmethod
    def rand_n_gon( n , maxX , maxY ):
        vertices = []
        for i in range( 0 , n ):
            vertices.append( Polygon.rand_xy( maxX , maxY ) )
        return Polygon( vertices  , Polygon.rand_rgba() )
        
    
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
        surface = pygame.surface.Surface( (IMG_WIDTH, IMG_HEIGHT) , flags = pygame.SRCALPHA )
        surface.set_alpha( self._color[ 3 ] )
        pygame.draw.polygon( surface , self._color[0:3] , self._vertices )
        display.blit( surface , (0, 0) )
        
    def __str__( self ):
        return "Polygon { Vertices = " + str( self._vertices ) + ", Color = " + str( self._color ) + "}"

'''
Unit testing
'''
def main():
    test1 = Polygon.rand_triangle( IMG_WIDTH , IMG_HEIGHT )
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