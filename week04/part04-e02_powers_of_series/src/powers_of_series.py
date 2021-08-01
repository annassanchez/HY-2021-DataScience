#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    df_power = pd.DataFrame()
    for i in range(1,k+1):
        s_ = pd.Series((s.values) ** i, name = i)
        if i==1:
            df_power = pd.DataFrame(s_)
        if i != 1:
            df_power[i] = s_
    return df_power
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))
    
if __name__ == "__main__":
    main()
