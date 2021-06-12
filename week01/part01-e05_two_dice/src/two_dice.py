#!/usr/bin/env python3

def main():
    pass
    for a in range(1,6):
        for b in range(1,6):
            if a + b == 5:
                print('({:d},{:d})'.format(a,b))
            else:
                continue

if __name__ == "__main__":
    main()
