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

print("\n")
print(df)
print("\n")
print(df > 0)
print("\n")
print(df[df > 0])
print("\n")
print(df[df['W']>0])
print("\n")
print(df[df['W']>0]['Y'])
print("\n")
print(df[df['W']>0][['Y','X']])
print("\n")
print(df[(df['W']>0) & (df['Y'] > 0)])

print("\n")
print(df)
print("\n")
print(df.reset_index())
print("\n")

newind = 'CA NY WY CO'.split()

df['States'] = newind


print(df)
print("\n")
df.set_index('States', inplace=True)

print(df)
print("\n")
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(np.random.randn(6,2),
                   index=hier_index,
                   columns=['A','B'])
print(df)

print("\n")
print(df.loc['G1'])
print("\n")
print(df.loc['G1'].loc[1])
print("\n")
df.index.names = ['Group','Num']
print(df)
print("\n")
print(df.xs('G1'))
print("\n")
print(df.xs(['G1',1]))
print("\n")
print(df.xs(1,level='Num'))

print("\n\nMISSING DATA")

df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})

print("\n")
print(df)

print("\n")
print(df.dropna())

print("\n")
print(df.dropna(axis=1))

print("\n")
print(df.dropna(thresh=2))

print("\n")
print(df.fillna(value='FILL VALUE'))

print("\n")
print(df['A'].fillna(value=df['A'].mean()))

print("\n")
print("GROUP BY")

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

print("\n")
print(df)
print("\n")
print(df.groupby("Company").mean())
print("\n")
print(df.groupby("Company").min())
print("\n")
print(df.groupby("Company").count())
print("\n")
print(df.groupby("Company").describe())
print("\n")
print(df.groupby("Company").describe().transpose())
print("\n")
print(df.groupby("Company").describe().transpose()["GOOG"])

print("\n")
print("Merging, Joining, and Concatenating")

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

print("\n")
print(df1)
print("\n")
print(df2)
print("\n")
print(df3)
print("\n")
print(pd.concat([df1,df2,df3]))