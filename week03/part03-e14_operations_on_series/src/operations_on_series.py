#!/usr/bin/env python3
import pandas as pd

def create_series(a_list, b_list):
    s1 = pd.Series(a_list, index=["a", "b", "c"])
    s2 = pd.Series(b_list, index=["a", "b", "c"])
    return s1, s2
    
def modify_series(s1, s2):
    new_s1 = s1
    new_s1['d'] = s2.loc["b"]
    new_s2 = s2.drop(labels=["b"])
    kk = new_s1.__add__(new_s2)
    return new_s1, new_s2
    
def main():
    L1 = [1,2,3]
    L2 = [4,5,6]
    s1, s2 = create_series(L1, L2)
    modify_series(s1, s2)
    
if __name__ == "__main__":
    main()
