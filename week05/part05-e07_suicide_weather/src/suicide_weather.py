#!/usr/bin/env python3

import pandas as pd

def temperatures():
    df = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html", header= 0, index_col=0)
    df = df[0]
    df.iloc[:,0] = df.iloc[:,0].str.replace("\u2212", "-").astype(float)
    return df


def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv")
    df = df.drop(["year","age", "sex"], axis= 1)
    df["ratio"] = df["suicides_no"] / df["population"]
    df2 = df.groupby("country").mean()
    return df2["ratio"]
    
def suicide_weather():
    df = temperatures()
    df2 = suicide_fractions() 
    df3 = pd.concat([df, df2.fillna(0)], axis=1).dropna()       # Suicide NaN data is ok here for some reason
    df4 = pd.concat([df, df2], axis=1).dropna()                 # But not here
    return df2.shape[0], df.shape[0], df3.shape[0], df4.iloc[:,0].corr(df4.iloc[:,-1], method = "spearman")
 
def main():
    info= suicide_weather()
    print(f"Suicide DataFrame has {info[0]} rows")
    print(f"Temperature DataFrame has {info[1]} rows")
    print(f"Common DataFrame has {info[2]} rows")
    print(f"Spearman correlation: {info[3]}")

if __name__ == "__main__":
    main()
