import pandas as pd
import seaborn as sns

df = sns.load_dataset('iris')
df.shape
df.head()

# 각각의 값을 그룸화 해서 카운트해줌
df['species'].value_counts()
    #보통 사용할때 새로운 데이터 프레임을 만들어서 갯수를 데이터화함
df_specise = pd.DataFrame(df['species'].value_counts())
print(df_specise)
print(df_specise.iloc[:2])
#데이터 갯수
print(len(df))
print(df.shape)
# columns 내 유니크한 value 카운
print(df['species'].nunique())
# 데이터의 통계적 수치  describe(include=[]) np.number = 수자형 데이터만, np.object 는 숫제외 데이터들
print(df.describe())

df["sepal_length"].sum()
df["sepal_length"].count()
#중간값과 평균값은 다르다
df["sepal_length"].median()
df["sepal_length"].mean()

df["sepal_length"].quantile([0.25,0.75])
df["sepal_length"].min()
df["sepal_length"].max()
df["sepal_length"].var() #분산
df["sepal_length"].std() #표준편차
