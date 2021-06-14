#!/usr/bin/env python3

import math
from math import sqrt
import numpy as np 

def solve_quadratic(a, b, c):
    discriminant = (b**2) - (4*a*c)
    result1 = (-b + sqrt(discriminant)) / (2*a)
    result2 = (-b - sqrt(discriminant)) / (2*a)
    return (result1,result2)


def main():
    pass

if __name__ == "__main__":
    main()
