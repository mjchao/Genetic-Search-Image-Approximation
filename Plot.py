'''
Created on Sep 25, 2015

@author: mjchao
'''
import numpy as np
import matplotlib.pyplot as plt
import re

class Plot( object ):
    
    @staticmethod
    def plot_data( fitness_stats ):
        f = open( fitness_stats , 'r' )
        x = []
        y = []
        for line in f.readlines():
            data = re.findall( r'\d*\.?\d+' , line )
            print str( data )
            if ( len( data ) >= 2 ):
                generation = data[ 0 ]
                fitness = data[ 1 ]
                x.append( generation )
                y.append( fitness )
         
        x = np.array( x )
        y = np.array( y )
        plt.plot( x , y )
        plt.xlabel( "Generations" )
        plt.ylabel( "Fitness" )
        plt.title( "Fitness Over Generations With N=1, K=1" )
        plt.show()
         
Plot.plot_data( "haystack.out" )   
        