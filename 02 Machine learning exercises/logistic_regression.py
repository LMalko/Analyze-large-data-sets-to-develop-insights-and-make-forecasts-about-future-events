import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import cufflinks as cf
import plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


train = pd.read_csv("titanic_train.csv")

# Check for missing data
# print(train.isnull())
# Missing some of the age info
# Missing a lot of the cabin info

sns.heatmap(train.isnull(), yticklabels=False,
            cbar=False, cmap='viridis')

plt.show()

sns.set_style('whitegrid')
sns.countplot(x='Survived', data=train)
plt.show()

sns.countplot(x='Survived', data=train, hue='Sex')
plt.show()


sns.countplot(x='Survived', data=train, hue='Pclass')
plt.show()

sns.distplot(train['Age'].dropna(), kde=False, bins=30, color="green",
             hist_kws={"rwidth": 0.75, 'edgecolor': 'red', 'alpha': 1.0})
plt.show()
# or
train['Age'].plot.hist(bins=30)
plt.show()

# Check for children, spouse.
sns.countplot(x='SibSp', data=train)
plt.show()


sns.distplot(train['Fare'].dropna(), kde=False, bins=30, color="green",
             hist_kws={"rwidth": 0.75, 'edgecolor': 'red', 'alpha': 1.0})
plt.show()

fig = train['Fare'].iplot(kind="hist", asFigure=True, bins=50)
py.offline.plot(fig)



# Cleaning the data

# Imputation. Fill in missing age with avg age by passenger class
sns.boxplot(x='Pclass', y='Age', data=train)
plt.show()

def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        return 24

    else:
        return Age

train['Age'] = train[['Age', 'Pclass']].apply(impute_age,
                                              axis=1)

sns.heatmap(train.isnull(), yticklabels=False,
            cbar=False, cmap='viridis')

plt.show()

# Cabin has to many missing values, it's better to drop it.

train.dropna(inplace=True)

sns.heatmap(train.isnull(), yticklabels=False,
            cbar=False, cmap='viridis')

plt.show()






# Categorical features - Creating a dummy variable
# using multi-collinearity

sex = pd.get_dummies(train['Sex'], drop_first=True)

embark = pd.get_dummies(train['Embarked'], drop_first=True)

train = pd.concat([train, sex, embark], axis=1)


# Delete unnecessary columns

train.drop(['PassengerId', 'Sex', 'Embarked', 'Name', 'Ticket', 'Cabin'],
           axis=1, inplace=True)




X = train.drop("Survived", axis=1)
y = train['Survived']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=101)

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)

predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report

print(classification_report(y_test, predictions))

from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, predictions))






