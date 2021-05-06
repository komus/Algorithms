from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import matplotlib

"""In simple terms, a Naive Bayes classifier assumes that the presence 
of a particular feature in a class is unrelated to the presence of any other feature."""
class GaussianNBClassifier:
    """
    test = 10% data
    
    """
    def classify(train_features, train_label, test_features, test_labels):
        classifier = GaussianNB()
        fit = classifier.fit(train_features, train_label)
        pred = classifier.predict(test_features)
        accuracy = accuracy_score(pred, test_labels)
        return fit, pred, accuracy





class MakeImage:
    def prettyimage():
        pass
