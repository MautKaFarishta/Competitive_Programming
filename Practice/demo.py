import pandas as pd

d = {'col1': [1, 2], 'col2': [3, 4]}
e = {'col1': [4, 2]}
f = {'col1': [8, 6], 'col2': [3, 4],'col3': [3, 4]}

df1 = pd.DataFrame(data=d)
df2 = pd.DataFrame(data=e)
df3 = pd.DataFrame(data=f)

print(df1+df2+df3)
