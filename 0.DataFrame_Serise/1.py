import pandas as pd

df = pd.DataFrame(
    {"a" : [4 ,5, 6],
    "b" : [7, 8, 9],
    "c" : [10, 11, 12]},
    index = [1, 2, 3])

df = pd.DataFrame(
    [[4, 7, 10],
    [5, 8, 11],
    [6, 9, 12]],
    index=[1, 2, 3],
    columns=['a', 'b', 'c'])

# #전체 보기
# print(df)
# # 해당 열 보기
# print(df["a"])
# print(df[["b","c"]])
# #해당 행 보기
# print(df.loc[1])
# print(df.loc[[1,2]])
# #해당 원소 보기
# print(df.loc[3,"a"])
# print(df.loc[[1,2],["a","b"]])

df = pd.DataFrame(
    {"a" : [4 ,5, 6],
    "b" : [7, 8, 9],
    "c" : [10, 11, 12]},
    index = pd.MultiIndex.from_tuples( [('d',1),('d',2),('e',2)], names=['n','v']))

print(df)
