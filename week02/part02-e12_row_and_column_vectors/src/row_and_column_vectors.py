#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    b = a.shape[0]
    c= np.split(a, b, axis =0)    
    return c
def get_column_vectors(a):
    b = a.shape[1]
    c= np.split(a, b, axis = 1)    
    return c

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
