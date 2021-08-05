#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    kk = pd.read_csv("src/presidents.tsv", sep="\t")
    kk['Start'] = kk['Start'].str.split(expand=True)[0]
    kk = kk.replace("-", np.nan) 
    kk = kk.replace("two", 2) 
    kk['President'] = kk['President'].str.title()
    kk[["surname", "name"]] = kk['President'].str.split(",", expand = True)
    kk["name"] = kk["name"].fillna('', axis = 0)
    kk['President'] = (kk['name'] + " " + kk["surname"]).str.lstrip()
    kk['Vice-president'] = kk['Vice-president'].str.title()
    kk[["surname", "name"]] = kk['Vice-president'].str.split(",", expand = True)
    kk["name"] = kk["name"].fillna('', axis = 0)
    kk['Vice-president'] = (kk['name'] + " " + kk["surname"]).str.lstrip()
    kk.drop(["name", "surname"], inplace = True, axis = 1)
    kk = kk.astype({'President':object, 'Start': int, 'Last':float, 'Seasons':int, 'Vice-president':object})
    return kk

def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()
