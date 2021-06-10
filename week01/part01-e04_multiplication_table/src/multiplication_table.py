#!/usr/bin/env python3


def main():
    pass
    for i in [1,2,3,4,5,6,7,8,9,10]:
        for s in [1,2,3,4,5,6,7,8,9,10]:
            print('{:4d}'.format(i*s), end=' ')
        print(end='\n')

if __name__ == "__main__":
    main()
