import pandas as pd
import numpy as np
%matplotlib inline
#시계열 분석에서 쓴다..?

s= pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2015',periods=1000))
s=s.cumsum()
s.plot()
# 이동평균
r= s.rolling(window=30)
r.mean()
s.plot(style='k--')
r.mean().plot(style='k--')

df= pd.DataFrame(np.random.randn(1000,4),index=pd.date_range('1/1/2015',periods=1000),columns=['A','B','C','D'])
df=df.cumsum()
df.plot()
df.rolling(window=60).sum().plot(subplots=True)
df.rolling(window=len(df),min_periods=1).mean().plot()
df.expanding(min_periods=1).mean().plot()
