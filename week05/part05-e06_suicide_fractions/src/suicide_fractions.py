#!/usr/bin/env python3

import pandas as pd
import numpy as np

def suicide_fractions():
    df_suicide = pd.read_csv('src/who_suicide_statistics.csv', sep = ',')
    df_suicide['suicide_population'] = df_suicide['suicides_no'] / df_suicide['population']
    suicide = df_suicide.groupby(by = 'country')['suicide_population'].mean()
    return suicide

def main():
    suicide_fractions()

if __name__ == "__main__":
    main()
