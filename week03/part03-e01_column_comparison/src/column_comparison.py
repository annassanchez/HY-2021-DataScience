#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    a_1 = a[:, -2 ]
    a_2 = a[:, 1 ]
    c = a_1 < a_2
    return a[c]
    
def main():
    pass

if __name__ == "__main__":
    main()
