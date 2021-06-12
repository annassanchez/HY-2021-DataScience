#!/usr/bin/env python3
def triple(a):
    "computes the triple of a number"
    return a*3
def square(a):
    "computes the square of a number"
    return a**2
def main():
    pass
    for a in range(1,10):
        x = triple(a)
        y = square(a)
        if x < y:
            break
        print(f"triple({a})=={x:d} square({a})=={y:d}")
if __name__ == "__main__":
    main()

