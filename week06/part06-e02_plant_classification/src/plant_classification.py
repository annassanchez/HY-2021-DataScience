#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():
    #1_load dataset
    X, y = load_iris(return_X_y = True)
    #2_split into testing and training
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=0)
    #3_fit training daata with Gaussian NB
    model = naive_bayes.GaussianNB()
    model.fit(X_train, y_train)
    #4_pedict labels
    labels_fitted = model.predict(X_test)
    #5_accuracy
    accuracy = metrics.accuracy_score(y_test, labels_fitted)
    return accuracy

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
