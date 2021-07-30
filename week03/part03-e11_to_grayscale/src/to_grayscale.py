#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    gray = np.dot(image[...,:3], [0.2126, 0.7152, 0.0722])
    return gray

def to_red(img):
    image = img.copy()
    image[:, :, 1] = 0   # green
    image[:, :, 2] = 0  # blue
    #plt.imshow(image)
    return image

def to_green(img):
    image = img.copy()
    image[:, :, 0] = 0    # red
    image[:, :, 2] = 0    # blue
    #plt.imshow(image)
    return image

def to_blue(img):
    image = img.copy()
    image[:, :, 0] = 0    # red
    image[:, :, 1] = 0    # green
    return image

def main():
    painting=plt.imread("src/painting.png")

    plt.imshow(to_grayscale(painting), cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    plt.show()
    to_grayscale(painting)

    fig, ax = plt.subplots(3,1)
    ax[0].imshow(to_red(painting))
    ax[1].imshow(to_green(painting)) 
    ax[2].imshow(to_blue(painting))
    plt.show()

if __name__ == "__main__":
    main()
