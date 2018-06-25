import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("911_data.csv")

# 1. Check info of the file.

print(df.info())