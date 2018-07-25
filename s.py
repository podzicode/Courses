import numpy as np
import pandas as pd
from numpy.random import randn
my_data=[10,20,30]
series=['USA','JAPAN','CANADA']
my_data2=[30,40,100]
series2=['USA','INDIA','JAPAN']
arr2=np.array(my_data2)
arr= np.array(my_data)
s1=pd.Series(my_data,series)
s2=pd.Series(my_data2,series2)
print(s1)
print(s2)
print(s1+s2)
np.random.seed(101)
df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
print(df.loc['A']);
df['new']=df['W']+df['X']
print(df['new'])
print(df.iloc[0,1])
booldf=df>0
print(df[booldf])
newind='CA OR DN MI IL'
newind=newind.split()
df['Series']=newind
print(df)
df.set_index('Series')
print(df)