import pandas as pd
import random

# Исходные данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем пустой DataFrame для one-hot encoding
one_hot_df = pd.DataFrame(columns=['robot', 'human'])

# Проходим по строкам и заполняем one-hot DataFrame
for index, row in data.iterrows():
    if row['whoAmI'] == 'robot':
        one_hot_df.loc[index] = [1, 0]
    else:
        one_hot_df.loc[index] = [0, 1]

one_hot_df.head()
print(one_hot_df.head())
