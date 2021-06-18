#!/usr/bin/env python3

def reverse_dictionary(d):
    reverse = {}
    for key, value in d.items():
        #print(key)
        #print(value)
        for j in value:
            if j in reverse.keys():
                #reverse[j] = [reverse[j],key]
                reverse[j].append(key)
            else:
                reverse[j] = [key]
            #reverse[j] = [key]
    return reverse

def main():
    pass

if __name__ == "__main__":
    main()
