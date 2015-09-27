'''
Created on Sep 12, 2015

@author: mjchao
'''

from Parameters import IMG_WIDTH , IMG_HEIGHT
from Polygon import Polygon
from random import randint , gauss
import copy

class Mutator( object ):
    
    '''
    Replaces a polygon with a random new triangle.
    '''
    @staticmethod
    def __mutate1__( code ):
        idxToChange = randint( 0 , len( code._polygons )-1 )
        code._polygons[ idxToChange ] = Polygon.rand_n_gon( 3 , IMG_WIDTH , IMG_HEIGHT )
    
    '''
    Swaps the positions of two polygons in the ordered list of the genetic code.
    '''
    @staticmethod
    def __mutate2__( code ):
        idx1 = randint( 0 , len( code._polygons )-1 )
        idx2 = randint( 0 , len( code._polygons )-1 )
        code._polygons[ idx1 ] , code._polygons[ idx2 ] = code._polygons[ idx2 ] , code._polygons[ idx1 ]
    '''
    Returns a slightly altered color parameter.
    
    @param colorValue - a value in the range 0-255
    @return - the given color value plus/minus some random offset
    from -9 to 9
    '''
    @staticmethod
    def __alter_color( colorValue ):
        #change = randint( -25 , 25 )
        
        #use a normal distribution for color
        #so that drastic color changes can still happen.
        #in many cases, we need a drastic color change.
        change = int( gauss( 0 , 25 ) )
        changedValue = colorValue + change
        if ( changedValue < 0 ):
            return 0
        elif( changedValue > 255 ):
            return 255
        else:
            return changedValue
    '''
    Slightly alters a polygon's color in the genetic code
    '''
    @staticmethod
    def __mutate3__( code ):
        idxToChange = randint( 0 , len( code._polygons )-1 )
        polygon = code._polygons[ idxToChange ]
        currColor = polygon.get_color()
        newR = Mutator.__alter_color( currColor[ 0 ] )
        newG = Mutator.__alter_color( currColor[ 1 ] )
        newB = Mutator.__alter_color( currColor[ 2 ] )
        newA = Mutator.__alter_color( currColor[ 3 ] )
        newColor = ( newR , newG , newB , newA )
        polygon.set_color( newColor )
    
    '''
    Slightly alters the position of a polygon's vertices
    '''
    @staticmethod
    def __mutate4__( code ):
        for polygon in code._polygons:
            for i in range( 0 , len( polygon._vertices ) ):
                currX = polygon._vertices[ i ][ 0 ]
                dx = int( gauss( 0 , IMG_WIDTH/10 ) )
                newX = currX + dx
                
                currY = polygon._vertices[ i ][ 1 ]
                dy = int( gauss( 0 , IMG_HEIGHT/10 ) )
                newY = currY + dy
                
                polygon._vertices[ i ] = (newX , newY)
    
    '''
    Adds a vertex to a polygon in the genetic code.
    '''
    @staticmethod 
    def __mutate5__( code ):
        idxToChange = randint( 0 , len( code._polygons )-1 )
        polygon = code._polygons[ idxToChange ]
        newVertex = Polygon.rand_xy( IMG_WIDTH , IMG_HEIGHT )
        polygon._vertices.append( newVertex ) 
    
    '''
    Removes a vertex from a polygon, if possible, in the genetic code.
    '''
    @staticmethod
    def __mutate6__( code ):
        idxToChange = randint( 0 , len( code._polygons )-1 )
        polygon = code._polygons[ idxToChange ]
        if ( len( polygon._vertices ) <= 3 ):
            return
        else:
            vertexIdx = randint( 0 , len( polygon._vertices )-1 )
            del polygon._vertices[ vertexIdx ]
            
    '''
    Selects a random mutation to apply to a polygon that 
    will alter its shape
    '''
    @staticmethod   
    def __mutate_alter_shape__( code ):
        mutationsList = [ Mutator.__mutate4__ , Mutator.__mutate6__ ]
        mutationIdx = randint( 0 , len( mutationsList)-1 )
        mutationsList[ mutationIdx ]( code )
        
    '''
    
    '''
    @staticmethod
    def __mutate_modify_polygon__( code ):
        mutationsList = [ Mutator.__mutate3__ , Mutator.__mutate_alter_shape__ ]
        mutationIdx = randint( 0 , len(mutationsList)-1 )
        mutationsList[ mutationIdx ]( code )
        
    '''
    Selects a random mutation to apply to a polygon.
    This mutation happens for sure. It is the responsibility
    of the caller to ensure that mutations occur
    with some probability.
    '''
    @staticmethod
    def mutate( code ):
        mutationsList = [ Mutator.__mutate1__ , Mutator.__mutate2__ , \
                         Mutator.__mutate_modify_polygon__ , Mutator.__mutate_modify_polygon__ , \
                         Mutator.__mutate_modify_polygon__ ]
        mutationIdx = randint( 0 , len( mutationsList )-1 )
        mutationsList[ mutationIdx ]( code )
'''
Unit testing 
'''
def main():
    from GeneticCode import GeneticCode 
    unmutated = GeneticCode()
    mutated = copy.deepcopy( unmutated )
    
    Mutator.__mutate1__( mutated ) 
    assert str( unmutated ) != str( mutated )
    
    mutated = copy.deepcopy( unmutated )
    Mutator.__mutate2__( mutated )
    assert str( unmutated ) != str( mutated )
    
    mutated = copy.deepcopy( unmutated )
    Mutator.__mutate3__( mutated )
    assert str( unmutated ) != str( mutated )
    
    mutated = copy.deepcopy( unmutated )
    Mutator.__mutate4__( mutated )
    assert str( unmutated ) != str( mutated )
    
    mutated = copy.deepcopy( unmutated )
    Mutator.__mutate5__( mutated )
    assert str( unmutated ) != str( mutated )
    
    #should not be able to delete vertices from 3-gons
    mutated = copy.deepcopy( unmutated )
    Mutator.__mutate6__( mutated )
    assert str( unmutated ) == str( mutated )
    
    #have to have at least 4-gons before we can test deleting vertices
    unmutated = GeneticCode.rand_genetic_code_with_n_gons( 4 )
    mutated = copy.deepcopy( unmutated )
    Mutator.__mutate6__( mutated )
    assert str( unmutated ) != str( mutated )
    
    mutated = copy.deepcopy( unmutated )
    Mutator.mutate( mutated )
    assert str( unmutated ) != str( mutated )
    
    print str( unmutated )
    print str( mutated )
    
    print "Mutator unit testing passed."

if __name__ == "__main__" : main()
    