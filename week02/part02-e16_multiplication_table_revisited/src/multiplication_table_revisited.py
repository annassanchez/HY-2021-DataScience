#!/usr/bin/env python3

import numpy as np

def multiplication_table(number):
    a = np.arange(number)[np.newaxis]
    b = a.transpose()
    result = a*b
    return result

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
