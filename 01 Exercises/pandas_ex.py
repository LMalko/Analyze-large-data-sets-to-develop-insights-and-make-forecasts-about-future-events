# Series

import numpy as np
import pandas as pd

labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}
print("\n")
print(pd.Series(data=my_list))
print("\n")
print(pd.Series(data=my_list,index=labels))
print("\n")
print(pd.Series(arr))
print("\n")
print(pd.Series(d))
print("\n")
print(pd.Series(data=labels))
print("\n")
ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])
print(ser1)
print("\n")
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])
print(ser2)
print("\n")
print(ser1['USA'])
print("\n")
print(ser1 + ser2)
print("\nDATAFRAMES\n")

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5, 4),
                  index='A B C D E'.split(),
                  columns='W X Y Z'.split())

print(ser1['USA'])
print(df)
print("\n")
print(df['W'])
print("\n")
print(df[['W','Z']])
print("\n")
df['new'] = df['W'] + df['Y']
print(df)
print("\n")
df.drop('new',axis=1, inplace=True)
print(df)
df.drop('E',axis=0, inplace=True)
print("\n")
print(df)
print("\n")
print(df.loc['A'])
print("\n")
print(df.iloc[2])
print("\n")
print(df.loc['B','Y'])
print("\n")
print(df.loc[['A','B'],['W','Y']])
print("\n")
print(df.loc[['A','B'],['W','Y']])
print("\nCONDITIONAL SELECTION")

