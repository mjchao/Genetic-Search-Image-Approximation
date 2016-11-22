'''
Created on Sep 14, 2015

@author: mjchao
'''

from Parameters import N , K , T , IMG_WIDTH , IMG_HEIGHT , OUTPUT_DIR , IMG_PIXEL_ARRAY
from GeneticCode import GeneticCode
from PIL import Image, ImageDraw
from random import randint , uniform
from Utils import save_surface , loadImage, euclideanDistance,\
    convertToPixelArray
from time import sleep
import sys


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
        
    @staticmethod
    def save_code_as_image( code , gen ):
        filename = OUTPUT_DIR + "/" + str( gen ) + ".png"
        save_surface( code._surface , filename )
        
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
   
def main(): 
    codes = Search.search()
        
if __name__ == "__main__" : main()
