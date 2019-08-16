import pandas as pd
import numpy as np

df = pd.DataFrame([[np.nan,2,np.nan,0],[3,4,np.nan,1],[np.nan,np.nan,np.nan,5]],columns=list('ABCD'))
df

#dropna axis =1 columns, axis = 0 row, how -'all' 이면 모두 값이 없으면 제거, 'any' 하나라도 값이 없으면 제#
df.dropna(axis=1,how='all')
df.dropna(axis=0,how='all')

#fillna 는 채우는거
df.fillna(0)
valuse = {'A':0,'B':1,'C':2,'D':3}

df.fillna(value=valuse)

df.isnull()
df.isnull().sum()
