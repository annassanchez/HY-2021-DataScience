#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def cyclists_per_day():
  #url_cyclist = 'https://raw.githubusercontent.com/annassanchez/HY-2021-DataScience/main/week05/Helsingin_pyorailijamaarat.csv'
  #df_cyclist = pd.read_csv(url_cyclist, sep=';')
  df_cyclist = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
  df_cyclist = df_cyclist.dropna(axis=0, how="all").dropna(axis=1, how="all")
  df_cyclist[["Weekday", "Day", "Month", "Year", "Hour"]] = df_cyclist['Päivämäärä'].str.split(expand=True)
  df_cyclist[["Month"]] = df_cyclist[["Month"]].replace({"tammi": "1", "helmi": "2", "maalis": "3", 
                                                          "huhti": "4", "touko": "5", "kesä": "6", 
                                                          "heinä": "7", "elo": "8", "syys": "9", 
                                                          "loka": "10", "marras": "11", "joulu": "12"})
  df_cyclist = df_cyclist.astype({"Weekday": object, "Day": int, "Month": int, "Year": int})
  test = df_cyclist.groupby(['Year', 'Month', 'Day']).sum()
  return test
    
def main():
    kk = cyclists_per_day().loc[(2017,8,)]
    kk.plot()
    plt.show()

if __name__ == "__main__":
    main()
