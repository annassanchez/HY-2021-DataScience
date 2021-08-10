#!/usr/bin/env python3

import pandas as pd


def bicycle_timeseries():
    #url = 'https://raw.githubusercontent.com/annassanchez/HY-2021-DataScience/main/week05/Helsingin_pyorailijamaarat.csv'
    #kk = pd.read_csv(url, sep = ';', header = 0)
    kk = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep = ';', header = 0)
    kk = kk.dropna(axis=0, how='all')
    kk = kk.dropna(axis=1, how='all')
    kk[["Weekday", "Day", "Month", "Year", "Time"]] = kk['Päivämäärä'].str.split(expand=True)

    kk[["Weekday"]] = kk[["Weekday"]].replace({"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", 
        "pe": "Fri", "la": "Sat", "su": "Sun"})
    kk[["Month"]] = kk[["Month"]].replace({"tammi": "1", "helmi": "2", "maalis": "3", "huhti": "4", 
        "touko": "5", "kesä": "6", "heinä": "7", "elo": "8", "syys": "9", "loka": "10", "marras": "11",
        "joulu": "12"})
    kk["Hour"] = kk["Time"].str.split(":", expand=True)[0]#.map(str)
    kk["Minute"] = kk["Time"].str.split(":", expand=True)[1]#.map(str)
    kk['Päivämäärä'] = pd.to_datetime(kk[["Year", "Month", "Day", "Hour", "Minute"]], format = '%Y/%m/%d %H:%M')
    kk = kk.set_index("Päivämäärä")
    kk.drop(["Weekday", "Day", "Month", "Year", "Hour", "Minute", "Time"], axis = 1, inplace=True)
    return kk


def main():
    bicycle_timeseries()

if __name__ == "__main__":
    main()
