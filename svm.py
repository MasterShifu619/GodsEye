import pickle
import pandas as pd

dataset = 'model_jairaj_home.csv'

data = pd.read_csv(dataset)
print (data.head())


from sklearn.model_selection import train_test_split

y = data.Class #labels
X = data.drop(['Class','Color','Name'], axis=1)
print(y)
print(X)

from sklearn import svm

clf=svm.SVC()
clf.fit(X, y)
filename="model_jairaj_home.sav"
pickle.dump(clf, open(filename, 'wb'))


