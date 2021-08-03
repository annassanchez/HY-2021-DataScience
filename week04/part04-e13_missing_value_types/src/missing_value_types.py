#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    df = pd.DataFrame([['-', '-'], [1917, 'Niinistö'], [1776, "Trump"],[1523, '-'], ['-', 'Steinmeier'], 
    [1992, "Putin"]], columns = ['Year of independence', 'President'], 
    index = ["United Kingdom" , "Finland" , "USA", "Sweden", "Germany", "Russia"] ) 
    df = df.replace('-', np.nan)
    return df
               
def main():
    missing_value_types().dtypes

if __name__ == "__main__":
    main()
