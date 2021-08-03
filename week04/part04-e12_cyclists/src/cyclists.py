#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep = ';')
    df_rows = df.dropna(how='all', axis = 0)
    df_columns = df_rows.dropna(how = 'all', axis = 1)
    return df_columns


def main():
    return
    
if __name__ == "__main__":
    main()
