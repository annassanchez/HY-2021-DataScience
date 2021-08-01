#!/usr/bin/env python3

import pandas as pd

def cities():  
    indices = ['Helsinki', 'Espoo', 'Tampere', 'Vantaa', 'Oulu']  
    population = [643272, 279044, 231853, 223027, 201810]
    total_area = [715.48, 528.03, 689.59, 240.35, 3817.52]
    s_population = pd.Series(population, index = indices)
    s_total_area = pd.Series(total_area, index = indices)
    df = pd.DataFrame({"Population" : s_population, "Total area" : s_total_area})
    return df
    
def main():
    return
    
if __name__ == "__main__":
    main()
