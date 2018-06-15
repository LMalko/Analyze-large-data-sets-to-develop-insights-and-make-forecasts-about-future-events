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
print("\n")