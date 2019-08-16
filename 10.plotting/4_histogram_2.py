import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

%matplotlib inline

#한글폰트 사용시 그래프에서 마니어스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame({'a':np.random.randn(1000)+1,'b' :np.random.randn(1000),'c':np.random.randn(1000)-1},columns=list("abc"))

#diff 는 앞에값과 뒤의값의 차
df['a_diff'] = df['a'].diff()
df[['a','a_diff']]
#shift 는 그만큼 shift 누적시키기
df['a_shift'] = df['a'].shift(1)
df[['a','a_shift']]
df[['a','b','c']].diff().hist(color='k',alpha=0.5,bins=20)
df[['a','b','c']].hist(color='k',alpha=0.5,bins=50,figsize=(10,10))
#plot.hist() 와 걍 .hist() 의 차이는 plot.hist()는 한 그래프에 다같이 그리기, 걍 hist는 각자 따로 그리기
df.plot.hist()

data= pd.Series(np.random.randn(1000))
data.hist(figsize=(10,10))
