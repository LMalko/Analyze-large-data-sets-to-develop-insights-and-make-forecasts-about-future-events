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
# Palettes:
# https://matplotlib.org/examples/color/colormaps_reference.html


# plt.show()
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


# plt.show()
plt.close()











# 3. Matrix plots.

flights = pd.read_csv("flights.csv")




# Order months
cats = ['January','February','March','April','May','June',
        'July','August','September','October','November',
        'December']
flights["month"] = flights["month"].astype('category',
                                  ordered=True,
                                  categories=cats)

# Convert to matrix form
tc = tips.corr()
sns.heatmap(tc)

# plt.show()
plt.close()

sns.heatmap(tc, annot=True, cmap="coolwarm")

# plt.show()
plt.close()

# Convert to matrix form
fp = flights.pivot_table(index="month", columns="year",
                    values="passengers")

sns.heatmap(fp, cmap="coolwarm", linecolor="white",
            linewidths=0.5)
# cmap="magma"

# plt.show()
plt.close()


sns.clustermap(fp)
# sns.clustermap(fp, cmap="coolwarm", standard_scale=1)

# plt.show()
plt.close()






# 4. GRIDS

iris = pd.read_csv("iris.csv")
grid = sns.PairGrid(iris)
#
# grid.map(plt.scatter)

grid.map_diag(sns.distplot)
grid.map_upper(plt.scatter)
grid.map_lower(sns.kdeplot)


# plt.show()
plt.close()


grid = sns.FacetGrid(data=tips, col="time", row="smoker")
#
# grid.map(sns.distplot, "total_bill")
grid.map(plt.scatter, "total_bill", "tip")

# plt.show()
plt.close()




# 5 REGRESSION PLOTS


sns.lmplot(x="total_bill", y="tip",
           data=tips, hue="sex",
           markers=["o", "v"],
           # Enlarge markes by calling matplotlib
           scatter_kws={"s": 100})

# plt.show()
plt.close()

sns.lmplot(x="total_bill", y="tip",
           data=tips,
           # 2 seperate columns
           col="day",
           # 2 seperate rows
           row="time",
           # Add another column
           hue="sex",
           aspect=0.6, size=8)

# plt.show()
plt.close()



# 6 STYLE AND COLOR

# Set diagram size
plt.figure(figsize=(9, 5))

# Set font size
# sns.set_context("poster", font_scale=3)
# sns.set_context("poster")

# sns.set_style("ticks")
sns.set_style("whitegrid")
sns.countplot(x="sex", data=tips)

# sns.despine(bottom=True, left=True)
# sns.despine()


# plt.show()
plt.close()

sns.lmplot(x="total_bill", y="tip",
           data=tips, hue="sex", palette="seismic")



plt.show()

