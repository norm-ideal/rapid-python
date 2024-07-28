import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('https://iis.edu.tama.ac.jp/ban-country-formatted-noip.csv')
print(df.head())

d2 = df
d2['datetime'] = pd.to_datetime(d2['date']+'T'+d2['time'])
d2['country'] = d2['country'].str.upper()

print(d2.head())

d2['hh'] = d2['datetime'].dt.hour
d2['date'] = d2['datetime'].dt.date
print(d2.head())

dailyCount = d2.groupby('date',as_index=False)['country'].count()
dailyCount.columns = ['date','count']
print(dailyCount.head(20))

countryCount = d2.groupby('country',as_index=False)['date'].count()
countryCount.columns = ['country','count']
countryCount.sort_values(by='count', axis=0, ascending=False, inplace=True)
print(countryCount.head(10))


# dailyCount.plot.bar('date','count')






