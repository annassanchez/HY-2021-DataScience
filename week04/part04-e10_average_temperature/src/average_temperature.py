#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    july_temp = df.loc[df['m'] == 7,:]
    avg_july_temp = july_temp['Air temperature (degC)'].mean()
    return avg_july_temp

def main():
    proportion = average_temperature()
    print(f"Average temperature in July: {proportion:.1f}")

if __name__ == "__main__":
    main()
