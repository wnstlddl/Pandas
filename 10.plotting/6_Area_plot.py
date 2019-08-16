import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

%matplotlib inline

#한글폰트 사용시 그래프에서 마니어스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame(np.random.rand(10,5),columns=['a','b','c','d','f'])
#음수가 있으면 안되네욤
df.plot.area(stacked=False,alpha=0.3,grid = True)
df.plot(grid = True,stacked=False)
