#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    municipalities = pd.read_csv("src/municipal.tsv", sep="\t", index_col = 'Region 2018')[1:312]
    return municipalities
    
def main():
    municipalities_of_finland()
    
if __name__ == "__main__":
    main()
