import pickle
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import numpy as np
dataset = 'trained_vectors.csv'

data = pd.read_csv(dataset)
print (data.head())


from sklearn.model_selection import train_test_split

y = data.Class #labels
X = data.drop(['Class','Color','Name'], axis=1)
print(y)
print(X)



# Split dataset into training set and test set
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)
# print("This is the X_test")
#print(X_train,y_train)

from sklearn.ensemble import RandomForestClassifier
# #DON'T RUN AGAIN YOU HAVE 78% ACCURATE MODEL
#
# #Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X, y)
filename="rfc_model.sav"
pickle.dump(clf, open(filename, 'wb'))
# #Train the model using the training sets
# y_pred=clf.predict(X_test)
# clf.fit(X_train,y_train)
# rfc_cv_score = cross_val_score(clf, X, y, cv=10, scoring='roc_auc')
# #X_test=np.array[51.22,51.22,129.24,74.95,190.16,119.2,155.33,288.33,219.67,229.99]
# print(X_test.shape)
# y_pred=clf.predict(X_test)
# x_pred=clf.score(X,y,sample_weight=None)
# print(x_pred)
# #DON'T RUN AGAIN YOU HAVE 78% ACCURATE MODEL
#
# print("=== Confusion Matrix ===")
# print(confusion_matrix(y_test, y_pred))
# print('\n')
# print("=== Classification Report ===")
# print(classification_report(y_test, y_pred))
# print('\n')
# print("=== All AUC Scores ===")
# print(rfc_cv_score)
# print('\n')
# print("=== Mean AUC Score ===")
# print("Mean AUC Score - Random Forest: ", rfc_cv_score.mean())
# print(X_test.size)

# from sklearn import metrics
# # Model Accuracy, how often is the classifier correct?
# print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
# dtc = DecisionTreeClassifier().fit(X, y)
# plot_tree(dtc, filled=True)
# plt.show()

