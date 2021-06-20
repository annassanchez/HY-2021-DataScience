#!/usr/bin/env python3

def sum_equation(L):
    if len(L) != 0:
        li = " + ".join([str(x) for x in L])
        li.strip()
        car = " = " + str(sum(L))
        result = li + car
        result = result.strip()
        return result
    else:
        return '0 = 0'

def main():
    pass

if __name__ == "__main__":
    main()
