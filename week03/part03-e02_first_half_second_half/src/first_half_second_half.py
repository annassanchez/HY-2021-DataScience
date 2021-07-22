#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a): 
    num_cols = a.shape[1]
    num = int(num_cols/2)
    first_half = (np.sum(a[:, :num], axis=1))
    second_half = (np.sum(a[:, num:], axis=1))
    c = (first_half) > (second_half)
    return a[c]

def main():
    a = np.array([[8, 9, 3, 8],[0, 5, 3, 9], [5, 7, 6, 0], [7, 8, 1, 6]])
    print(first_half_second_half(a))
    pass

if __name__ == "__main__":
    main()
