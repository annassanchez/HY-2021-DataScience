# Enter you module contents here
'triangle stuff'
import math

__author__ = "annassanchez"
__version__ = "0.1"

def hypothenuse(a,b):
    '''Calculates the hytothenusa of two given sides in a right-angle triangle'''
    return math.sqrt(a**2 + b**2)

def area(base, height):
    '''calculates the area of a triangle given the base and the height'''
    return ((base*height) / 2 )