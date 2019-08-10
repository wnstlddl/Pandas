import pandas as pd
import numpy as np
df = df = pd.DataFrame({"a":[1,2,3,np.nan],"b":[4,5,np.nan,6],"c":[np.nan,7,8,9]},index=[1,2,3,4])

print(df)
# head(n)- 위에서부터 n개의 행 가져오기, tail(n)뒤에서부터 n개의 행 가져오기
print(df.head(2))
print(df.tail(2))

# frac 안의 숫자 비율로 행을 랜덤하게 가져오기 4개의 행에서서 frac=0.5이면 2개만 랜덤하게 뽑아온다
print(df.sample(frac=0.5))
# n개의 갯수만큼만 랜덤하게 샘플링 해옴
print(df.sample(n=3))
# index 범위대로 가져오기
print(df.iloc[:2])
print(df.iloc[2:])
# 해당 열에서 n개의 큰갯수nlargest(n,"열"), n개의 작은갯 nsmallest(n,"열") 단 해당열이 다 숫자형태
df = pd.DataFrame({"a": [1,10,8,11,-1],"b": list('abced'),"c": [1.0,2.0,np.nan,3.0,4.0]})
print(df)
print(df.nlargest(2,"a"))
print(df.nlargest(1,"a"))
print(df.nsmallest(2,"c"))
print(df.nsmallest(1,"c"))
