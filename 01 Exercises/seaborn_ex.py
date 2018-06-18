import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

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
# plt.show()
plt.close()

# KDE = sum of all normal distributions around the plot.

# Drops dashmark for every single value.
sns.rugplot(tips["total_bill"])
plt.show()




