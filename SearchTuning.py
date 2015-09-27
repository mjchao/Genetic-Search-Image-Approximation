'''
Created on Sep 27, 2015

@author: mjchao
'''
from Parameters import N, K, T, E
from Search import Search

def tune( dataFilename ):
    Nvalues = [1, 2, 4, 8]
    Kvalues = [1, 2, 4, 8]
    
    print "Starting"
    for n in Nvalues:
        print n
        for k in Kvalues:
            print k
            N = n
            K = k
            t = int((E - N)/K)
            T = t
            print T
            results = Search.search()
            f = open( dataFilename , 'a' )
            f.write( str( N ) + " " + str( K ) + " " + str( T ) + " " + str( results[ 0 ].get_fitness() ) )
            f.close()
    

tune( "mona_lisa_tuning.out" )
