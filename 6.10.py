import pandas as pd
import os

file_order = r'orders.csv'
file_prod = r'Products.csv'
os.chdir(r'D:\Downloads')

order = pd.read_csv(file_order, delimiter=';')
prod = pd.read_csv(file_prod, delimiter=';')

df = pd.merge(order, prod, how='left', left_on='ID товара', right_on='Product_ID')

df = df[df['Оплачен'] == 'Да']

df = df[df['Name'].apply(lambda x: True if 'Носки' in str(x) else False)]

df['Total'] = df['Количество']* df['Price']

print(df.Total.sum())

'''
s = df[(df['Оплачен'] == 'Да') & (df['Name'].str.contains('Носки'))]
print(sum(s['Price'] * s['Количество']))
'''