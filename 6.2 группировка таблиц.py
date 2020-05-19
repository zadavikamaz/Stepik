import pandas as pd
import numpy as np
import os

os.chdir(r'D:\Downloads')

df = pd.read_csv('dataset_345422_8 (5).txt', delimiter=';') #IP_PROP32 содержит размеры, IP_PROP30 цвета

pr_pn_xl = df.groupby(['IP_PROP30', 'IP_PROP32']).sum().loc['pink', 'XL']['CR_PRICE_1_USD']
qnt_pn_xl = df.groupby(['IP_PROP30', 'IP_PROP32']).sum().loc['pink', 'XL']['CP_QUANTITY']


print(pr_pn_xl*qnt_pn_xl)

'''
data = pd.read_csv('dataset_345422_8.txt',sep=';')
data['cost'] = data['CP_QUANTITY'] * data['CR_PRICE_1_USD']
print(data.groupby(['IP_PROP30','IP_PROP32'])['cost'].sum()['pink']['XL'])'''

'''
df = pd.read_csv('dataset_345422_8.txt', sep=';')
query = df.query("IP_PROP30 == 'pink' & IP_PROP32 == 'XL'")
print(query['CR_PRICE_1_USD'].dot(query['CP_QUANTITY']))'''