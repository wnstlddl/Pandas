import pandas as pd
import seaborn as sns

df=sns.load_dataset("iris")
print(df.head())

columns =["sepal_length","sepal_width"]
df = df[columns]
print(df.head())
#특정 columns 을 가져올때 df["sepal_length"] or df.sepal_length
print(df["sepal_length"])
print(df.sepal_length) # 점을 해서 가져올때 한글 or 특수문자는 불가
# 정규 표현식을 이욯애서 columns 가져오기, 정규표현식 공부해야합니다....ㅠㅠ
print(df.filter(regex="width"))
#특정 columns 범위 가져오기 앞에 : 는 행의 범위 지정 가능 lioc는 열 지정할때 인덱스 번호로 되는데 loc는 안되네?그게 큰차이
df=sns.load_dataset("iris")
print(df)
print(df.loc[:,"sepal_length":"sepal_width"])
print(df.loc[2:5,"sepal_length":"sepal_width"])
print(df.iloc[0:3,[1,3]])
print(df.iloc[0:3,[1,2,3]])
print(df.loc[0:3,["sepal_length","sepal_width"]])
