import pygame
from Utils import *
from math import log10

orig = loadImage( "darwin.bmp" )
approx = loadImage( "darwin/darwin_test.png" )

origArray = convertToPixelArray( orig )
approxArray = convertToPixelArray( approx )

euclideanDist = euclideanDistance( origArray , approxArray )
fitness = -(log10(euclideanDist) - log10(norm( approxArray ) + norm( origArray ) ) )

print euclideanDist
print fitness
