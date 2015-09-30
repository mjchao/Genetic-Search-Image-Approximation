'''
Created on Sep 26, 2015

@author: mjchao
'''
def gen( directory ):
    cmd = "python pngmerge.py -o anim.png -dn 15 "
    for i in range( 0 , 501 ):
        genNum = i * 1000
        pngFile = directory + "/" + str(genNum) + ".png"
        cmd += pngFile + " "
    
    print cmd
    
gen( "turing" )