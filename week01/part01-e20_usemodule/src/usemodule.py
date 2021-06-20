#!/usr/bin/env python3

# Don't modify the below hack

try:
    from src import triangle
except ModuleNotFoundError:
    import triangle 

def main():
    # Call the functions from here
    h = triangle.hypothenuse(2,3)
    a = triangle.area(2,3)

if __name__ == "__main__":
    main()
