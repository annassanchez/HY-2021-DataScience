#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    # Create DataFrame
    path = 'src/UK-top40-1964-1-2.tsv'
    #path = '/Users/carlnysten/Library/Application Support/Code/User/globalStorage/moocfi.test-my-code/tmcdata/TMC workspace/Exercises/hy/hy-data-analysis-with-python-2020/part04-e15_last_week/src/UK-top40-1964-1-2.tsv'
    df = pd.read_csv(path, sep='\t')
    # Modify values in last week column and clear entries that weren't on last week's list
    df.LW[df.LW == 'New'] = '1000'
    df.LW[df.LW == 'Re'] = '1000'
    df.LW = df.LW.astype('int')
    indices = df.index[df.LW == 1000].tolist()
    df.iloc[indices] = np.nan
    # Peak pos 
    df['Peak Pos'].mask((df.LW > df['Peak Pos']) & (df.Pos == df['Peak Pos']), inplace=True)
    # Create New DataFrame of last week
    last_week = df.copy()
    last_week.Pos = df.LW
    # Clear the whole LW column in last_week, 
    # because we can't know positions of songs from two weeks ago
    last_week.LW = None
    # Find missing positions
    all_positions = set(range(1,41))
    existing_positions = set(last_week.Pos[pd.notna(last_week.Pos)].tolist())
    missing_positions = list(all_positions - existing_positions)
    # Insert missing positions into last_week
    last_week.Pos[pd.isna(last_week.Pos)] = missing_positions
    # Sort last_week based on the position column and reset indices
    last_week.sort_values('Pos', axis='index', inplace=True)
    last_week.reset_index(inplace=True, drop=True)
    # Subtract one from WOC, weeks on chart
    last_week.WoC = last_week.WoC -1
    return last_week

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
