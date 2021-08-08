#!/usr/bin/env python3

import pandas as pd


def cycling_weather():
  #url_weather = 'https://raw.githubusercontent.com/annassanchez/HY-2021-DataScience/main/week05/kumpula-weather-2017.csv'
  #url_cycling = 'https://raw.githubusercontent.com/annassanchez/HY-2021-DataScience/main/week05/Helsingin_pyorailijamaarat.csv'
  df_weather = pd.read_csv('src/kumpula-weather-2017.csv', sep=',')
  df_cycling = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
  df_cycling = df_cycling.dropna(axis=0, how="all").dropna(axis=1, how="all")
  df_cycling[["Weekday", "Day", "Month", "Year", "Hour"]] = df_cycling['Päivämäärä'].str.split(expand=True)
  df_cycling[["Month"]] = df_cycling[["Month"]].replace({"tammi": "1", "helmi": "2", "maalis": "3", 
                                                          "huhti": "4", "touko": "5", "kesä": "6", 
                                                          "heinä": "7", "elo": "8", "syys": "9", 
                                                          "loka": "10", "marras": "11", "joulu": "12"})
  df_cycling = df_cycling.astype({"Weekday": object, "Day": int, "Month": int, "Year": int})
  df_cyc_weat = pd.merge(df_weather, df_cycling, left_on=['d', 'm', 'Year'], 
                          right_on=["Day", "Month", "Year"])
  df_cyc_weat.drop(['m', 'd', 'Time', 'Time zone', 'Päivämäärä'], inplace=True, axis = 1)
  return df_cyc_weat

def main():
    cycling_weather()

if __name__ == "__main__":
    main()
