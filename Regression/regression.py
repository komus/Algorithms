import sys
import pickle
sys.path.append("../")
from feature_format import featureFormat, targetFeatureSplit
from sklearn import linear_model, model_selection
from sklearn.metrics import mean_squared_error, r2_score
dictionary = pickle.load( open("../data/final_project_dataset_modified.pkl", "rb") )

### list the features you want to look at--first item in the 
### list will be the "target" feature
features_list = ["bonus", "salary"]
data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit( data )


### training-testing split needed in regression, just like classification

feature_train, feature_test, target_train, target_test =  model_selection.train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"



### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and 
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.

reg = linear_model.LinearRegression()
reg.fit(feature_train, target_train)



print(f"coef:{reg.coef_}, intercept:{reg.intercept_}")
print(f"mean squared error: {mean_squared_error(feature_test, reg.predict(feature_test))}")
print('Coefficient of determination: %.2f'% r2_score(feature_test, reg.predict(feature_test)))

print(f"Regression score {reg.score(feature_test, target_test)}")
### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass
plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()