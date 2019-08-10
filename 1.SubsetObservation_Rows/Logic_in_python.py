import pandas as pd
import numpy as np
df = pd.DataFrame({"a":[1,2,3],"b":[4,5,6],"c":[7,8,9]},index=[1,2,3])

print(df["b"] != 4)
print(df[df["b"] != 4])
# 해당 열에 그 값이 존재하나? 리스트 형태로 or 조건인듯?
print(df["b"].isin([4,5]))

# null    값 존재여부 확인, 반대함수 notnull()
df = pd.DataFrame({"a":[1,2,3,np.nan],"b":[4,5,np.nan,6],"c":[np.nan,7,8,9]},index=[1,2,3,4])

print(df)
print(pd.isnull(df))
print(pd.isnull(df).sum())
print(df.c.isnull())
