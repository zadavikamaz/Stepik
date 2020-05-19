import pandas as pd
import os

file = r'dataset_file_storage.csv'
os.chdir(r'D:\Downloads')
df = pd.read_csv(file, delimiter=';')

fs_of_prid = df.groupby(['CompanyID', 'ProjectID'], as_index=False).aggregate({'FileSize': 'sum'})
all_size = fs_of_prid.FileSize.mean()
out = fs_of_prid[fs_of_prid.FileSize > all_size]

print(len(out.groupby('CompanyID')))