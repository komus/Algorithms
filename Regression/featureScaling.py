from typing import List
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn import linear_model
import matplotlib


def normalization(feature:List) -> List:
    rescaled = []
    min_feature = min(feature)
    max_feature = max(feature)
    for item in feature:
        try:
            r = (item - min_feature)/float(max_feature - min_feature)
            rescaled.append(r)
        except ZeroDivisionError as e:
            print(e)
    return rescaled
    

def normalization_sklearn(feature:np.ndarray) -> np.ndarray:
    """
        Ensures input is a numpy array and returns scaled numpy array
        Converts int value to float value. 
        Raises error when feature not in acceptable format
    """
    accepted = ["int32", "uint32","int8", "float64"]
    if feature.dtype in accepted:
        if feature.dtype != "float64":
            feature.astype(np.float64)
    else:
        raise ValueError("Array not in acceptable format")
    try:
        rescale = MinMaxScaler().fit_transform(feature)
        return rescale
    except ValueError as e:
        print(e) 



