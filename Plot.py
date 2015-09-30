'''
Created on Sep 25, 2015

@author: mjchao
'''
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

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
        
    @staticmethod
    def plot_tuning( tuning_stats ):
        f = open( tuning_stats , 'r' )
        x = []
        y = []
        z = []
        for line in f.readlines():
            data = [ float(s) for s in line.split( " " ) ]
            n = data[ 0 ]
            k = data[ 1 ]
            fitness = data[ 3 ]
            x.append( n )
            y.append( k )
            z.append( fitness )
            
        x = np.array( x )
        y = np.array( y )
        z = np.array( z )
        
        fig = plt.figure()
        
        ax = fig.gca(projection='3d')
        xPlot, yPlot = np.meshgrid([1, 2, 4, 8], [1, 2, 4, 8])
        zPlot = [[0 for _ in range(4)] for _ in range(4)]
        for i in range( 0 , len(xPlot) ):
            for k in range( 0 , len(xPlot) ):
                for j in range( 0 , len( x ) ):
                    if ( x[ j ] == xPlot[ i ][ k ] and y[ j ] == yPlot[ i ][ k ] ):
                        zPlot[ i ][ k ] = z[ j ]
        
        print zPlot
        ax.plot_surface(xPlot, yPlot, zPlot , linewidth=1 , rstride=1, cstride=1 , cmap = cm.coolwarm , antialiased=False)
        ax.set_xlabel( "N" )
        ax.set_ylabel( "K" )
        ax.set_zlabel( "Fitness" )
        plt.show()
         
    @staticmethod
    def plot_tuning_average( files ):
        indices = {
                   1:0 ,
                   2:1 ,
                   4:2 ,
                   8:3 ,
        }
        xPlot , yPlot = np.meshgrid( [1, 2, 4, 8], [1, 2, 4, 8] )
        zPlot = [[0 for _ in range(4)] for _ in range(4)]
        for filename in files:
            f = open( filename , 'r' )
            for line in f.readlines():
                data = [float(s) for s in line.split( " " ) ]
                n = data[ 0 ]
                k = data[ 1 ]
                fitness = data[ 3 ]
                xIndex = indices[ n ]
                yIndex = indices[ k ]
                zPlot[ xIndex ][ yIndex ] += fitness
         
        maxFitness = 0
        maxIdx = ( -1, -1 )
        for i in range(4):
            for j in range(4):
                zPlot[ i ][ j ] = zPlot[ i ][ j ] / float(len( files ))
                if ( zPlot[ i ][ j ] > maxFitness ):
                    maxFitness = zPlot[ i ][ j ] 
                    maxIdx = (i, j)   
                
        print maxFitness
        print maxIdx  
        #zPlot = zPlot / float(len( files ))
        #print np.max( zPlot )
        #print np.argmax( zPlot )
        
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_surface(xPlot, yPlot, zPlot , linewidth=1 , rstride=1, cstride=1 , cmap = cm.coolwarm , antialiased=False)
        ax.set_xlabel( "N" )
        ax.set_ylabel( "K" )
        ax.set_zlabel( "Average Fitness" )
        plt.show()
                
         
    
Plot.plot_data( "turing.out" )
#Plot.plot_tuning( "turing_tuning.out" )
#Plot.plot_tuning_average([ "darwin_tuning.out" , "haystack_tuning.out" , "michigan_tuning.out" , "mona_lisa_tuning.out" , "turing_tuning.out"] )
    
        