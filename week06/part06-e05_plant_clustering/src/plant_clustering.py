#!/usr/bin/env python3

from sklearn.datasets import load_iris

from sklearn import metrics

import scipy
import numpy as np
from sklearn.cluster import KMeans


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    #1_load dataset
    X, y = load_iris(return_X_y = True)
    #3_fit training daata with Gaussian NB
    model = KMeans(3, random_state=0)
    model.fit(X)
    #4_fix y with permutation
    permutation = find_permutation(3, y, model.labels_)
    #5_obtain new labels
    new_labels = [ permutation[label] for label in model.labels_]   # permute the labels
    #6_calculate accuracy
    accuracy = metrics.accuracy_score(y, new_labels)
    return accuracy

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
