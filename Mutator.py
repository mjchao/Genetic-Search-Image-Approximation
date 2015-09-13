'''
Created on Sep 12, 2015

@author: mjchao
'''
class Mutator( object ):
    
    mutationsList = [ Mutator.__mutate1__ ]
    '''
    Selects a random mutation to apply to a polygon.
    This mutation happens for sure. It is the responsibility
    of the caller to ensure that mutations occur
    with some probability.
    '''
    @staticmethod
    def mutate( polygon ):
        pass
    
    '''
    Replaces a polygon with a random new polygon of the same number
    of sides.
    '''
    @staticmethod
    def __mutate1__( polygon ):
        pass
    
    '''
    Slightly alters a polygon's color
    '''
    @staticmethod
    def __mutate3__( polygon ):
        pass
    
    '''
    Slightly alters the position of a polygon's vertices
    '''
    @staticmethod
    def __mutate4__( polygon ):
        pass 
    
    '''
    Adds a vertex to a polygon
    '''
    @staticmethod 
    def __mutate5__( polygon ):
        pass 
    
    '''
    Removes a vertex from a polygon, if possible
    '''
    @staticmethod
    def __mutate6__( polygon ):
        pass
    
'''
Unit testing 
'''
def main():
    pass 

if __name__ == "__main__" : main()
    