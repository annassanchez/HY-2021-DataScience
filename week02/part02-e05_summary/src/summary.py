#!/usr/bin/env python3

import sys
import statistics

def summary(filename):
    L=[]
    #reading the file
    with open(filename, "r") as f:
        L = []
        for line in f:
            try:
                n = float(line)
                L.append(n)
            except:
                pass
        Sum = sum(L)
        Average = statistics.mean(L)
        Stddev = statistics.stdev(L)
    return (Sum,Average,Stddev)

def main():
    #print(sys.argv[1:])
    for filename in sys.argv[1:]:
        Sum,Average,Stddev = summary(filename)
        print(f'File: {filename} Sum: {Sum:.6f} Average: {Average:.6f} Stddev: {Stddev:.6f}')

if __name__ == "__main__":
    main()
