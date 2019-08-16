import pandas as pd
import numpy as np
import matplotlib as mpl
%matplotlib inline

#한글폰트 사용시 그래프에서 마니어스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

df= pd.DataFrame(np.random.rand(1000,2),columns=['a','b'])
df['b'] = df['b']+np.arange(1000)

df.plot.hexbin(x='a',y='b',gridsize=25)

df['z'] = np.random.uniform(0,3,1000)

df.plot.hexbin(x='a',y='b',C='z',reduce_C_function=np.max,gridsize=25)
