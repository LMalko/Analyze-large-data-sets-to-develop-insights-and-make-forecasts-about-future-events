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

sns.jointplot(x='total_bill',y='sex',data=tips)

plt.show()


