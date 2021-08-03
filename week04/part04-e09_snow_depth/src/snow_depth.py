#!/usr/bin/env python3

import pandas as pd

def snow_depth():  
    df = pd.read_csv('src/kumpula-weather-2017.csv', sep = ',')   
    snow = df.loc[:, ['Snow depth (cm)']]
    max_snow = snow.describe()
    return max_snow.iloc[-1,-1]

def main():
    proportion = snow_depth()
    print(f"Max snow depth: {proportion:.1f}")

if __name__ == "__main__":
    main()
