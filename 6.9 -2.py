import pandas as pd
import os

os.chdir(r'D:\Downloads')
df = pd.read_csv('StudentsPerformance.csv')
# ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course',
# 'math score', 'reading score', 'writing score']

"""
gender — пол абитуриента  (female - женщина, male - мужчина);
race/ethnicity — национальность (зашифрована в виде значений "group A", "group B" и т.д.);
parental level of education — уровень образования родителей;
lunch — насколько качественно пообедал абитуриент перед тестом;
test preparation course — закончил ли абитуриент подготовительные курсы;
math score — оценка по математике;
reading score — оценка по чтению;
writing score — оценка по письму."""

'''Какое среднее значение оценок по всем предметам у мальчиков из такой же группы с уровнем образования как у 
родителей девочек, получивших максимальную среднюю оценку по всем предметам?
Ответ округлите до одного знака после запятой.'''

df['cost'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
par_lv = df[df.gender == 'female'].groupby(['parental level of education']).aggregate({'cost':'mean'})
par_degree = par_lv.idxmax()[0] #заведение которое окончили родители получившие максимальный средний балл

print(
    df[(df['parental level of education'] == par_degree) & (df.gender == 'male')].aggregate({'cost':'mean'})
)