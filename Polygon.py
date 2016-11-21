'''
Created on Sep 12, 2015

@author: mjchao
'''

from Parameters import IMG_WIDTH , IMG_HEIGHT
from PIL import Image, ImageDraw
from random import randint , gauss
import Utils

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
    Returns a coordinate (x, y) near the given point. The (x, y)
    are generated with a gaussian distribution with mean
    (x, y) and standard deviation of the width and height of the
    image divided by 10, respectively. 
    '''
    @staticmethod
    def gauss_xy_about_point( point ):
        return ( int(gauss( point[ 0 ] , IMG_WIDTH/10 )) , int(gauss( point[ 1 ] , IMG_HEIGHT/10)) )
    
    '''
    Returns a random (r, g, b, a) value
    '''
    @staticmethod
    def rand_rgba():
        return ( randint( 0 , 255 ) , randint( 0 , 255 ) , randint( 0 , 255 ) , randint( 0 , 255 ) )
    
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
        center = Polygon.rand_xy( maxX , maxY )
        return Polygon( [Polygon.gauss_xy_about_point( center ) for _ in range( 0 , n )]  , Polygon.rand_rgba() )
        
    
    '''
    Creates a polygon.
    '''
    def __init__( self , vertices = None , color = None ):
        if vertices is None:
            self._vertices = [Polygon.rand_xy(IMG_WIDTH , IMG_HEIGHT) for _ in range( 0 , 3 ) ]
        else:
            self._vertices = vertices
            
        if color is None:
            self._color = Polygon.rand_rgba()
        else :
            self._color = color
        
    '''
    Returns the number of vertices this polygon has. 
    '''   
    def num_vertices( self ):
        return len( self._vertices )
      
    '''
    Returns the color of this polygon as an (r, g, b, a) tuple
    '''
    def get_color( self ):
        return self._color  
    '''
    Sets the color of this polygon.
    
    @param color - the (r, g, b, a) color for this polygon as a tuple
    '''
    def set_color( self , color ):
        self._color = color
        
    def __str__( self ):
        return "Polygon { Vertices = " + str( self._vertices ) + ", Color = " + str( self._color ) + "}"    
    
if __name__ == "__main__" : main()
