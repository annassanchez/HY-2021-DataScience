#!/usr/bin/env python3

def transform(s1, s2):
    l1s = s1.split()
    l1 = list(map(int, l1s))
    l2s = s2.split()
    l2 = list(map(int, l2s))
    l = list(zip(l1,l2))
    return [(int(x) * int(y)) for x, y in l]

def main():
    pass

if __name__ == "__main__":
    main()
