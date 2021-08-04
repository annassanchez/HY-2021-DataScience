#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep = "\t")
    df = df.replace({"New": np.nan, "Re": np.nan})
    special_df = df.loc[(df['Pos'] > df['LW'].astype(float)), :]
    return special_df

def main():
    special_missing_values()

if __name__ == "__main__":
    main()
