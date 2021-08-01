#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    current_index = s.index
    current_values = s.values
    inverse = pd.Series(current_index, index = current_values)
    return inverse

def main():
    inverse_series(pd.Series([1,2,3], index = ['a','b','c']))

if __name__ == "__main__":
    main()
