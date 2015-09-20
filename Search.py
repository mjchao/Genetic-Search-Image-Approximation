'''
Created on Sep 14, 2015

@author: mjchao
'''

from Parameters import N , K , T , IMG_WIDTH , IMG_HEIGHT , OUTPUT_DIR
from GeneticCode import GeneticCode
from random import randint
import pygame
from pygame.locals import QUIT , KEYDOWN , K_ESCAPE
from Utils import save_surface

class Search( object ):
    
    '''
    This puts the best codes first (higher fitness means
    lower comparator value).
    '''
    @staticmethod
    def fitness_comparator( code1 , code2 ):
        if ( code2.get_fitness() > code1.get_fitness() ):
            return 1
        elif ( code1.get_fitness() > code2.get_fitness() ):
            return -1
        else:
            return 0
        
    '''
    Performs the genetic search algorithm.
    '''
    @staticmethod
    def search():
        
        #start with N random genetic codes
        codes = [ GeneticCode() for _ in range( 0 , N ) ]
        
        for gen in range( 0 , T ):
            
            #pick K pairs of states and cross them.
            for childNum in range( 0 , K ):
                    
                parent1 = codes[ randint( 0 , N-1 ) ]
                parent2 = codes[ randint( 0 , N-1 ) ]
                child = GeneticCode.cross( parent1 , parent2 )
                child.mutate()
                codes.append( child )
                
                #save the image every 1000 children
                if ( (K * gen + childNum) % 1000 == 0 ):
                    print "Processing generation " + str( gen )
                    bestImg = max( codes , key = lambda p : p.get_fitness() )
                    #print bestImg.get_fitness()
                    filename = OUTPUT_DIR + "/" + str( gen ) + ".bmp"
                    surface = pygame.surface.Surface( (IMG_WIDTH, IMG_HEIGHT) , flags = pygame.SRCALPHA )
                    bestImg.draw_onto_surface( surface )
                    save_surface( surface , filename )
            
            #keep N best states
            codes.sort( Search.fitness_comparator )
            codes = codes[ 0:N ]
            #print str( codes[ 0 ].get_fitness() ) + " " + str( codes[ N-1 ].get_fitness() )
            
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
