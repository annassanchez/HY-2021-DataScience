#!/usr/bin/python3

import numpy as np

def meeting_lines(a_1,b_1,a_2,b_2):
    a = np.array([[float(a_1), -1.0], [float(a_2), -1.0]])
    b = np.array([-float(b_1),-float(b_2)])
    point = np.linalg.solve(a, b)
    return point

def main():
    a1=1
    b1=4
    a2=3
    b2=2

    x, y  = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")

if __name__ == "__main__":
    main()
