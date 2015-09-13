'''
Created on Sep 12, 2015

@author: mjchao
'''
from Parameters import IMG_WIDTH , IMG_HEIGHT , N
from Polygon import Polygon

'''
Represents a Genetic Code to be used in the genetic search.
In our search problem, the genetic code is a list of Polygon
objects.
'''
class GeneticCode( object ):
    
    '''
    Creates a GeneticCode object. By default, it's a random list of N
    triangles.
    '''
    def __init__( self , polygons = None ):
        if polygons is None:
            self._polygons = [ Polygon.rand_triangle( IMG_WIDTH , IMG_HEIGHT ) for _ in range( 0 , N ) ]
        else:
            self._polygons = polygons
        self._fitness = -1
        pass
    
    '''
    Mutates this genetic code with some probability. This object is modified
    with a random mutation.
    '''
    def mutate( self ):
        pass
    
    '''
    Gets the polygon at the given index in the list of polygons
    of which this genetic code consists
    '''
    def get( self , idx ):
        return self._polygons[ idx ]
    
    '''
    Sets the polygon at the given index to be the
    given polygon.
    '''
    def set( self , idx , newPolygon ):
        self._polygons[ idx ] = newPolygon
        
    '''
    Returns the fitness score of this genetic code.
    '''
    def get_fitness( self ):
        if ( self._fitness != -1 ):
            return self._fitness
        else:
            #TODO
            pass
         
    '''
    Returns the number of polygons of which this
    genetic code consists
    '''   
    def size( self ):
        return len( self._polygons )
    
    '''
    Crosses two polygons and produces a third
    polygon with traits from both parent polygons.
    '''
    @staticmethod
    def cross( polygon1 , polygon2 ):
        pass
        #TODO
        
    '''
    Crosses an arbitrary number of polygons and
    produces an offspring with traits from all
    parent polygons.
    '''
    @staticmethod
    def crossN( *polygons ):
        pass
        #TODO
        
    def __str__( self ):
        return "GeneticCode {Polygons = " + ', '.join( str(x) for x in self._polygons ) + ", fitness = " + str( self._fitness ) + "}"

'''
Unit Testing
'''
def main():
    test = GeneticCode()
    print test 

if __name__ == "__main__" : main()