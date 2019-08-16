import pandas as pd
import seaborn as sns
df = sns.load_dataset("mpg")
df.shape
df
#값 소팅하기, ascending=False 역순정렬
df.sort_values("mpg").head()
df.sort_values("mpg",ascending=False).head()

#column명 바꾸기
df = df.rename(columns={"model_year":"Year"})
#index 소팅, 역시 ascending=False 로 역순으로 가능
df.sort_index(ascending=False)
#컬럼 지우기, 중요한건 이걸 다시 df=df.drop(columns="cylinders") 이렇게 해줘야 저장된다
df.drop(columns="cylinders")
