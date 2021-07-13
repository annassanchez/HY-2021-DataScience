#!/usr/bin/env python3

def file_extensions(filename):
    l = []
    d = {}
    with open(filename, "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if "." in line:
            two = line.rsplit(".", 1)
            end = two[1]
            if end in d:
                d[end].append(line)
            else:
                d[end]=[line]
        else:
            l.append(line)
    return (l,d)

def main():
    l, d = file_extensions("src/filenames.txt")
    print(f"{len(l)} files with no extension")
    for k, v in sorted(d.items()):
        print(f"{k} {len(v)}")

if __name__ == "__main__":
    main()
