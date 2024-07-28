# だいたい正しい Python 入門（番外編）

Copyright © 2022 IDEHARA, Norimimichi. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the license is included in the section entitled “GNU Free Documentation License”.

---
subtitle: 初心者のための関数定義

author: "出原至道 (idehara@tama.ac.jp)"

date: \today{}

---

\newpage

## データ処理をやってみよう

### データ処理のためのライブラリ

```Python
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
```

解説は後で書く。

