#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    m = df[df['Population change from the previous year, %']>0]
    return m.shape[0]/df.shape[0]

def main():  
    filename = "src/municipal.tsv"
    df = pd.read_csv(filename,sep='\t')
    statement = "Proportion of growing municipalities:" 
    proportion = "{:.1f}%".format(growing_municipalities(df)*100)
    print(statement,proportion)

if __name__ == "__main__":
    main()
