#!/usr/bin/env python3

import matplotlib.pyplot as plt

def main():
    x_1 = [2,4,6,7]
    y_1 = [4,3,5,1]
    x_2 = [1,2,3,4]
    y_2 = [4,2,3,1]
    plt.plot(x_1, y_1, x_2, y_2)
    plt.title("Combinated graphs")
    plt.xlabel("x-axis")       
    plt.ylabel("y-axis")  
    plt.show()

if __name__ == "__main__":
    main()
