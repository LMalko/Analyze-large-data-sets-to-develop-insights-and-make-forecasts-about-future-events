import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. DISTRIBUTION PLOTS.

tips = pd.read_csv('tips.csv')

sns.distplot(tips['total_bill'])
# No line
# sns.distplot(tips['total_bill'], kde=False)

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

sns.pairplot(tips, hue="sex")
plt.show()




