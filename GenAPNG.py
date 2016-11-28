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

def genExp(directory):
	cmd = "python pngmerge.py -o anim.png -dn 15 "
	#cmd += "mjchao.png "
	genNum = 1

	pngFiles = []
	for i in range(0 , 10000):
		if genNum*1000 > 7000000:
			break
		pngFile = directory + "/" + str(int(genNum) * 1000) + ".png"
		pngFiles.append(pngFile)
		genNum *= 1.01
		genNum += 1
	pngFiles.append("mjchao.png")

	for i in range(len(pngFiles)):
		cmd += pngFiles[i] + " "
	for i in range(len(pngFiles)-1, 0, -1):
		cmd += pngFiles[i] + " "

	print cmd
	
    
genExp( "mjchao2" )
