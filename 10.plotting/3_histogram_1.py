import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

%matplotlib inline

#한글폰트 사용시 그래프에서 마니어스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame({'a':np.random.randn(1000)+1,'b' :np.random.randn(1000),'c':np.random.randn(1000)-1},columns=list("abc"))
df.head()

#alpha 는 투명도를 의미 bins 는 x축 분할수 기본은 10으로 설정되어잇
df.plot.hist(alpha=0.3,bins=20)
#stacked 는 그 위로 누적해서 그리기

df.plot.hist(stacked=True,bins=20)

# orientation='horizontal' 세로로, cumulative='True' 누적시키기
df['a'].plot.hist(orientation='horizontal',cumulative='True')
