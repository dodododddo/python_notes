import pandas as pd

df = pd.read_csv('/home/jr/python_notes/homework/ch9-11/msg.csv')
print(df)
df = df.drop(columns=['Name'])
df = df.dropna(axis=0, how='all')
df_dummy = pd.get_dummies(df, dummy_na=True)
df_filled = df_dummy.fillna(df_dummy.mean())
df_filled.to_csv('/home/jr/python_notes/homework/ch9-11/msg_filled.csv')

data = df_filled.to_numpy()
print('\n',df_filled)
print('\n', data)