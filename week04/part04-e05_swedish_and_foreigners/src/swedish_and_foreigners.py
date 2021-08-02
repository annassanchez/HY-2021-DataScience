#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    municipalities = pd.read_csv("src/municipal.tsv", sep="\t", index_col = 'Region 2018')[1:312]
    swedish = municipalities[(municipalities['Share of Swedish-speakers of the population, %'] > 5) & (municipalities['Share of foreign citizens of the population, %'] > 5)]
    swedish = swedish[['Population', 'Share of Swedish-speakers of the population, %', 'Share of foreign citizens of the population, %']]
    return swedish

def main():
    swedish_and_foreigners()

if __name__ == "__main__":
    main()
