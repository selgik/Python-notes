# note019_select_data1.py

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


########## 1. SELECT COLUMN(labal)
# label = column's name

import pandas as pd
df = pd.read_excel('score.xlsx', index_col='app_name')
df

#1) select column
df['name']            #result shows: index column, name column, summary of name column (Name:name, dtype: object)
df[['name', 'eng']]   #result shows: index column, name column, eng column

#2) select column from integer index
#when to use? imagine data is piling up (right columns keep adding up) reading column with ref number migt be easier.
#also, see 3rd & 4th example below. You can simply refer the column's position to get information.

df.column             #result: Index(['name', 'school', 'height', 'kor', 'eng', 'math', 'phy', 'socio', 'sw'], dtype='object')
df.column[2]          #result: 'height'
df[df.column[3]]      #result: index column, kor column
df[df.column[-1]]     #result: index column, sw column <--- use this when you need last column's info.

#3) slicing
df['eng'][0:5]        #result: index column, eng column before row N5 (85, 35, 75, 60, 20)
                      #        0th - 4th data will be brought in.
df[['name', 'height']][:3]     #result: name and height column's data will be brougth in (0th - 2nd data)
df[3:]                #result: all column's information will be brought in from 3th row (including 3th data)


########## 2. SELECT COLUMN(loc)
# (From: https://www.w3resource.com/pandas/dataframe/dataframe-loc.php)
#       The loc property is used to access a group of rows and columns by label(s) or a boolean array.
#       .loc[] is primarily label based, but may also be used with a boolean array.

#using index, select columns
#using other data will not work (ex df.loc['Chae'] gives an error)

df.loc['N1']                        #result: data assigned to N1 will be brougt in
df.loc['N1', 'kor']                 #result: 90
df.loc[['N1', 'N2'], 'eng']         #result: index column, eng column (85, 35)
df.loc[['N1', 'N2'],['kor', 'eng']] #result: index column, kor column (90, 40) and eng column (85, 35)
df.loc['N1':'N4','kor':'phy']       #result: from N1-N4, data for kor coulmn - phy column will be shown.
                                    #        when using slicing, there is no need for double spacing.
                                    #        be aware, for this slicing, latter part will be INCLUDED!


########## 3. SELECT COLUMN(iloc)
#using location, select columns

df.iloc[0]            #result: Chae's data from all columns <-- get data for 0th index
df.iloc[0:5]          #result: from Chae to Kang's data from all columns <-- exclude 5th (Byun's) data!
df.iloc[0, 1]         #result: 'Buk' <-- find data for 0th index(Chae), from 1st column position(school)
df.iloc[4, 2]         #result: 188 <-- find data for 4th index(Kang), from 2nd coulmn position(height)
df.iloc[[0,1], 2]     #result: index column, height columns (197, 184) for 0th and 1st index
df.iloc[[0,1],[3,4]]  #result: index column, kor/eng columns (90,40/85, 35) for 1th and 1st index
df.iloc[0:3, 2:5]     #result: index coulmn, height/kor/eng columns for 0th-2nd index


