import pandas as pd
import seaborn as sns

df=sns.load_dataset("mpg")
df.head()
df.groupby(by="origin").size()
df["origin"].value_counts()

df.groupby(by="origin").min()
df.groupby(by="origin")['cylinders'].mean()
# 치트시트엔없는기능
pd.DataFrame(df.groupby(['model_year','origin'])['cylinders'].mean())

df2 = pd.DataFrame( {"a" : [4 ,5, 6], "b" : [7, 8, 9], "c" : [10, 11, 12]},    index = [1, 2, 3])
df2
df2.shift(-1)
df2['a'].shift(1)

df["model_year"].rank(method='min').value_counts()
df["model_year"].rank(pct=True).head()

df2.cumsum()
df2.cummin()
df2.cumprod()
