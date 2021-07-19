#!/usr/bin/env python3

import numpy as np

def diamond(number):
    #base array
    if number != 1:
        a = np.eye(number, dtype=int)
        b = a.T
        c = a[::-1][:,:-1]
        d = b[::-1][:,1-a.shape[0]:]
        concat01 = np.concatenate((c,a), axis = 1)
        concat02 = np.concatenate((b,d), axis = 1)[1:,:]
        concat = np.concatenate((concat01, concat02))
    elif number == 1:
        concat = np.eye(number, dtype=int)
    return concat

def main():
    pass

if __name__ == "__main__":
    main()
