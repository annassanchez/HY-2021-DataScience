#!/usr/bin/env python3

import pandas as pd

def top_bands():
  #url_top40 = 'https://raw.githubusercontent.com/annassanchez/HY-2021-DataScience/main/week05/UK-top40-1964-1-2.tsv'
  #url_bands = 'https://raw.githubusercontent.com/annassanchez/HY-2021-DataScience/main/week05/bands.tsv'
  df_top40 = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
  df_top40['Artist'] = df_top40['Artist'].str.title()
  df_bands = pd.read_csv('src/bands.tsv', sep='\t')
  df_topBands = pd.merge(df_top40, df_bands, left_on='Artist', right_on='Band', how = 'right')
  return df_topBands

def main():
    df = top_bands()
    print("Shape:", df.shape)
    print("Columns:", df.columns)

if __name__ == "__main__":
    main()
