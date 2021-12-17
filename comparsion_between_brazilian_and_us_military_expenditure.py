import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# DataSet Import
expenditures = pd.read_csv('br-and-us-military-expenditure-1960-2019.csv')

# Brazil Decades
bra_decades = expenditures.iloc[0, 4:64].copy()
bra_60_to_70 = expenditures.iloc[0, 4:15].copy()
bra_70_to_80 = expenditures.iloc[0, 15:25].copy()
bra_80_to_90 = expenditures.iloc[0, 25:35].copy()
bra_90_to_00 = expenditures.iloc[0, 35:45].copy()
bra_00_to_10 = expenditures.iloc[0, 45:55].copy()
bra_10_decade = expenditures.iloc[0, 55:64].copy()

# US Decades
us_decades = expenditures.iloc[1, 4:64].copy()
us_60_to_70 = expenditures.iloc[1, 4:15].copy()
us_70_to_80 = expenditures.iloc[1, 15:25].copy()
us_80_to_90 = expenditures.iloc[1, 25:35].copy()
us_90_to_00 = expenditures.iloc[1, 35:45].copy()
us_00_to_10 = expenditures.iloc[1, 45:55].copy()
us_10_decade = expenditures.iloc[1, 55:64].copy()

''' Brazilian Military Expenditures Trough Decades '''

''' Brazilian Indexes Reset '''

# All decades
bra_decades = bra_decades.reset_index()
bra_decades.columns = ['year','amount']

# 60's to 70's
bra_60_to_70 = bra_60_to_70.reset_index()
bra_60_to_70.columns = ['year','amount']

# 70's to 80's
bra_70_to_80 = bra_70_to_80.reset_index()
bra_70_to_80.columns = ['year','amount']

# 80's to 90's
bra_80_to_90 = bra_80_to_90.reset_index()
bra_80_to_90.columns = ['year','amount']

# 90's to 00's
bra_90_to_00 = bra_90_to_00.reset_index()
bra_90_to_00.columns = ['year','amount']

# 00's to 10's
bra_00_to_10 = bra_00_to_10.reset_index()
bra_00_to_10.columns = ['year','amount']

# 10's decade
bra_10_decade = bra_10_decade.reset_index()
bra_10_decade.columns = ['year','amount']

''' Brazilian Separated Decades Expenditure '''

# 60's to 70's
plt.figure(figsize=(10,8))
sns.barplot(x='year', y='amount', data=bra_60_to_70, palette='crest')
plt.ylabel("Expenditure in USD (Trillions)", size=14)
plt.xlabel("Years", size=14)
plt.title("Brazil's Military Expenditure (1960 - 1970)", size=16)
plt.savefig("Brazil_Expenditure_Timeline_1960_1970.png")

# 70's to 80's
plt.figure(figsize=(10,8))
sns.barplot(x='year', y='amount', data=bra_70_to_80, palette='crest')
plt.ylabel("Expenditure in USD (Trillions)", size=14)
plt.xlabel("Years", size=14)
plt.title("Brazil's Military Expenditure (1971 - 1980)", size=16)
plt.savefig("Brazil_Expenditure_Timeline_1971_1980.png")

# 80's to 90's
plt.figure(figsize=(10,8))
sns.barplot(x='year', y='amount', data=bra_80_to_90, palette='crest')
plt.ylabel("Expenditure in USD (Trillions)", size=14)
plt.xlabel("Years", size=14)
plt.title("Brazil's Military Expenditure (1981 - 1990)", size=16)
plt.savefig("Brazil_Expenditure_Timeline_1981_1990.png")

# 90's to 00's
plt.figure(figsize=(10,8))
sns.barplot(x='year', y='amount', data=bra_90_to_00, palette='crest')
plt.ylabel("Expenditure in USD (Trillions)", size=14)
plt.xlabel("Years", size=14)
plt.title("Brazil's Military Expenditure (1991 - 2000)", size=16)
plt.savefig("Brazil_Expenditure_Timeline_1991_2000.png")

# 00's to 10's
plt.figure(figsize=(10,8))
sns.barplot(x='year', y='amount', data=bra_00_to_10, palette='crest')
plt.ylabel("Expenditure in USD (Trillions)", size=14)
plt.xlabel("Years", size=14)
plt.title("Brazil's Military Expenditure (2001 - 2010)", size=16)
plt.savefig("Brazil_Expenditure_Timeline_2001_2010.png")

# 10's decade
plt.figure(figsize=(10,8))
sns.barplot(x='year', y='amount', data=bra_10_decade, palette='crest')
plt.ylabel("Expenditure in USD (Trillions)", size=14)
plt.xlabel("Years", size=14)
plt.title("Brazil's Military Expenditure (2011 - 2018)", size=16)
plt.savefig("Brazil_Expenditure_Timeline_2011_2018.png")

''' Military Expenditure Timeline '''

