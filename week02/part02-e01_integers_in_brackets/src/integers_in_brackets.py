#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    aux = []
    for l in re.findall(r'\[\s*[+-]?\b\d+\b\s*\]',s):
        for x in re.findall(r'[+-]?\b\d+\b',l):
            aux.append(int(x))
    return aux

def main():
    pass

if __name__ == "__main__":
    main()
