'''
Created on Sep 14, 2015

@author: mjchao
'''

from Parameters import N , K , T , E
from GeneticCode import GeneticCode
from random import randint

class Search( object ):
    
    @staticmethod
    def fitness_comparator( code1 , code2 ):
        return code2.get_fitness() - code1.get_fitness()
        
    '''
    Performs the genetic search algorithm.
    '''
    @staticmethod
    def search():
        
        #start with N random genetic codes
        codes = [ GeneticCode() for _ in range( 0 , N ) ]
        
        for _ in range( 0 , T ):
            
            #pick K pairs of states and cross them.
            for _ in range( 0 , K ):
                parent1 = codes[ randint( 0 , N-1 ) ]
                parent2 = codes[ randint( 0 , N-1 ) ]
                codes.append( GeneticCode.cross( parent1 , parent2 ) )
            
            #keep N best states
            codes.sort( Search.fitness_comparator )
            codes = codes[ 0:N-1 ]
            
            #repeat T times 

        
Search.search()
