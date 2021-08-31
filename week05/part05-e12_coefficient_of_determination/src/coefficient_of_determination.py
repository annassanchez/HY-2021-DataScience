#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model
import numpy as np


def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    X = df.loc[:,"X1":"X5"]
    y = df.Y
 
    x1 = np.array(df.loc[:,"X1"]).reshape(-1,1)
    x2 = np.array(df.loc[:,"X2"]).reshape(-1,1)
    x3 = np.array(df.loc[:,"X3"]).reshape(-1,1)
    x4 = np.array(df.loc[:,"X4"]).reshape(-1,1)
    x5 = np.array(df.loc[:,"X5"]).reshape(-1,1)

    reg_all = linear_model.LinearRegression().fit(X, y)
    reg_x1 = linear_model.LinearRegression().fit(x1, y)
    reg_x2 = linear_model.LinearRegression().fit(x2, y)
    reg_x3 = linear_model.LinearRegression().fit(x3, y)
    reg_x4 = linear_model.LinearRegression().fit(x4, y)
    reg_x5 = linear_model.LinearRegression().fit(x5, y)

    r_all = reg_all.score(X,y)
    r_x1 = reg_x1.score(x1, y)
    r_x2 = reg_x2.score(x2, y)
    r_x3 = reg_x3.score(x3, y)
    r_x4 = reg_x4.score(x4, y)
    r_x5 = reg_x5.score(x5, y)
    return [r_all, r_x1, r_x2, r_x3, r_x4, r_x5]

 
    
def main():
    results = coefficient_of_determination()
    #print(f'R2-score with feature(s) X: {results[0]}')
    for index, item in enumerate(results[1:]):
        print(f'R2-score with feature(s) X{index}: {item}')

if __name__ == "__main__":
    main()
