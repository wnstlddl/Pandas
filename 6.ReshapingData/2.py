import pandas as pd
df = pd.DataFrame({"A":{0:"a", 1:"b",2:"c"},"B":{0:1,1:3,2:5},"C":{0:2,1:4,2:6}})
df

cf = pd.DataFrame({"A" : ["a","b","c"],"B" :[1,3,5],"C":[2,4,6]},index = [0,1,2])
cf

pd.melt(df,id_vars=['A'],value_vars=['B','C'])
pd.melt(df,value_vars=['A','B','C'])
pd.melt(df,value_vars=['A','B','C']).rename(columns={'variable':'var','value':'val'})

df2= pd.DataFrame({'bar':['a','b','c','d','e'],'baz':[1,2,3,4,5,],'foo':['one','one','one','two','two']})
