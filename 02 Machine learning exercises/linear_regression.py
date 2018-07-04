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

# Interpreting the coefficients:
#
# Holding all other features fixed, a 1 unit increase in Avg. Area Income is associated with an increase of $21.52 .
# Holding all other features fixed, a 1 unit increase in Avg. Area House Age is associated with an increase of $164883.28 .
# Holding all other features fixed, a 1 unit increase in Avg. Area Number of Rooms is associated with an increase of $122368.67 .
# Holding all other features fixed, a 1 unit increase in Avg. Area Number of Bedrooms is associated with an increase of $2233.80 .
# Holding all other features fixed, a 1 unit increase in Area Population is associated with an increase of $15.15 .
# Does this make sense? Probably not because I made up this data.

# Make predictions

predictions = lr.predict(X_test)

plt.scatter(y_test, predictions)

plt.show()

sns.distplot((y_test - predictions))

plt.show()



# Metrics


from sklearn import metrics

# MAE is the easiest to understand, because it's the average error.
# MSE is more popular than MAE, because MSE "punishes" larger errors, which tends to be useful in the real world.
# RMSE is even more popular than MSE, because RMSE is interpretable in the "y" units.

print("MAE: ", metrics.mean_absolute_error(y_test, predictions))
print("MSE: ", metrics.mean_squared_error(y_test, predictions))
print("RMSE: ", np.sqrt(metrics.mean_squared_error(y_test, predictions)))