#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model
import numpy as np

def cycling_weather_continues(station):

    url_weather = 'src/kumpula-weather-2017.csv'
    df_weather = pd.read_csv(url_weather, sep=',')
    url_cycling = 'src/Helsingin_pyorailijamaarat.csv'
    df_cycling = pd.read_csv(url_cycling, sep=';').dropna(axis=0, how="all").dropna(axis=1, how="all")
    df_cycling[["Weekday", "Day", "Month", "Year", "Hour"]] = df_cycling['Päivämäärä'].str.split(expand=True)
    df_cycling = df_cycling.loc[df_cycling["Year"] == '2017', :]
    df_cycling[["Month"]] = df_cycling[["Month"]].replace({"tammi": "1", "helmi": "2", "maalis": "3", 
                                                                "huhti": "4", "touko": "5", "kesä": "6", 
                                                                "heinä": "7", "elo": "8", "syys": "9", 
                                                                "loka": "10", "marras": "11", "joulu": "12"})
    df_cycling = df_cycling.astype({"Weekday": object, "Day": np.int64, "Month": np.int64, "Year": np.int64})
    df_cycling = df_cycling.groupby(["Year","Month","Day"]).sum().reset_index()
    df_cyc_weat = pd.merge(df_weather, df_cycling, left_on=['d', 'm', 'Year'], 
                            right_on=["Day", "Month", "Year"])
                            
    df_cyc_weat= df_cyc_weat.fillna(method="ffill").drop(["m", "d", "Time", "Time zone"],axis=1)

    df = df_cyc_weat
    Y = df.loc[:, station]
    X = df.loc[:, ["Precipitation amount (mm)","Snow depth (cm)","Air temperature (degC)"]].ffill()
    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(X,Y)
    return (model.coef_, model.score(X,Y))
    
def main():
    x = "Baana"
    cofs, score = cycling_weather_continues(x)
    #print(cofs)
    print ("Measuring station: " + x)
    print("Regression coefficient for variable 'precipitation': {:.1f}".format(cofs[0]))
    print("Regression coefficient for variable 'snow depth': {:.1f}".format(cofs[1]))
    print("Regression coefficient for variable 'temperature': {:.1f}" .format(cofs[2]))
    print("Score: {:.2f}".format(score))

if __name__ == "__main__":
    main()
