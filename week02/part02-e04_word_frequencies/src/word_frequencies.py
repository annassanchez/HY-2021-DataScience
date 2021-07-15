#!/usr/bin/env python3
import re

def word_frequencies(filename):
    # Creating empty result and final lists.
    result = []
    final = []
    d = {}
    # Reading the file.
    with open(filename, "r") as f:
        # Splitting the lines into words.
        for line in f:
            for word in line.split():
                wordtemp = word.strip("""!"#$%&'()*,-./:;?@[]_""")#.lower()
                result.append(wordtemp)
        # Puts words and their count into dict.
        for word in result:
            if word not in final:
                final.append(word)
        for x in final:
            d[x] = result.count(x)
    return d

def main():
    pass

if __name__ == "__main__":
    main()
