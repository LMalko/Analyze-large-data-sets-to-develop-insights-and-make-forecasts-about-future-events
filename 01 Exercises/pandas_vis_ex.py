import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing seaborn will affect the look of the diagram.
import seaborn as sns

df1 = pd.read_csv("data1.csv", index_col=0)
df2 = pd.read_csv("data2.csv")
df3 = pd.read_csv("data3.csv", index_col=0)

# df1["A"].hist(bins=30)
df1["A"].plot(kind="hist",bins=30)
# df1["A"].plot.hist()
plt.close()

# df2.plot.area()
# df2.plot.area(alpha=0.4)

# df2.plot.bar()
df2.plot.bar(stacked=True)
plt.close()

# df1.plot.line(y="B")
df1.plot.line(y="B", figsize=(12, 3))
# df1.plot.line(y="B", figsize=(12, 3), linewidth=1)
plt.close()
df1.plot.scatter(x="A", y="B", c="C", cmap="coolwarm")

# Boundaries need to be called AFTER plot.scatter.
# plt.xlim(-0.2, 1.2)
# plt.ylim(-0.2, 1.2)

# df1.plot.scatter(x="A", y="B", s=df1["C"] * 100)

df2.plot.box()
plt.close()
df = pd.DataFrame(np.random.randn(1000, 2),
                  columns=["a", "b"])
plt.close()
# df.plot.hexbin(x="a", y="b")
# df.plot.hexbin(x="a", y="b", gridsize=25)
# df.plot.hexbin(x="a", y="b", gridsize=25,
#                cmap="coolwarm")


df2["a"].plot.kde()
plt.close()
df2["a"].plot.density()
plt.close()
df2.plot.density()

plt.show()
