'''
Created on Sep 27, 2015

@author: mjchao
'''
import Parameters

def tune( dataFilename ):
    Nvalues = [1, 2, 4, 8]
    Kvalues = [1, 2, 4, 8]
    
    print "Starting"
    for n in Nvalues:
        print n
        for k in Kvalues:
            print k
            Parameters.N = n
            Parameters.K = k
            t = int((Parameters.E - Parameters.N)/Parameters.K)
            Parameters.T = t
            print Parameters.T
            from Search import Search
            results = Search.search()
            f = open( dataFilename , 'a' )
            f.write( str( Parameters.N ) + " " + str( Parameters.K ) + " " + str( Parameters.T ) + " " + str( results[ 0 ].get_fitness() ) + "\n" )
            f.close()
    

tune( "haystack_tuning.out" )
