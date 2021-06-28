#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    L = []
    with open(filename, "r") as f:
        for x in range(47):
            tmp = []
            line = f.readline()
            element = re.search(r'.{30}\s+(\d+)\s(\S+)\s(..)\s(\d+):(\d+)\s(.*)', line)
            for i in range(1, 7):
                #print(mo.group(i))
                try:
                    tmp.append(int(element.group(i)))
                except ValueError:
                    tmp.append(element.group(i))
                tupl = tuple(tmp)
            L.append(tupl)
    return L

def main():
    pass

if __name__ == "__main__":
    main()
