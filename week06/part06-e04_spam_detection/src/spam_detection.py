#!/usr/bin/env python3
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics
import gzip

def spam_detection(random_state=0, fraction=0.1):
    viluspam ="src/spam.txt.gz"
    viluham = "src/ham.txt.gz"

    with gzip.open(viluspam,'r') as fspam:
        #arspam = np.array(fspam)
        arspam = np.array(fspam.readlines())
    lspam = int(fraction*len(arspam))
#    arspam = np.array(list(arspam[0:lspam]))
    with gzip.open(viluham,'r') as fham:
        #arham = np.array(fham)
        arham = np.array(fham.readlines())
    lham = int(fraction * len(arham))
    X = np.concatenate([arham[0:lham],arspam[0:lspam]])
#    print(X.shape)
    hy = [0]*lham
    sy = [1]*lspam
    y = np.array([hy+sy]).T
    model =MultinomialNB()
    cv = CountVectorizer()
    Xfeats = cv.fit_transform(X)
#    print(Xfeats[0,:])
    ts = 0.75 # train size
    Xtrain, Xtest, ytrain, ytest = train_test_split(Xfeats, y, random_state=random_state, train_size = ts)

    model.fit(Xtrain, ytrain)

    fitted = model.predict(Xtest)

    acc = accuracy_score(ytest, fitted)
#    print(cv.vocabulary_)
#    print(cv.get_feature_names())

    toinen = int((1-ts)*(lham+lspam))

    return acc, toinen, int((1-acc)*toinen)

 

#    return 0.0, 0, 0

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
