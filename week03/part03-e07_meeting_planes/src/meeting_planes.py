#!/usr/bin/python3

import numpy as np

def meeting_planes(a_1, b_1, c_1, a_2, b_2, c_2, a_3, b_3, c_3):
    a = np.array([[float(b_1), float(a_1), -1.0], [float(b_2), float(a_2), -1.0] , [float(b_3), float(a_3), -1.0]])
    b = np.array([-float(c_1), -float(c_2), -float(c_3)])
    point = np.linalg.solve(a, b)
    return point

def main():
    a1=1
    b1=4
    c1=5
    a2=3
    b2=2
    c2=1
    a3=2
    b3=4
    c3=1

    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"Planes meet at x={x}, y={y} and z={z}")

if __name__ == "__main__":
    main()
