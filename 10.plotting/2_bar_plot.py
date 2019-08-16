import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline

#한글폰트 사용시 그래프에서 마니어스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False
# plot
#  kind:str
#  - 'line' : line plot(default)
###  - 'bar'  : vertical bar plot
#  - 'barh' : horizontal bar plot
#  - 'hist' : histogram
#  - 'box'  : boxplot
#  - 'kde'  : kernel Density Estimation plot
#  - 'density': same as 'kde'
#  - 'area' : area plot
#  - 'pie'  : pie plot
#  - 'scatter' : scatter plot
#  - 'hexbin': hexbin plot

ts= pd.Series(np.random.randn(1000),index = pd.date_range('1/1/2000',periods=1000))
ts.head()

df=pd.DataFrame(np.random.randn(1000,4),index = ts.index,columns=["A","B","C","D"])
df.head(6)
df.iloc[5].plot(kind='bar')

df.iloc[5].plot.bar()
plt.axhline(0,color='k')

df2 = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df2.plot.bar()
df2.plot.bar(stacked=True)
df2.plot.barh(stacked=True)
