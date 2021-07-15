#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, char):
        self.start = char
    #create the write function
    def write(self, s):
        return print(self.start + s)

def main():
    pass

if __name__ == "__main__":
    main()
