import os
import pandas as pd

os.chdir(r'D:\Downloads')
file = r'dataset_345422_14 (1).txt'
df = pd.read_csv(file, delimiter=',', parse_dates=['Date'])

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

df = df.dropna(axis=1)

df['dayofweek'] = df['Date'].dt.dayofweek

max_day = df.groupby('dayofweek').mean().sum(axis=1).idxmax()

print(days[max_day])
