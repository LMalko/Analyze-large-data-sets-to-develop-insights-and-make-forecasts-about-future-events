#Least squares method

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




# 1. Predict housing prices based on existing features.

df = pd.read_csv("USA_Housing.csv")

print(df.info())
print(df.columns)


# df1 = df.describe()
# df1.to_excel("MyOutput1.xlsx")
#
# sns_plot = sns.pairplot(df,aspect=0.6, size=4)
# plt.tight_layout()
# sns_plot.savefig("pairplot1.png")

# plt.close()
#
# sns.distplot(df["Price"], bins=50, color="green",
#              hist_kws={"rwidth":0.75,'edgecolor':'red', 'alpha':1.0})
# plt.show()
#
# sns.heatmap(df.corr(), annot=True)
# plt.show()



# Grab column names - features.
X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
        'Avg. Area Number of Bedrooms', 'Area Population']]

# Target variable - in this case --> price column
y = df["Price"]



# Make a model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=101)


lr = LinearRegression()
lr.fit(X_train, y_train)

coefficient1 = lr.intercept_
coefficients_for_each_feature = lr.coef_

cdf = pd.DataFrame(coefficients_for_each_feature, X.columns,
             columns=["Coeff"])

print(cdf)

# Make predictions

predictions = lr.predict(X_test)

plt.scatter(y_test, predictions)

plt.show()

sns.distplot((y_test - predictions))

plt.show()