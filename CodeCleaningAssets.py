import pandas as pd
import numpy as np
from datetime import datetime, timedelta

df = pd.read_csv('src/ASSETS/2_YB.csv')
two_years_bond_df = df.rename(columns={'DATE': 'date', 'DGS2': '2YR'})
two_years_bond_df = two_years_bond_df.drop(two_years_bond_df[two_years_bond_df['2YR'] == '.'].index)
two_years_bond_df['2YR'] = two_years_bond_df['2YR'].astype(float).round(2)
two_years_bond_df["date"] = pd.to_datetime(two_years_bond_df["date"], format="%Y-%m-%d")

df = pd.read_csv('src/ASSETS/10_YB.csv')
ten_years_bond_df = df.rename(columns={'DATE': 'date', 'DGS2': '10YR'}).dropna()
ten_years_bond_df['date'] = pd.to_datetime(ten_years_bond_df['date'])
ten_years_bond_df = ten_years_bond_df.set_index('date')
ten_years_bond_df = ten_years_bond_df.resample('MS').first()
ten_years_bond_df = ten_years_bond_df.reset_index()
ten_years_bond_df = ten_years_bond_df.rename(columns={' value': '10YR'})

df = pd.read_csv('src/ASSETS/GOLD.csv', sep=";", header=None)
df = df.rename(columns={0: 'date', 1: 'gold'}).dropna()
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")
df['date'] = df['date'].dt.strftime('%Y-%m')
df['date'] = pd.to_datetime(df['date']) + pd.offsets.MonthBegin(1)
df['gold'] = df['gold'].str.replace(',', '.')
df['gold'] = pd.to_numeric(df['gold'])
df['gold%'] = (df['gold'].diff() / df['gold'].shift()) * 100
gold_df = df[['date', 'gold%']].dropna()

df = pd.read_csv('src/ASSETS/NASDAQ_COMPOSITE.csv')
df = df.rename(columns={'DATE': 'date', 'NASDAQCOM_PCH': 'nasdaq%'}).dropna()
df = df.drop(df[df['nasdaq%'] == '.'].index)
df['nasdaq%'] = df['nasdaq%'].astype(float)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
nas_df = df

df = pd.read_csv('src/ASSETS/SP500.csv')
df = df.drop(['Apertura', 'Massimo', 'Minimo', 'Vol.', 'Var. %'], axis=1)
df = df.rename(columns={'Data': 'date', 'Ultimo': 'SP500'})
df["date"] = pd.to_datetime(df["date"], format="%d.%m.%Y")
df = df.sort_values('date', ascending=True).reset_index().drop('index', axis=1)
df['SP500'] = df['SP500'].str.replace('.', '')
df['SP500'] = df['SP500'].apply(lambda x: x.replace(',', '.'))
df['SP500'] = pd.to_numeric(df['SP500'])
df['sp500%'] = (df['SP500'].diff() / df['SP500'].shift()) * 100
df = df.drop('SP500', axis=1)
sp_df = df.dropna()

df = pd.read_csv('src/ASSETS/OILWTI.csv')
df = df.rename(columns={'DATE': 'date', 'WTISPLC_PCH': 'oil%'}).dropna()
df['date'] = pd.to_datetime(df['date'])
oil_df = df

from functools import reduce

dfs = [sp_df, nas_df, gold_df, two_years_bond_df, ten_years_bond_df, oil_df]
assets_df = reduce(lambda left, right: pd.merge(left, right, on='date', how='inner'), dfs)