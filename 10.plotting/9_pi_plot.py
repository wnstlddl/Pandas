import pandas as pd
import numpy as np
import matplotlib as mpl
%matplotlib inline

#한글폰트 사용시 그래프에서 마니어스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

series = pd.Series(3 * np.random.rand(4),index=['a','b','c','d'],name = 'series')
series.plot.pie(figsize=(6,6))
df = pd.DataFrame({'mass':[0.33,4.87,5.97],'radiuse':[2439,6051,6378]},index=['Mercury','Venus','Earth'])
df
df['mass'].plot.pie(figsize=(6,6))
df.plot.pie(subplots=True,figsize=(10,5))
