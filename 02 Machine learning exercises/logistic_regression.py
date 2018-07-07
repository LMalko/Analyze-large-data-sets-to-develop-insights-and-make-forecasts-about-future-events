import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import cufflinks as cf
import plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot


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



