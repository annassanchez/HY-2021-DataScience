#!/usr/bin/env python3

import math

def triangle():
    base = int(input("Give base of the triangle: "))
    height = int(input("Give height of the triangle: "))
    area = base * height / 2
    print(f"The area is {area:.6f}")
def rectangle():
    base = int(input("Give base of the rectangle: "))
    height = int(input("Give height of the rectangle: "))
    area = base * height
    print(f"The area is {area:.6f}") 
def circle():
    r = int(input("Give radius of the circle: "))
    area = math.pi * (r * r)
    print(f"The area is {area:.6f}")

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if (shape=="triangle"):
            triangle()
        elif (shape=="rectangle"):
            rectangle()
        elif (shape=="circle"):
            circle()
        elif (shape==""):
            break
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
