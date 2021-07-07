#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    tulos = []
    with open(filename, "r") as f:
        next(f) # skipataan eka turha rivi
        for x in range(754):
            try:
                string = f.readline()
                mo = re.search(r'(\d+)\s+(\d+)\s+(\d+)\s+(.*)', string)
                teksti = mo.group(0)
                osien_lista = teksti.split(sep=None)
                if len(osien_lista) > 4:
                    osien_lista[3] = osien_lista[3] + " " + osien_lista[4]
                tulosstring = ("\t".join(osien_lista[0:3]))
                tulosstring = tulosstring + "\t" + osien_lista[3]
                tulos.append(tulosstring)
            except Exception as err:
                    pass
    return tulos


def main():
    pass

if __name__ == "__main__":
    main()
