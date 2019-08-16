import pandas as pd

#꿀팁 concat은 위아래로 열을 합칠때, merge는 행을 붙일때 주로 쓴다


adf= pd.DataFrame({"x1":["A","B","c"],"x2":[1,2,3]})
bdf= pd.DataFrame({"x1":["A","B","D"],"x3":["T","F","T"]})
adf
bdf
pd.merge(adf,bdf,how='left', on='x1')
pd.merge(adf,bdf,how='right', on='x1')
pd.merge(bdf,adf,how='left', on='x1')
pd.merge(adf,bdf,how='inner', on='x1')
pd.merge(adf,bdf,how='outer', on='x1')
adf[adf.x1.isin(bdf.x1)]
adf[~adf.x1.isin(bdf.x1)]

adf= pd.DataFrame({"x1":["A","B","C"],"x2":[1,2,3]})
bdf= pd.DataFrame({"x1":["B","C","D"],"x2":[2,3,4]})
adf
bdf
pd.merge(adf,bdf)

pd.merge(adf,bdf,how='outer')

pd.merge(adf,bdf,how='outer',indicator=True)
pd.merge(adf,bdf,how='outer',indicator=True).query('_merge=="left_only"').drop(columns=['_merge'])
pd.merge(adf,bdf,how='outer',indicator=True).query('_merge=="left_only"')
