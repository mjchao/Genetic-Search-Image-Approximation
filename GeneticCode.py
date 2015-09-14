'''
Created on Sep 12, 2015

@author: mjchao
'''
from Mutator import Mutator
from Parameters import IMG_WIDTH , IMG_HEIGHT , N
from Polygon import Polygon

import random
from random import uniform
import copy

'''
Represents a Genetic Code to be used in the genetic search.
In our search problem, the genetic code is a list of Polygon
objects.
'''
class GeneticCode( object ):
    
    MUTATION_PROBABILITY = 0.9
    
    '''
    Creates a random GeneticCode with N n-gons.
    '''
    @staticmethod
    def rand_genetic_code_with_n_gons( n ):
        polygons = [ Polygon.rand_n_gon( n , IMG_WIDTH , IMG_HEIGHT ) for _ in range( 0 , N ) ]
        return GeneticCode( polygons )
    
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
        randVal = uniform( 0 , 1 )
        if ( randVal <= GeneticCode.MUTATION_PROBABILITY ):
            Mutator.mutate( self )
    
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
            return 0
         
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
    def cross( code1 , code2 ):
        return GeneticCode.crossN( code1 , code2 )
        
    '''
    Crosses an arbitrary number of polygons and
    produces an offspring with traits from all
    parent polygons.
    '''
    @staticmethod
    def crossN( *codes ):
        numParents = len( codes )
        partitions = random.sample( range( 0 , N ) , numParents-1 )
        partitions.sort()
        partitions = [0] + partitions
        partitions.append( N )
        
        childPolygons = []
        for i in range( 0 , numParents ):
            childPolygons = childPolygons + copy.deepcopy( codes[ i ]._polygons[ partitions[i] : partitions[i+1] ] )

        return GeneticCode( childPolygons )
        
    def __str__( self ):
        return "GeneticCode {Polygons = " + ', '.join( str(x) for x in self._polygons ) + ", fitness = " + str( self._fitness ) + "}"

'''
Unit Testing
'''
def main():
    unmutated = GeneticCode.rand_genetic_code_with_n_gons( 5 )
    
    GeneticCode.MUTATION_PROBABILITY = 1
    mutated = copy.deepcopy( unmutated )
    mutated.mutate()
    assert str( unmutated ) != str( mutated )
    
    GeneticCode.MUTATION_PROBABILITY = 0
    mutated = copy.deepcopy( unmutated )
    mutated.mutate()
    assert str( unmutated ) == str( mutated )
    
    parent1 = GeneticCode.rand_genetic_code_with_n_gons( 4 )
    parent2 = GeneticCode.rand_genetic_code_with_n_gons( 4 )
    parent3 = GeneticCode.rand_genetic_code_with_n_gons( 4 )
    child = GeneticCode.crossN( parent1 , parent2 , parent3 )
    print str( parent1 )
    print str( parent2 )
    print str( parent3 )
    print str( child )
    
    child = GeneticCode.cross( parent1 , parent2 )
    print str( child )
    
    print "Genetic code unit testing passed."

if __name__ == "__main__" : main()