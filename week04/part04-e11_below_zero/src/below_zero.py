#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv", sep=",")
    below_zero_df = df.loc[df['Air temperature (degC)'] < 0]
    below_zero_days = below_zero_df.shape[0]
    return below_zero_days

def main():
    print(f"Number of days below zero: {below_zero():.0f}")
    
if __name__ == "__main__":
    main()
