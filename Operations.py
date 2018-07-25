import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()
df2=(df['col2'].unique())
arr1=(df['col2'].value_counts())
print(arr1)
def add(x):
    return x+x;
df3=df['col2'].apply(add)
print(df3)
df3=df['col3'].apply(len)
print(df3)