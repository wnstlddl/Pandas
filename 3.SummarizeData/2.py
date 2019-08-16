import pandas as pd
import seaborn as sns

df = sns.load_dataset('iris')
# apply 는 함수를 만들고 함수를 호출해서 데이터 전처리하게 만드는것
df.apply(lambda x : x[0])
df['species'].apply(lambda x : x[:3])
df['species_3'] = df['species'].apply(lambda x : x[:3])

def smp(x):
    x = x[-3:]
    return x

df['species-3'] = df['species'].apply(smp)
df
