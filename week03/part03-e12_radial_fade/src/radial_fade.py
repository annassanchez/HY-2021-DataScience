#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

a= np.random.randint(0, 5, size=(3, 3))

def center(a):
    painting=a.copy()
    #print(painting.shape)
    y=(painting.shape[1]-1)/2
    x=(painting.shape[0]-1)/2
    return (x,y) 

def radial_distance(a):
    c = center(a)
    dist = np.zeros((a.shape[0],a.shape[1]))
    for h in range(dist.shape[0]):
        for w in range(dist.shape[1]):
            dist[h, w] = np.sqrt(np.sum((np.array([h, w])-c)**2))
    return dist

def scale(a, tmin=0.0, tmax=1.0):
    if a.min()==a.max():
        return a*0 
    else:
        return ((a-a.min())/(a.max()-a.min()))

def radial_mask(a):
	img2 = a.copy()
	a_dist = radial_distance(img2)
	a_scaled = scale(a_dist)
	mask = 1-a_scaled
	return mask

def radial_fade(a):
    img2 = a.copy()
    m=radial_mask(img2).reshape(img2.shape[0],img2.shape[1],1)
    r=img2*m
    return r

def main():
    painting=plt.imread("src/painting.png")
    img = painting.copy()
    e = radial_mask(img)
    print(e.min())
    fig, ax = plt.subplots(3,1)
    ax[0].imshow(painting)
    ax[1].imshow(radial_mask(img))
    ax[2].imshow(radial_fade(img))
    plt.show()

if __name__ == "__main__":
    main()
