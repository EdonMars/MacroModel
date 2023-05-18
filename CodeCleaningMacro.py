import pandas as pd
import numpy as np


df = pd.read_csv('src/MACRO/FED_EFFECTIVE_FUNDS.csv')
interest_rate_df = df.rename(columns={'DATE': 'date', 'DFF': 'interest_rate'})
interest_rate_df = interest_rate_df.drop(interest_rate_df[interest_rate_df['interest_rate'] == '.'].index)
interest_rate_df['interest_rate'] = interest_rate_df['interest_rate'].astype(float)
interest_rate_df["date"] = pd.to_datetime(interest_rate_df["date"], format="%Y-%m-%d")

df = pd.read_csv('src/MACRO/CPI_MOM.csv')
df = df.rename(columns={'DATE': 'date', 'CPIAUCSL_PCH': 'cpi_mom%'})
df['cpi_mom%'] = df['cpi_mom%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
cpi_mom_df = df

df = pd.read_csv('src/MACRO/CPI_YOY.csv')
df = df.rename(columns={'DATE': 'date', 'CPIAUCSL_PC1': 'cpi_yoy%'})
df['cpi_yoy%'] = df['cpi_yoy%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
cpi_yoy_df = df

df = pd.read_csv('src/MACRO/GDP_QOQ.csv')
df = df.rename(columns={'DATE': 'date', 'GDP_PCH': 'gdp_qoq%'})
df['gdp_qoq%'] = df['gdp_qoq%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
df = df.set_index('date')
df = df.resample('MS').asfreq()
df = df.interpolate(method='linear')
df = df.reset_index()
df['gdp_qoq%'] = df['gdp_qoq%'].astype(float).round(2)
gdp_qoq_df = df

df = pd.read_csv('src/MACRO/M2_MOM.csv')
df = df.rename(columns={'DATE': 'date', 'M2REAL_PCH': 'm2_mom%'})
df['m2_mom%'] = df['m2_mom%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
m2_mom_df = df

df = pd.read_csv('src/MACRO/M2_YOY.csv')
df = df.rename(columns={'DATE': 'date', 'M2REAL_PC1': 'm2_yoy%'})
df['m2_yoy%'] = df['m2_yoy%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
m2_yoy_df = df

df = pd.read_csv('src/MACRO/PPI_YOY_COMMODITIES_ALL.csv')
df = df.rename(columns={'DATE': 'date', 'PPIACO_PC1': 'ppi_comm_yoy%'})
df['ppi_comm_yoy%'] = df['ppi_comm_yoy%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
ppi_yoy_comm_df = df

df = pd.read_csv('src/MACRO/INDUSTRIAL_PRODUCTION_MOM.csv')
df = df.rename(columns={'DATE': 'date', 'INDPRO_PCH': 'ind_prod_mom%'})
df['ind_prod_mom%'] = df['ind_prod_mom%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
ind_prod_mom_df = df

df = pd.read_csv('src/MACRO/INDUSTRIAL_PRODUCTION_YOY.csv')
df = df.rename(columns={'DATE': 'date', 'INDPRO_PC1': 'ind_prod_yoy%'})
df['ind_prod_yoy%'] = df['ind_prod_yoy%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
ind_prod_yoy_df = df

df = pd.read_csv('src/MACRO/BANK_PRIME_LOAN.csv')
df = df.rename(columns={'DATE': 'date', 'DPRIME': 'bank_prime_loan_rate'})
df = df.drop(df[df['bank_prime_loan_rate'] == '.'].index)
df['bank_prime_loan_rate'] = df['bank_prime_loan_rate'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
bank_loan_df = df

df = pd.read_csv('src/MACRO/PPI_YOY_COMMODITIES_CHEMICALS.csv')
df = df.rename(columns={'DATE': 'date', 'WPU06_PC1': 'ppi_yoy_chem%'})
df['ppi_yoy_chem%'] = df['ppi_yoy_chem%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
ppi_yoy_chem_df = df

df = pd.read_csv('src/MACRO/PPI_YOY_COMMODITIES_CONSTRUCTION.csv')
df = df.rename(columns={'DATE': 'date', 'WPUSI012011_PC1': 'ppi_yoy_constr%'})
df['ppi_yoy_constr%'] = df['ppi_yoy_constr%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
ppi_yoy_constr_df = df

df = pd.read_csv('src/MACRO/PPI_YOY_COMMODITIES_COPPER.csv')
df = df.rename(columns={'DATE': 'date', 'WPUSI019011_PC1': 'ppi_yoy_copper%'})
df['ppi_yoy_copper%'] = df['ppi_yoy_copper%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
ppi_yoy_copper_df = df

df = pd.read_csv('src/MACRO/PPI_YOY_COMMODITIES_INDUSTRIAL.csv')
df = df.rename(columns={'DATE': 'date', 'PPIIDC_PC1': 'ppi_yoy_industrial%'})
df['ppi_yoy_industrial%'] = df['ppi_yoy_industrial%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
ppi_yoy_industrial_df = df

df = pd.read_csv('src/MACRO/PPI_YOY_COMMODITIES_METALS.csv')
df = df.rename(columns={'DATE': 'date', 'WPU10_PC1': 'ppi_yoy_metals%'})
df['ppi_yoy_metals%'] = df['ppi_yoy_metals%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
ppi_yoy_metals_df = df

df = pd.read_csv('src/MACRO/PPI_YOY_COMMODITIES_PLYWOOD.csv')
df = df.rename(columns={'DATE': 'date', 'WPU083_PC1': 'ppi_yoy_wood%'})
df['ppi_yoy_wood%'] = df['ppi_yoy_wood%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
ppi_yoy_wood_df = df

df = pd.read_csv('src/MACRO/PPI_YOY_COMMODITIES_PROCESSED_GOODS.csv')
df = df.rename(columns={'DATE': 'date', 'WPSID61_PC1': 'ppi_yoy_proc_goods%'})
#df = df.drop(df[df['ppi_yoy_chem_df'] == '.'].index)
df['ppi_yoy_proc_goods%'] = df['ppi_yoy_proc_goods%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
ppi_yoy_proc_goods_df = df

df = pd.read_csv('src/MACRO/PPI_YOY_COMMODITIES_UNPROCESSED_GOODS.csv')
df = df.rename(columns={'DATE': 'date', 'WPSID62_PC1': 'ppi_yoy_unproc_goods%'})
df['ppi_yoy_unproc_goods%'] = df['ppi_yoy_unproc_goods%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
ppi_yoy_unproc_goods_df = df

df = pd.read_csv('src/MACRO/PPI_YOY_COMMODITIES_RUBBER_PLASTIC.csv')
df = df.rename(columns={'DATE': 'date', 'WPU07_PC1': 'ppi_yoy_rubber_plastic%'})
df['ppi_yoy_rubber_plastic%'] = df['ppi_yoy_rubber_plastic%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
ppi_yoy_rubber_plastic_df = df

df = pd.read_csv('src/MACRO/PPI_YOY_INDUSTRY.csv')
df = df.rename(columns={'DATE': 'date', 'PCUOMFGOMFG_PC1': 'ppi_yoy_industry%'})
df['ppi_yoy_industry%'] = df['ppi_yoy_industry%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
ppi_yoy_industry_df = df

df = pd.read_csv('src/MACRO/TRUCKS_SALES_YOY.csv')
df = df.rename(columns={'DATE': 'date', 'HTRUCKSSAAR_PC1': 'truck_sales_yoy%'})
df['truck_sales_yoy%'] = df['truck_sales_yoy%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
truck_sales_yoy_df = df

df = pd.read_csv('src/MACRO/TRUCKS_SALES_MOM.csv')
df = df.rename(columns={'DATE': 'date', 'HTRUCKSSAAR_PCH': 'truck_sales_mom%'})
df['truck_sales_mom%'] = df['truck_sales_mom%'].astype(float).round(2)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
truck_sales_mom_df = df

from functools import reduce

dfs = [interest_rate_df, cpi_yoy_df, cpi_mom_df, gdp_qoq_df, m2_yoy_df, m2_mom_df, ppi_yoy_comm_df, ind_prod_yoy_df, ind_prod_mom_df, bank_loan_df, ppi_yoy_chem_df, ppi_yoy_constr_df, ppi_yoy_copper_df, ppi_yoy_industrial_df, ppi_yoy_metals_df, ppi_yoy_wood_df, ppi_yoy_proc_goods_df, ppi_yoy_unproc_goods_df, ppi_yoy_rubber_plastic_df, ppi_yoy_industry_df, truck_sales_yoy_df, truck_sales_mom_df]
macro_df = reduce(lambda left, right: pd.merge(left, right, on='date', how='inner'), dfs)