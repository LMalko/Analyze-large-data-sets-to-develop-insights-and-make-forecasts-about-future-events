import numpy as np
import pandas as pd

df1 = pd.read_csv("data1.csv", index_col=0)
df2 = pd.read_csv("data2.csv", index_col=0)
df3 = pd.read_csv("data3.csv", index_col=0)

print(df1["A"].hist())