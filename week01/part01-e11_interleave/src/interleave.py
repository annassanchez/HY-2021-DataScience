#!/usr/bin/env python3

def interleave(*lists):
    li = []
    for x in zip(*lists):
        li.extend([*x])
    return li

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))


if __name__ == "__main__":
    main()
