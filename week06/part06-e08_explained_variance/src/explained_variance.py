#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.decomposition import PCA

#Write function explained_variance which reads the tab separated file “data.tsv”.
#The data contains 10 features.
#Then fit PCA to the data.
#The function should return two lists (or 1D arrays).
#The first list should contain the variances of all the features.
#The second list should consist of the explained variances returned by the PCA.

def explained_variance():
    data = pd.read_csv("src/data.tsv", header = 0, sep = "\t")
    pca = PCA(10)
    pca.fit(data)
    pcavarianssi = pca.explained_variance_
    datavarianssi = []
    for i in data:
        rivivarianssi = data[i].var()
        datavarianssi.append(rivivarianssi)
    return np.array(datavarianssi), pcavarianssi

def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))
    print(f"The variances are: {v[0]:.3f} {v[1]:.3f} {v[2]:.3f} {v[3]:.3f} {v[4]:.3f} {v[5]:.3f} {v[6]:.3f} {v[7]:.3f} {v[8]:.3f} {v[9]:.3f}")
    print(f"The explained variances after PCA are: {ev[0]:.3f} {ev[1]:.3f} {ev[2]:.3f} {ev[3]:.3f} {ev[4]:.3f} {ev[5]:.3f} {ev[6]:.3f} {ev[7]:.3f} {ev[8]:.3f} {ev[9]:.3f}")
    x = np.arange(1,len(ev) + 1)
    plt.plot(x,np.cumsum(ev))
    plt.show()

if __name__ == "__main__":
    main()
