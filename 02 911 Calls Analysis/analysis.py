import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("911_data.csv")

# 1. Check info of the file.

# print(df.info())


# 2. What are the top 6 zipcodes for 911 calls?

# print(df["zip"].value_counts().head(6))


# 3. How many unique title codes are there?

# print(df['title'].unique())
# print(df['title'].nunique())


# 4. Reason column with abbreviation value of Reasons/ Departments column.

# df["Reason"] = df["title"].apply(lambda title: title.split(":")[0])
#
# print(df["Reason"])

