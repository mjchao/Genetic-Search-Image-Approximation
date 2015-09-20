'''
Created on Sep 14, 2015

@author: mjchao
'''

from Parameters import N , K , T , E
from GeneticCode import GeneticCode
from random import randint
import pygame
from pygame.locals import QUIT , KEYDOWN , K_ESCAPE

class Search( object ):
    
    @staticmethod
    def fitness_comparator( code1 , code2 ):
        if ( code2.get_fitness() > code1.get_fitness() ):
            return -1
        elif ( code1.get_fitness() > code2.get_fitness() ):
            return 1
        else:
            return 0
        
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
            codes = codes[ 0:N ]
            
            #repeat T times 

        return codes
        
codes = Search.search()
pygame.init()
screen = pygame.display.set_mode( (32, 32) )
screen.fill( (0, 0, 0) )
codes[ 0 ].draw_onto_screen( screen )
pygame.display.update()

state = 0
while state == 0:
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            state = 1
            break
