#!/usr/bin/env python3

import sys

def file_count(filename):
    words_ = []
    words = []
    char = 0
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            words_ += line.split()
            words += line
        for word in words:
            char += len(word)
    return (len(lines), len(words_), char)

def main():
    #print(sys.argv[1:])
    for filename in sys.argv[1:]:
        lines, words, characters= file_count(filename)
        print(f'{lines}\t{words}\t{characters}\t{filename}')

if __name__ == "__main__":
    main()
