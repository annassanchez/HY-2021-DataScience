#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    kk = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep = ';', header = 0)
    kk = kk.dropna(axis=0, how='all')
    kk = kk.dropna(axis=1, how='all')
    kk[["Weekday", "Day", "Month", "Year", "Hour"]] = kk['Päivämäärä'].str.split(expand=True)

    kk[["Day"]] = kk[["Day"]].astype(int)
    kk[["Weekday"]] = kk[["Weekday"]].replace({"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", 
        "pe": "Fri", "la": "Sat", "su": "Sun"})
    kk[["Month"]] = kk[["Month"]].replace({"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, 
        "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, "syys": 9, "loka": 10, "marras": 11,
        "joulu": 12})#.map(int)
    kk["Year"] = kk["Year"].map(int)
    kk["Hour"] = kk["Hour"].str.split(":", expand=True)[0].map(int)
    #kk['Päivämäärä'] = kk["Weekday"] + " " + kk["Day"] + " " + kk["Month"] + " " + kk["Year"] + " " + kk["Hour"].map(str)
    kk = kk[kk.columns.tolist()[-5:]]
    #kk
    return kk

def main():
    split_date()
       
if __name__ == "__main__":
    main()
