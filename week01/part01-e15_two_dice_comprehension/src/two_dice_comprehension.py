#!/usr/bin/env python3

def main():
    pass
    L =  [ print('({:d}, {:d})'.format(a,b)) for a in range(1,6) for b in range (1,6) if a + b == 5 ]

if __name__ == "__main__":
    main()
