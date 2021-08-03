#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", index_col=0, sep="\t")
    df = df.iloc[:, [1,2]]
    return df.head(10)

def main():
    subsetting_by_positions().head(10)

if __name__ == "__main__":
    main()
