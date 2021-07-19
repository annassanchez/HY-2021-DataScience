#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    number = a.shape[0]
    squared = np.square(a)    
    added = squared.sum(axis=1)
    length = np.sqrt(added)
    reshaped_length = length.reshape(number,)
    return reshaped_length

def main():
    np.random.seed(9)
    b = np.random.randint(0, 10, (3,4))
    vector_lengths(b)
    print(vector_lengths(b))

if __name__ == "__main__":
    main()
