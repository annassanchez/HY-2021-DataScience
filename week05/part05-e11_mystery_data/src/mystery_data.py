#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def mystery_data():
  #url = 'https://raw.githubusercontent.com/annassanchez/HY-2021-DataScience/main/week05/mystery_data.tsv'
  #data = pd.read_csv(url, sep = '\t')
  data = pd.read_csv('src/mystery_data.tsv', sep = '\t')
  model_linear = LinearRegression(fit_intercept=False)
  X = data[['X1', 'X2', 'X3', 'X4', 'X5']]#.values.reshape(5000,1)
  y = data['Y']#.values.reshape(1000,1)
  model_linear.fit(np.vstack([X]), y)
  return model_linear.coef_

def main():
    coefficients = mystery_data()
    print("Coefficient of X1 is: ", coefficients[0][0])
    print("Coefficient of X2 is: ", coefficients[0][1])
    print("Coefficient of X3 is: ", coefficients[0][2])
    print("Coefficient of X4 is: ", coefficients[0][3])
    print("Coefficient of X5 is: ", coefficients[0][4])
    # print the coefficients here
    
if __name__ == "__main__":
    main()
