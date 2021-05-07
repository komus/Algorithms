"""
Using Naives Bayes classifier to classify emails
"""

import sys
from time import time
from email_preprocess import preprocess
sys.path.append("../")
from NaivesBayes import classify


def processemail():
    features_train, features_test,labels_train, labels_test = preprocess()
    fit, pred, accuracy, fit_time, pred_time = classify(features_train,labels_train,features_test, labels_test)
    print(f"Accuracy is {accuracy} \n Training time: {fit_time}\n Prediction time: {pred_time}")
    


processemail()