plt.figure(figsize=(50,20))
sns.barplot(x='year', y='amount', data=bra_decades, palette='crest')
plt.ylabel("Expenditure in USD (Trillions)", size=22)
plt.xlabel("Years", size=22)
plt.title("Brazil's Military Expenditure Timeline", size=24)
plt.savefig("Brazil_Military_Expenditure_Timeline.png")

''' United States Military Expenditures Trough Decades '''

''' US Indexes Reset '''

# All decades
us_decades = us_decades.reset_index()
us_decades.columns = ['year','amount']

# 60's to 70's
us_60_to_70 = us_60_to_70.reset_index()
us_60_to_70.columns = ['year','amount']

# 70's to 80's
us_70_to_80 = us_70_to_80.reset_index()
us_70_to_80.columns = ['year','amount']

# 80's to 90's
us_80_to_90 = us_80_to_90.reset_index()
us_80_to_90.columns = ['year','amount']

# 90's to 00's
us_90_to_00 = us_90_to_00.reset_index()
us_90_to_00.columns = ['year','amount']

# 00's to 10's
us_00_to_10 = us_00_to_10.reset_index()
us_00_to_10.columns = ['year','amount']

# 10's decade
us_10_decade = us_10_decade.reset_index()
us_10_decade.columns = ['year','amount']

'''United States Separated Decades Expenditure**'''

# 60's to 70's
plt.figure(figsize=(10,8))
sns.barplot(x='year', y='amount', data=us_60_to_70, palette='rocket')
plt.ylabel("Expenditure in USD (Trillions)", size=14)
plt.xlabel("Years", size=14)
plt.title("United State's Military Expenditure (1960 - 1970)", size=16)
plt.savefig("US_Expenditure_Timeline_1960_1970.png")

# 70's to 80's
plt.figure(figsize=(10,8))
sns.barplot(x='year', y='amount', data=us_70_to_80, palette='rocket')
plt.ylabel("Expenditure in USD (Trillions)", size=14)
plt.xlabel("Years", size=14)
plt.title("United State's Military Expenditure (1971 - 1980)", size=16)
plt.savefig("US_Expenditure_Timeline_1971_1980.png")

# 80's to 90's
plt.figure(figsize=(10,8))
sns.barplot(x='year', y='amount', data=us_80_to_90, palette='rocket')
plt.ylabel("Expenditure in USD (Trillions)", size=14)
plt.xlabel("Years", size=14)
plt.title("United State's Military Expenditure (1981 - 1990)", size=16)
plt.savefig("US_Expenditure_Timeline_1981_1990.png")

# 90's to 00's
plt.figure(figsize=(10,8))
sns.barplot(x='year', y='amount', data=us_90_to_00, palette='rocket')
plt.ylabel("Expenditure in USD (Trillions)", size=14)
plt.xlabel("Years", size=14)
plt.title("United State's Military Expenditure (1991 - 2000)", size=16)
plt.savefig("US_Expenditure_Timeline_1991_2000.png")

# 00's to 10's
plt.figure(figsize=(10,8))
sns.barplot(x='year', y='amount', data=us_00_to_10, palette='rocket')
plt.ylabel("Expenditure in USD (Trillions)", size=14)
plt.xlabel("Years", size=14)
plt.title("United State's Military Expenditure (2001 - 2010)", size=16)
plt.savefig("US_Expenditure_Timeline_2001_2010.png")

# 10's decade
plt.figure(figsize=(10,8))
sns.barplot(x='year', y='amount', data=us_10_decade, palette='rocket')
plt.ylabel("Expenditure in USD (Trillions)", size=14)
plt.xlabel("Years", size=14)
plt.title("United State's Military Expenditure (2011 - 2018)", size=16)
plt.savefig("US_Expenditure_Timeline_2011_2018.png")

''' Military Expenditure Timeline '''

plt.figure(figsize=(50,20))
sns.barplot(x='year', y='amount', data=us_decades, palette='rocket')
plt.ylabel("Expenditure in USD (Trillions)", size=22)
plt.xlabel("Years", size=22)
plt.title("United State's Military Expenditure Timeline", size=24)
plt.savefig("US_Military_Expenditure_Timeline.png")

''' Comparsion Between United State's and Brazil's Military Expenditures '''

values_bra = pd.DataFrame(bra_decades, columns=['amount'])
values_bra.columns=['Brazil\'s Expenditure Amount']
values_bra

values_us = pd.DataFrame(us_decades, columns=['amount'])
values_us.columns=['United State\'s Expenditure Amount']


ax = values_bra.plot()
values_us.plot(ax=ax, figsize=(10,7))
plt.ylabel("Expenditure in USD (Trillions)", size=14)
plt.xlabel("Years", size=14)
plt.title("Comparsion of Brazil's and United State's Military Expenditure", size=16)
plt.savefig("Brazil_US_Military_Expenditure_Comparsion.png")