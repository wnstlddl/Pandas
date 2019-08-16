import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

%matplotlib inline

#한글폰트 사용시 그래프에서 마니어스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame(np.random.randn(10,5),columns=['a','b','c','d','f'])
df.describe()
df.plot.box()
color = {'boxes':'DarkGreen','whiskers':'DarkOrange','medians':'DarkBlue','caps':'Gray'}
df.plot.box(color=color,sym='r+')
df.plot.box(color=color,sym='r+',vert=False)
#plot.box() 는 그리드 없고 걍 바로 boxplot() 은 그리드 있따

df.boxplot()
