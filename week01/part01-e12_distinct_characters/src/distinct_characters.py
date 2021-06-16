#!/usr/bin/env python3

def distinct_characters(L):
    new_dict = {}
    for i, value in enumerate(L):
        length = len(set(value))
        new_dict[value] = length
        i +=1
    return new_dict

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
