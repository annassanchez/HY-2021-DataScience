#!/usr/bin/env python3

import numpy as np
import functools

def matrix_power(a, n): 
    if n == 0:
        size = int(a.shape[0])
        a_power = np.eye(size)
    elif n > 0:
        iter = (a for i in range(n-1))
        a_power = functools.reduce((lambda x, y: x@y), iter, a)
    elif n < 0:
        iter = (a for i in range(n))
        a_power = functools.reduce((lambda x, y: x@y), (np.linalg.inv(a) for i in range(-n-1)), np.linalg.inv(a))
    return a_power

def main():
    return

if __name__ == "__main__":
    main()
