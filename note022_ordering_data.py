#note022_ordering_data.py 

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


########## 1. ORDERING DATA
#1) order per 1 column
df.sort_values('height')                      #result: sort rows per height ASC (default)
df.sort_values('height', ascending = False)   #result: sort rows per height DESC

#2) order per multiple columns
df.sort_values(['math', 'eng'], ascending = False)          #result: sort rows per math, eng columns DESC
df.sort_values(['math', 'eng'], ascending = [True, False])  #result: sort rows per math ASC, eng DESC

#3) just sort and check one column -> use Series
df['height'].sort_values(ascending=False)

#4) order per index value
df.sort_index(ascending=False)

  
