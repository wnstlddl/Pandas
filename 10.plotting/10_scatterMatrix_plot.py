import pandas as pd
import numpy as np
import matplotlib as mpl
from pandas.plotting import scatter_matrix
%matplotlib inline

#한글폰트 사용시 그래프에서 마니어스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

df= pd.DataFrame(np.random.randn(1000,4),columns=list('abcd'))

df.head()

#kde = 커널밀도함수
scatter_matrix(df,alpha = 0.2,figsize=(10,5),diagonal='kde')
