import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing seaborn will affect the look of the diagram.
import seaborn as sns

df1 = pd.read_csv("data1.csv", index_col=0)
df2 = pd.read_csv("data2.csv")
df3 = pd.read_csv("data3.csv", index_col=0)

# df1["A"].hist(bins=30)
# df1["A"].plot(kind="hist",bins=30)
# df1["A"].plot.hist()


# df2.plot.area()
# df2.plot.area(alpha=0.4)

# df2.plot.bar()
# df2.plot.bar(stacked=True)




plt.show()
