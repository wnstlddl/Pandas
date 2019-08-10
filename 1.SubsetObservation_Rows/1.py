import pandas as pd

df = pd.DataFrame({"a":[1,2,3],"b":[4,5,6],"c":[7,8,9]},index=[1,2,3])

# #해당조건 참 거짓
# print(df.b>4)
# print(df["b"]>4)
# #해당조건 참인 DataFream
# print(df[df.b>4])
# print(df[df.b==4])

df = pd.DataFrame({"a":[1,2,3,3],"b":[4,5,6,6],"c":[7,8,9,9]},index=[1,2,3,4])
print(df)
# 중복 행 삭제, drop_duplicates(), 변수를 변환시키진 않는다, 변환을 원하면 df = df.drop_duplicates()
print(df.drop_duplicates())
print(df)
