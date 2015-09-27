'''
Created on Sep 14, 2015

@author: mjchao
'''

from Parameters import N , K , T , IMG_WIDTH , IMG_HEIGHT , OUTPUT_DIR , IMG_PIXEL_ARRAY
from GeneticCode import GeneticCode
from random import randint , uniform
import pygame
from pygame.locals import QUIT , KEYDOWN , K_ESCAPE
from Utils import save_surface , loadImage, euclideanDistance,\
    convertToPixelArray
from time import sleep
import sys

pygame.font.init()

class Search( object ):
    
    '''
    We use this window for taking screenshots and saving the image
    to a file. The normal surface object seems incapable of dealing
    with alpha values, so we have to actually blit to a window.
    We also have to add a bit of extra space at the bottom
    to draw the generation number.
    '''
    window = pygame.display.set_mode( (IMG_WIDTH , IMG_HEIGHT+10) ) 
    generationFont = pygame.font.SysFont( "Times New Roman" , 8 )
    
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
        
    @staticmethod
    def save_code_as_image( code , gen ):
        filename = OUTPUT_DIR + "/" + str( gen ) + ".png"
        
        #draw the generation number
        label = Search.generationFont.render( str( gen ) , 1 , (255,255,255) )
        Search.window.blit( label , (0 , IMG_HEIGHT+1 ) )
        
        #update screen before saving it
        pygame.display.update()
        save_surface( Search.window , filename )
        
    '''
    Performs the genetic search algorithm.
    '''
    @staticmethod
    def search():
        
        #start with N random genetic codes
        codes = [ GeneticCode() for _ in range( 0 , N ) ]
        
        for gen in range( 0 , T+1 ):
            
            sumFitness = sum( [ x.get_fitness() for x in codes ] )
            
            #pick K pairs of states and cross them.
            for childNum in range( 0 , K ):
                
                #select first parent proportional to fitness    
                key1 = uniform( 0 , sumFitness )
                currSum = 0
                for code in codes:
                    currSum += code.get_fitness()
                    if ( currSum > key1 ):
                        parent1 = code
                        break
                
                #select second parent proportional to fitness    
                key2 = uniform( 0 , sumFitness )
                currSum = 0
                for code in codes:
                    currSum += code.get_fitness()
                    if ( currSum > key2 ):
                        parent2 = code
                        break
                    
                child = GeneticCode.cross( parent1 , parent2 )
                child.mutate()
                codes.append( child )
                
                #save the image every 1000 children
                if ( (K * gen + childNum) % 1000 == 0 ):
                    bestCode = max( codes , key = lambda p : p.get_fitness() )
                    print "Processing generation " + str( gen ) + "; best fitness = " + str( bestCode.get_fitness() )
                    Search.save_code_as_image( bestCode , gen )
                    
            #keep N best states
            codes.sort( Search.fitness_comparator )
            codes = codes[ 0:N ]
            
            #repeat T times 

        #save the last image
        #print "Processing generation " + str( T-1 )
        #Search.save_code_as_image( codes[ 0 ] , T-1 )
        return codes
    
codes = Search.search()
pygame.init()
screen = pygame.display.set_mode( (32, 32) )
screen.fill( (0, 0, 0) )
codes[ 0 ].draw_onto_screen( screen )
save_surface( screen , OUTPUT_DIR + "/" + "final.bmp" )
pygame.display.update()

state = 0
while state == 0:
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            state = 1
            break
        
    state = 1
