import pandas as pd

df = pd.read_csv('data/csv/ZILLOW-C12385_MLP4B.csv')
print(df.head())
df.set_index('Date', inplace=True)
df.to_csv('data/csv/newcsv.csv')

df = pd.read_csv('data/csv/newcsv.csv')
print(df.head())

df = pd.read_csv('data/csv/newcsv.csv', index_col=0)
print(df.head())

df.columns = ['South Holland,IL HPI']
print(df.head())

df.to_csv('data/csv/newcsv2.csv')
df.to_csv('data/csv/newcsv3.csv', header=False)

df = pd.read_csv('data/csv/newcsv3.csv', names=['Date', 'South_Holland_HPI'], index_col=0)
print(df.head())
