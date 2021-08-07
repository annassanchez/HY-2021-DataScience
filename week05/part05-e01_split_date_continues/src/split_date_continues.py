#!/usr/bin/env python3

import pandas as pd
import numpy as np

#df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep = ';', header = 0)

def split_date(df):
    df = df.dropna(axis=0, how='all')
    df = df.dropna(axis=1, how='all')
    df[["Weekday", "Day", "Month", "Year", "Hour"]] = df['Päivämäärä'].str.split(expand=True)
    df[["Weekday"]] = df[["Weekday"]].replace({"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", 
        "pe": "Fri", "la": "Sat", "su": "Sun"})
    df[["Month"]] = df[["Month"]].replace({"tammi": "1", "helmi": "2", "maalis": "3", "huhti": "4", 
        "touko": "5", "kesä": "6", "heinä": "7", "elo": "8", "syys": "9", "loka": "10", "marras": "11",
        "joulu": "12"})
    df["Hour"] = df["Hour"].str.split(":", expand=True)[0].map(int)
    df['Päivämäärä'] = df["Weekday"] + " " + df["Day"] + " " + df["Month"] + " " + df["Year"] + " " + df["Hour"].map(str)
    df = df[df.columns.tolist()[-5:] + [df.columns.tolist()[0]]]
    return df.astype({"Weekday":object, "Day":int,  "Month":int, "Year":int, "Hour": int})

def split_date_continues():
    #d = split_date()
    data = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep = ';', header = 0)
    d = split_date(data)
    data = data.dropna(axis=0, how='all')
    data = data.dropna(axis=1, how='all')
    #data.drop(['Päivämäärä'], inplace = True, axis = 1)
    final = pd.concat([d, data], axis = 1)
    final.drop([final.columns.tolist()[5]],inplace = True, axis = 1)
    #final['Day'] = final['Day'].astype(int)
    return final#.astype({"Weekday":object, "Day":int,  "Month":int, "Year":int, "Hour": float})


def main():
    #df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep = ';', header = 0)
    #split_date(df)
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
