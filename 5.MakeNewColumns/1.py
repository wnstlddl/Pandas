import pandas as pd
import numpy as np
df=pd.DataFrame({"A":range(1,11),"B":np.random.randn(10)})

#새로운 column 만드는 방법
df.assign(In_A = lambda x:np.log(x.A))
df["sqrt"] = np.sqrt(df.A)

#숫자형 데이터를 카테고리컬하게 바꿔줄때 qcut 사용
pd.qcut(df.B,2,labels=False)
 #axis =0 열에서의 min,max axis =1 행에서의 min max
df.max(axis=1)
df.max(axis=0)
# 임계치를 정해주는
df["A"].clip(lower=5,upper=10)
# 절대값
df["B"]
df["B"].abs()
