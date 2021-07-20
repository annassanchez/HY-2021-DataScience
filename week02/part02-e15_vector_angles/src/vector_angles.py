#!/usr/bin/env python3

import numpy as np

def vector_angles(a,b):
    x = np.sqrt(np.sum(np.square(a),axis=1))
    y = np.sqrt(np.sum(np.square(b),axis=1))
    tmp = np.sum(a * b,axis=1) / (x * y)
    angle = np.arccos( np.clip( tmp, -1.0, 1.0 ) )
    degrees = np.degrees(angle)
    return degrees

def main():
    np.random.seed(4)
    a = np.random.randint(0, 10, (3,3))
    b = np.random.randint(0, 10, (3,3))
    vector_angles(a,b)

if __name__ == "__main__":
    main()
