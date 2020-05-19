import pandas as pd
import os

os.chdir(r'D:\Downloads')
df = pd.read_csv('StudentsPerformance.csv')
# ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course',
# 'math score', 'reading score', 'writing score']

reading_score= df.groupby(['gender', 'race/ethnicity']).aggregate({'reading score':'median'})
print(reading_score)
print(int(reading_score.max()))
