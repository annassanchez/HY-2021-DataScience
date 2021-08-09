#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    company = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    comps = company.groupby("Publisher")
    wkcomps = comps["WoC"].sum()
    wkcomps = wkcomps.sort_values(ascending=False)
    publ = wkcomps.head(1)
    p=publ.index[0]
    topsingles = company[company["Publisher"] == p]
    #print(wkcomps.index[wkcomps[0]].tolist())
    return topsingles

def main():
    best_record_company()
    

if __name__ == "__main__":
    main()
