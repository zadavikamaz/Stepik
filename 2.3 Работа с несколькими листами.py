import pandas as pd

PATH = r'D:\Downloads\trekking2.xlsx'
xl_1, xl_0 = pd.read_excel(PATH, sheet_name=(1)), pd.read_excel(PATH, sheet_name=(0))

data_merge = xl_1.merge(xl_0, left_on='Продукт', right_on='Unnamed: 0')
data_merge[['Продукт', 'Вес в граммах', 'ККал на 100', 'Б на 100', 'Ж на 100', 'У на 100']]
data_merge.drop(['Unnamed: 0'], axis=1, inplace=True)

data_merge[['Вес в граммах', 'ККал на 100', 'Б на 100', 'Ж на 100', 'У на 100']] = \
    data_merge[['Вес в граммах', 'ККал на 100', 'Б на 100', 'Ж на 100', 'У на 100']].fillna(0)

u = data_merge[['ККал на 100', 'Б на 100', 'Ж на 100', 'У на 100']]
v = data_merge['Вес в граммах']
out = {}
for col in u.columns:
    out[col] = sum(u[col]*v/100)

print(*map(int, out.values()))

"""
import pandas as pd

url = 'https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx'
calorific = pd.read_excel(url, sheet_name=0, index_col=0).fillna(0)
weight = pd.read_excel(url,	sheet_name=1, index_col=0)	
ration = pd.concat([weight, calorific], axis=1, join='inner')
print(*ration.apply(lambda x: x.iloc[1:] * x.iloc[0] / 100, axis=1).sum(axis=0).astype('int'))"""

'''' 
join='inner' объединяет по индексам, которые есть в обоих датафреймах. 
index_col=0 делает индексами первый столбец (с названиями продуктов). 
Иначе индексы будут от 0 до длины датафрейма без единицы.'''
