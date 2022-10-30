#note024_apply_function.py
# refer note 006 for function info

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


########## 1. CREATE FUNCTION TO MANIPULATE DATA

#1) Add string value to the integer type data
#Reminder: you want to add '_High' next to the data under the column 'school'
df['school'] = df['school'] + '_Hight'

#Now, I would like to add ' cm' next to the data under the column ' height'
df['height'] = df['height'] + ' cm'   # result: gives an error, because height is integer type and 'cm' is string.

#Let's create function to change height data to string
def add_cm(height):
  return str(height) + ' cm'

df['height'] = df['height'].apply(add_cm)
df                                    

#2) Capitalize the first letter 
def cap(lang):
  if pd.notnull(lang):
    return lang.capitalize()
  return lang

df['sw'] = df['sw'].apply(cap)
df

#Actully, above can simply be written as below:
df['sw'].str. ccapitalize()

#For permanent change, need to update as below:
df['sw'] = df['sw'].str.capitalize()

  
