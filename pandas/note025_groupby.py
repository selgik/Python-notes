#note025_grouping.py

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


########## 1. AGGREGATE DATA
#1) group data  
df.groupby('school')                    #no dataframe will be shown, just one line confirming the update

#2) group data -> show filtered data
df.groupby('school').get_group('Buk')   #result: filtered dataframe where school name is Buk


########## 2. AGGREGATE AND CALCULATE DATA
#1) count  
df.groupby('school').size()             #result: Buk 5 / Nong 3
df.groupby('school').size()['Nong']     #result: 3

#2) calculate average
df.groupby('school').mean()             #result: average value per school will show up where applicable (where dtype=int)
df.groupby('school')['height'].mean()   #result: Buk 184.8000 / Nong 193.3333 
df.groupby('school')[['kor', 'eng', 'math']].mean()   #get avg kor, eng, math data grouped by school


########## 3. GROUP BY 2 CRITERIA
#1) let's create new column with grade info
df['grade'] = [3,3,2,1,1,3,2,2]

#2) let's exercise
df.groupby('grade').size()              #result: 1  2 / 2 3 / 3 3
df.groupby('grade').mean()              #result: average value per grade will show up where applicable (where dtype=int)
df.groupby('grade').mean().sort_values('height')    #show average values per grade ordered by height ASC
df.groupby(['school','grade']).mean()   #get average data grouped by school and grade
df.groupby(['school','grade']).sum()    #get sum data grouped by school and grade

#3) when NaN values are included
# it will be good practice to see whether there is NaN values by comparing two sizes
# tip: size() will count NaN value but count() will not. 
df.groupby('school')['sw'].size()            # result: Buk 5 / Nong 3
df.groupby('school')['sw'].count()           # result: Buk 3 / Nong 3
df.groupby('school')[['name','sw']].count()  # result: Buk 5 3 / Nong 3 3 <-- 2 cells are NaN under 'sw' where school = Buk

#4) let's count how many students are per school and grade (3 ways)
df.groupby(['school','grade']).size()
df.groupby('school')['grade'].value_counts()

school = df.groupby('school')
school['grade'].value_counts()

#5) let's count how many students are per school and grade, where school = Buk
# .loc will only work with this code from #4
school = df.groupby('school')
school['grade'].value_counts().loc['Buk']

#6) let's calculate percentage of total using normalize()
school = df.groupby('school')
school['grade'].value_counts(normalize=True).loc['Buk']

#result:
#1  0.4
#3  0.4
#2  0.2

 
