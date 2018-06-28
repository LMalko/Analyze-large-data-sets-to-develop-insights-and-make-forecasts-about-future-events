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

# frequency
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


df = pd.DataFrame(data=np.random.randn(1000, 2),
                  columns=["a", "b"])
df.plot.box()

# or df2[["a", "b"]].plot.box() is the same

plt.show()
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




#
# plt.close()
# plt.style.use('ggplot')
# df2['a'].plot.hist(color="red", alpha=0.4, bins=30)
# plt.xlim(0, 1)
# plt.ylim(-0, 35)
# plt.show()

# import numpy as np
# plt.style.use('ggplot')
# df2["a"].plot.density()
# plt.xticks(np.arange(-0.5, 1.7, step=0.5))
# plt.yticks(np.arange(0.0, 1.3, step=0.2))
#
# plt.show()


# df2.plot.area(alpha=0.4)
# plt.xlim(0, 30)
# plt.yticks(np.arange(0, 3, step=0.5))


# legend outside diagram

# f = plt.figure()
# df3.plot.area(alpha=0.4,ax=f.gca())
# plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
# plt.xlim(0, 30)
# plt.yticks(np.arange(0, 3.4, step=0.5))