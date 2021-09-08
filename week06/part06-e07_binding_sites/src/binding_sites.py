#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc
from scipy.stats import mode

def toint(x):
    base = ["A", "C", "G", "T"]
    idx = [0, 1, 2, 3]
    d = dict(zip(base, idx))
    return d[x]

def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep='\t')
    # apply the 'toint' function to each letter 'l' in string 'x' contained in column 'X'
    df["X"] = df["X"].apply(lambda x: [toint(l) for l in list(x)])
    X = np.array(df["X"])
    X = np.asarray([np.asarray(row, dtype=int) for row in X], dtype=int)
    y = np.array(df["y"])
    return (X,y) # (np.array(df["X"]), np.array(df["y"]))

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    X, y = get_features_and_labels(filename)
    X = np.asarray([np.asarray(row, dtype=int) for row in X], dtype=int)
    y = np.asarray([np.asarray(row, dtype=int) for row in y], dtype=int)
    model = AgglomerativeClustering(linkage="average", affinity="euclidean")
    model.fit(X)
    labels = model.labels_
    n_clusters_ = len(set(labels))
    p = find_permutation(n_clusters_, y, labels)
    new_labels = [p[label] for label in labels]
    acc_ = accuracy_score(y, new_labels)
    return acc_

def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
         # Choose the most common label among data points in the cluster
        new_label = mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def cluster_hamming(filename):
    X, y = get_features_and_labels(filename)
    X = np.asarray([np.asarray(row, dtype=int) for row in X], dtype=int)
    y = np.asarray([np.asarray(row, dtype=int) for row in y], dtype=int)
    hamming_dist = pairwise_distances(X, metric="hamming")
    # If “precomputed”, a distance matrix (instead of a similarity matrix) is needed as input for the fit method.
    model = AgglomerativeClustering(linkage="average", affinity="precomputed")
    model.fit(hamming_dist)
    labels = model.labels_
    n_clusters_ = len(set(labels))
    p = find_permutation(n_clusters_, y, labels)
    new_labels = [p[label] for label in labels]
    acc_ = accuracy_score(y, new_labels)
    return acc_

def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
