import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import cufflinks as cf
import plotly as py

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, \
    confusion_matrix

from sklearn.ensemble import RandomForestClassifier




data = pd.read_csv("kyphosis.csv")

print(data.head())

sns.pairplot(data, hue="Kyphosis")

plt.show()


X = data.drop("Kyphosis", axis=1)
y = data["Kyphosis"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=101)

# single decision tree
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

predictions = dtree.predict(X_test)

print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))






rfc = RandomForestClassifier(n_estimators=200)




