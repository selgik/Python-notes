# note021_NaN.py

# dataset:
import pandas as pd
data = {
    'name': ['Chae', 'Jung', 'Song', 'Seo', 'Kang', 'Byun', 'Hwang', 'Yun'],
    'school': ['Buk','Buk','Buk','Buk','Buk','Nong','Nong','Nong'],
    'height': [197, 184, 168, 187, 188, 202, 188, 190],    
    'kor' : [90, 40, 80, 40, 15, 80, 55, 100],
    'eng' : [85, 35, 75, 60, 20, 100, 65, 85],
    'math' : [100, 50, 70, 70, 10, 95, 45, 90],
    'phy' : [95, 55, 80, 75, 35, 85, 40, 95],
    'socio' : [85, 25, 75, 80, 10, 80, 35, 95],
    'sw' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}
df = pd.DataFrame(data, index = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8'])
df.index.name = 'app_name'
df.to_excel('score.xlsx')
df = pd.read_excel('score.xlsx', index_col='app_name')


########## 1. UPDATE NaN DATA 
# NaN is empty data

#1) use fillna to update NaN 
df.fillna('')           #result: NaN data will be filled in with ' '
df.fillna('none')       #result: NaN data will be filled in with 'none'
df                      #result: 'none' will be back to 'NaN'. inplace=True needs to be added
df.fillna('checking', inplace=True)    #if df is run again, NaN will be showing as checking

#2) imagine school columns are all updated as NaN
import numpy as np
df['school'] = np.nan       #result: all data under column 'school' will be showing as NaN.

#3) now that entire data under 'school' column and few under 'sw' column show NaN
df['sw'].fillna('no_info')  #result: only NaN cells under 'sw' column will be updated as no_info
df['sw'].fillna('no_info', inplace=True)      #remember to add inplace=True to implement the change!


########## 2. DROP NaN DATA 
#1) drop entire row
df.dropna()             #result: entire row, containing NaN will be removed (in this case, N4 and N5 rows)

#2) options for dropna
#axis: index or columns --> will you remove entire row(reffering to index?) or column?
#how: any or all        --> will you remove if any cell is NaN? or remove if all cells are NaN?

#3) applying dropna options
df.dropna(axis='index', how='any')  #result: N4, N5 rows will be removed
df.dropna(axis='columns')           #result: 'sw' column will be removed. DEFAULT is how='any'!
  
  
