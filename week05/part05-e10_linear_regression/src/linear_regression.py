#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model_linear=LinearRegression(fit_intercept=True)
    model_linear.fit(np.vstack([x]).T, y)
    #xf = x
    #yf_linear = model_linear.predict(np.vstack([x]).T)
    slope =  model_linear.coef_[0]
    intercept = model_linear.intercept_
    return slope, intercept
    
def main():
    x = np.linspace(-50,150,50)
    y = x    
    a, b = fit_line(x, y)
    print("Slope:", a)
    print("Intercept:", b)
    plt.scatter(x, y, color="black")
    model_linear=LinearRegression(fit_intercept=True)
    model_linear.fit(np.vstack([x]).T, y)
    xf = x
    yf = model_linear.predict(np.vstack([x]).T)
    plt.plot(xf,yf, label="linear")
    plt.show()

    
if __name__ == "__main__":
    main()
