from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import matplotlib
from time import time

"""In simple terms, a Naive Bayes classifier assumes that the presence 
of a particular feature in a class is unrelated to the presence of any other feature."""
def classify(train_features, train_label, test_features, test_labels):
        classifier = GaussianNB()
        tfit = time()
        fit = classifier.fit(train_features, train_label)
        tfittime = round(time()-tfit, 3)
        tpred = time()
        pred = classifier.predict(test_features)
        tpredtime = round(time()-tpred, 3)
        accuracy = accuracy_score(pred, test_labels)
        return fit, pred, accuracy, tfittime, tpredtime


def MakeScatterplot():
        pass


