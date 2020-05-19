import os
import pandas as pd

os.chdir(r'D:\Downloads')
file = r'football_players.csv'

df = pd.read_csv(file)

club_wage_mm = df.groupby('Club').aggregate({'Wage':['mean', 'median']})

print(club_wage_mm[club_wage_mm['Wage']['mean'] == club_wage_mm['Wage']['median']].__len__())

#df.groupby('Club')['Wage'].agg(lambda x: 1 if (x.mean() == x.median()) else 0).sum()

"""import pandas as pd
df = pd.read_csv('football_players.csv').groupby(['Club'])
gr = df['Wage'].agg(['mean', 'median'])
print(sum(gr['mean'] == gr['median']/1))"""



