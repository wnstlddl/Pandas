import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import openpyxl

#%matplotlib inline

#한글폰트 사용시 그래프에서 마니어스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame(np.random.rand(10,5),columns=['a','b','c','d','f'])


# scatter 는 x,y 를 무조건 택해야하고 s는 점의 크기
ax=df.plot.scatter(x='a', y='b',color='DarkRed', label ='Group 1')
ax1=df.plot.scatter(x='a', y='c',color='DarkBlue', label ='Group 2',ax=ax)
df.plot.scatter(x='a', y='d',s=50, label ='Group 3',ax =ax1,c='c')

print(df.plot.scatter(x='a', y='b', label ='Group 1',c='c'))
df.to_excel('foo.xlsx',sheet_name='Sheet1')
