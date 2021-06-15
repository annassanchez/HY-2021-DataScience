#!/usr/bin/env python3
import numpy as np
def detect_ranges(L):
    L = sorted(L)
    sequences =  np.split(L, np.array(np.where(np.diff(L) > 1)[0]) + 1)
    M = []
    for s in sequences:
        if len(s)>1:
            M.append((np.min(s),np.max(s)+1))
        else:
            M.append(s[0])
    return M

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
