import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. DISTRIBUTION PLOTS.

tips = pd.read_csv('tips.csv')

sns.distplot(tips['total_bill'])
# No kde
# sns.distplot(tips['total_bill'], kde=False)
# Only kde
# sns.distplot(tips['total_bill'])

# plt.show()
plt.close()

sns.distplot(tips['total_bill'], kde=False, bins=40)
# plt.show()
plt.close()

sns.jointplot(x='total_bill',y='tip',data=tips, kind="hex")
# plt.show()
plt.close()

sns.jointplot(x='total_bill', y='tip', data=tips, kind="kde")
# plt.show()
plt.close()

sns.jointplot(x='total_bill', y='tip', data=tips, kind="reg")
# plt.show()
plt.close()

sns.jointplot(x='total_bill', y='tip', data=tips)
# plt.show()
plt.close()

sns.pairplot(tips)
# plt.show()
plt.close()

sns.pairplot(tips, hue="sex", palette="husl")
plt.show()
plt.close()

# KDE = sum of all normal distributions around the plot.

# Drops dashmark for every single value.
sns.rugplot(tips["total_bill"])
# plt.show()
plt.close()

# 2. CATEGORICAL PLOTS


sns.barplot(x="sex", y="total_bill", data=tips)

# plt.show()
plt.close()

sns.barplot(x="sex", y="total_bill",
            data=tips,
            estimator=np.min)

# plt.show()
plt.close()

sns.countplot(x="sex", data=tips)

# plt.show()
plt.close()

sns.boxplot(x="day", y="total_bill", data=tips)

# plt.show()
plt.close()

sns.boxplot(x="day", y="total_bill", data=tips,
            hue="smoker")

# plt.show()
plt.close()

sns.violinplot(x="day", y="total_bill",
               data=tips, hue="smoker")

# plt.show()
plt.close()

sns.violinplot(x="day", y="total_bill",
               data=tips, hue="smoker", split=True)

# plt.show()
plt.close()

sns.stripplot(x="day", y="total_bill",
               data=tips, hue="smoker", jitter=True)

# plt.show()
plt.close()

# violinplot + stripplot = swarmplot
sns.swarmplot(x="day", y="total_bill",
               data=tips, hue="smoker")

# plt.show()
plt.close()

# or violinplot on top of swarmplot

sns.violinplot(x="day", y="total_bill",
               data=tips, split=True)
sns.swarmplot(x="day", y="total_bill",
               data=tips, color="black")

# General function of all kinds of plots, chosen by keyword 'kind'.
# sns.factorplot(x="day", y="total_bill",
#                data=tips,kind="violin")


plt.show()

# 3. Matrix plots.








