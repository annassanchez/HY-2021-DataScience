#!/usr/bin/env python3
import pandas as pd

def read_series():
    values = []    
    indices = []  
    while True:
        value = input("Enter index and value: ")        
        if value != "":
            parts = value.split()
            if len(parts) == 2:
                indices.append(parts[0])
                values.append(parts[1])
            elif len(parts) != 2:
                try:
                    values.append(parts[1])
                    indices.append(parts[0])
                except Exception as error:
                    print("Input line is malformed")
        elif value == "":
            break
    s = pd.Series(values,index=indices)
    #print(s.index)
    #print(s.values)
    return s

def main():
    print(read_series())

if __name__ == "__main__":
    main()
