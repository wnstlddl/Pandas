import pandas as pd

s1 = pd.Series(['a','b'])
s2 = pd.Series(['c','d'])
s1
s2
pd.concat([s1,s2])
#앞에 인뎃스 삭제
pd.concat([s1,s2],ignore_index=True)
#키생성
pd.concat([s1,s2],keys=['s1','s2'])

pd.concat([s1,s2],keys=['s1','s2'],names=['dfdf','fgfgfg'])

df1 = pd.DataFrame([[1,2],[3,4],[5,6]])
df2 = pd.DataFrame([[7,8],[9,10],[11,12]])

df3 = pd.concat([df1,df2],ignore_index=True)
df3
