'''
Created on Sep 27, 2015

@author: mjchao
'''
from Parameters import N, K, T, E
from Search import Search

def tune( dataFilename ):
    Nvalues = [1, 2, 4, 8]
    Kvalues = [1, 2, 4, 8]
    
    for n in Nvalues:
        for k in Kvalues:
            t = int((E - N)/T)
            N = n
            K = k
            T = t
            results = Search.search()
            f = open( dataFilename , 'a' )
            f.write( str( N ) + " " + str( K ) + " " + str( T ) + " " + str( results[ 0 ].get_fitness() ) )
            f.close()
    

tune( "mona_lisa_tuning.out" )