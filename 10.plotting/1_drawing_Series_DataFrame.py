import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#matplotlib inline

#한글폰트 사용시 그래프에서 마니어스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False
# plot
#  kind:str
###  - 'line' : line plot(default)
#  - 'bar'  : vertical bar plot
#  - 'barh' : horizontal bar plot
#  - 'hist' : histogram
#  - 'box'  : boxplot
#  - 'kde'  : kernel Density Estimation plot
#  - 'density': same as 'kde'
#  - 'area' : area plot
#  - 'pie'  : pie plot
#  - 'scatter' : scatter plot
#  - 'hexbin': hexbin plot

ts = pd.Series(np.random.randn(1000),index = pd.date_range('1/1/2000',periods=1000))
ts
ts.cumsum().plot()
ts.plot()
ts = ts.cumsum()
ts.plot()

df = pd.DataFrame(np.random.randn(1000,4),index=ts.index,columns=list('ABCD'))
df = df.cumsum()
df.plot()

df3 = pd.DataFrame(np.random.randn(1000,2),columns=list('BC')).cumsum()
df3["A"] = pd.Series(list(range(len(df))))
df3.head()

df3.plot(x='A',y=['B','C'])
|
