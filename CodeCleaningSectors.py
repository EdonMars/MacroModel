import pandas as pd

df = pd.read_json('src/SECTORS/IYZ_TELCO.json')
df_clean = pd.DataFrame(columns=['date', 'IYZ%'])

for index, row in df.iterrows():
    date = row['historical']['date']
    price = row['historical']['close']
    
    df_clean.loc[len(df_clean)] = [pd.to_datetime(date), float(price)]
    
df_clean = df_clean.sort_values(by='date')
df = df_clean.reset_index(drop=True)

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

df_first_day = df.groupby(pd.Grouper(freq='MS')).first()
df_growth = df_first_day.pct_change().dropna()

df_growth['IYZ%'] = df_growth['IYZ%'] * 100
telco_df = df_growth.reset_index(drop=False)

print('1/10')


df = pd.read_json('src/SECTORS/XLB_MATERIALS.json')
df_clean = pd.DataFrame(columns=['date', 'XLB%'])

for index, row in df.iterrows():
    date = row['historical']['date']
    price = row['historical']['close']
    
    df_clean.loc[len(df_clean)] = [pd.to_datetime(date), float(price)]
    
df_clean = df_clean.sort_values(by='date')
df = df_clean.reset_index(drop=True)

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

df_first_day = df.groupby(pd.Grouper(freq='MS')).first()
df_growth = df_first_day.pct_change().dropna()

df_growth['XLB%'] = df_growth['XLB%'] * 100
materials_df = df_growth.reset_index(drop=False)

print('2/10')


df = pd.read_json('src/SECTORS/XLE_ENERGY.json')
df_clean = pd.DataFrame(columns=['date', 'XLE%'])

for index, row in df.iterrows():
    date = row['historical']['date']
    price = row['historical']['close']
    
    df_clean.loc[len(df_clean)] = [pd.to_datetime(date), float(price)]
    
df_clean = df_clean.sort_values(by='date')
df = df_clean.reset_index(drop=True)

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

df_first_day = df.groupby(pd.Grouper(freq='MS')).first()
df_growth = df_first_day.pct_change().dropna()

df_growth['XLE%'] = df_growth['XLE%'] * 100
energy_df = df_growth.reset_index(drop=False)

print('3/10')


df = pd.read_json('src/SECTORS/XLF_FINANCE.json')
df_clean = pd.DataFrame(columns=['date', 'XLF%'])

for index, row in df.iterrows():
    date = row['historical']['date']
    price = row['historical']['close']
    
    df_clean.loc[len(df_clean)] = [pd.to_datetime(date), float(price)]
    
df_clean = df_clean.sort_values(by='date')
df = df_clean.reset_index(drop=True)

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

df_first_day = df.groupby(pd.Grouper(freq='MS')).first()
df_growth = df_first_day.pct_change().dropna()

df_growth['XLF%'] = df_growth['XLF%'] * 100
finance_df = df_growth.reset_index(drop=False)

print('4/10')


df = pd.read_json('src/SECTORS/XLI_INDUSTRIAL.json')
df_clean = pd.DataFrame(columns=['date', 'XLI%'])

for index, row in df.iterrows():
    date = row['historical']['date']
    price = row['historical']['close']
    
    df_clean.loc[len(df_clean)] = [pd.to_datetime(date), float(price)]
    
df_clean = df_clean.sort_values(by='date')
df = df_clean.reset_index(drop=True)

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

df_first_day = df.groupby(pd.Grouper(freq='MS')).first()
df_growth = df_first_day.pct_change().dropna()

df_growth['XLI%'] = df_growth['XLI%'] * 100
industrial_df = df_growth.reset_index(drop=False)

print('5/10')


df = pd.read_json('src/SECTORS/XLK_TECH.json')
df_clean = pd.DataFrame(columns=['date', 'XLK%'])

for index, row in df.iterrows():
    date = row['historical']['date']
    price = row['historical']['close']
    
    df_clean.loc[len(df_clean)] = [pd.to_datetime(date), float(price)]
    
df_clean = df_clean.sort_values(by='date')
df = df_clean.reset_index(drop=True)

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

df_first_day = df.groupby(pd.Grouper(freq='MS')).first()
df_growth = df_first_day.pct_change().dropna()

df_growth['XLK%'] = df_growth['XLK%'] * 100
tech_df = df_growth.reset_index(drop=False)

print('6/10')


df = pd.read_json('src/SECTORS/XLP_CONSUMER_PRIMARY.json')
df_clean = pd.DataFrame(columns=['date', 'XLP%'])

for index, row in df.iterrows():
    date = row['historical']['date']
    price = row['historical']['close']
    
    df_clean.loc[len(df_clean)] = [pd.to_datetime(date), float(price)]
    
df_clean = df_clean.sort_values(by='date')
df = df_clean.reset_index(drop=True)

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

df_first_day = df.groupby(pd.Grouper(freq='MS')).first()
df_growth = df_first_day.pct_change().dropna()

df_growth['XLP%'] = df_growth['XLP%'] * 100
consumer_primary_df = df_growth.reset_index(drop=False)

print('7/10')


df = pd.read_json('src/SECTORS/XLV_HEALTH.json')
df_clean = pd.DataFrame(columns=['date', 'XLV%'])

for index, row in df.iterrows():
    date = row['historical']['date']
    price = row['historical']['close']
    
    df_clean.loc[len(df_clean)] = [pd.to_datetime(date), float(price)]
    
df_clean = df_clean.sort_values(by='date')
df = df_clean.reset_index(drop=True)

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

df_first_day = df.groupby(pd.Grouper(freq='MS')).first()
df_growth = df_first_day.pct_change().dropna()

df_growth['XLV%'] = df_growth['XLV%'] * 100
health_df = df_growth.reset_index(drop=False)

print('8/10')


df = pd.read_json('src/SECTORS/XLY_CONSUMER_NON_PRIMARY.json')
df_clean = pd.DataFrame(columns=['date', 'XLY%'])

for index, row in df.iterrows():
    date = row['historical']['date']
    price = row['historical']['close']
    
    df_clean.loc[len(df_clean)] = [pd.to_datetime(date), float(price)]
    
df_clean = df_clean.sort_values(by='date')
df = df_clean.reset_index(drop=True)

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

df_first_day = df.groupby(pd.Grouper(freq='MS')).first()
df_growth = df_first_day.pct_change().dropna()

df_growth['XLY%'] = df_growth['XLY%'] * 100
consumer_non_primary_df = df_growth.reset_index(drop=False)

print('9/10')


df = pd.read_json('src/SECTORS/XLU_PUBLIC.json')
df_clean = pd.DataFrame(columns=['date', 'XLU%'])

for index, row in df.iterrows():
    date = row['historical']['date']
    price = row['historical']['close']
    
    df_clean.loc[len(df_clean)] = [pd.to_datetime(date), float(price)]
    
df_clean = df_clean.sort_values(by='date')
df = df_clean.reset_index(drop=True)

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

df_first_day = df.groupby(pd.Grouper(freq='MS')).first()
df_growth = df_first_day.pct_change().dropna()

df_growth['XLU%'] = df_growth['XLU%'] * 100
public_df = df_growth.reset_index(drop=False)

print('10/10')


from functools import reduce

dfs = [public_df, telco_df, materials_df, energy_df, finance_df, industrial_df, tech_df, consumer_primary_df, consumer_non_primary_df, health_df]
sectors_df = reduce(lambda left, right: pd.merge(left, right, on='date', how='inner'), dfs)

