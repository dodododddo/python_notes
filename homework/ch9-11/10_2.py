import pandas as pd

data = [1, 2, 3, 4, 5]
df = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print(df)