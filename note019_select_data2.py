# note020_select_data2.py

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


########## 4. SELECT COLUMN(condition)
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='app_name')
df

#1) syntax
df['height']>=185     #result: index coulmn, boolean result will show by checking whether the height is >= 185

#2) variable can also be created using condition
#be aware, 'filter' cannot be the name of variable as it is python in-function

filt = (df['height']>=185)
df[filt]                      #result: corresponding data where height >=185 will only be brougt in
df[~filt]                     #result: reversed from prev one. Data wehre height >= 185 is False will only be brought in
df[df['height']>=185]         #result: works exactly the same as df[filt]
df[df['height']>=185, 'math'] #result: from filtered data, only math columns will show with index column
                              #        works exaclty the same as df[filt, 'math']
df.loc[filt, ['name', 'math']]         # from filtered data, only name and math columns will show with index column

#3) using operators
#And: &
#multiple & can be added

df.loc[(df['height']>=185) & (df['school'] == 'Buk')]
df[(df['height']>=185) & (df['school'] == 'Buk')]
df[filt & (df['school'] == 'Buk')]      
#all 3 will show the same results. Those with height>=185 and school=Buk.

#Or: |

df.loc[(df['height']<=170) | (df['height']>=200)]
df[(df['height']<=170) | (df['height']>=200)]   
# all 2 will show the same results. Those either with height <=170 or >=200


########## 5. SELECT COLUMN(str functions)
#1) use str functions
filt2 = df['name'].str.startswith('Song')
df[filt2]           # all data where name = Song will be brougt in

filt2 = df['name'].str.contains('ng')
df[filt2]           # all data where name contains 'ng' will be brougt in
df[~filt2]          # all data where name does not contains 'ng' will be brougt in

#2) use str functions with variable 
langs = ['Python', 'Java']
filt2 = df['sw'].isin(langs)
df[filt2]           # all data where sw is Python or Java will be brougt in

langs = ['python', 'java']
filt2 = df['sw'].str.lower().isin(langs)
df[filt2]           #all data where sw is Python, PYTHON or Java will be broguht in

filt2 = df['sw'].str.contains('Java')
df[filt2]           #gives an ERROR. Why? because there are empthy, NaN data

#3) how to handle NaN data
#first, let's check whether there is NaN data
df['sw'].str.lower() #while all data will be in lower cases, there will be 'NaN' containing capital letters.

#next, let's see why error was showing up
df['sw'].str.lower().isin(langs)  #result: boolean results --> showing True or False --> will give no error.
df['sw'].str.contains('Java')     #result: boolean results --> showing True, False or NaN --> that's why error.

#hence, we need to decide how to treat NaN data
df['sw'].str.contains('Java', na=False)       # NaN data will be treated as False data
filt2 = df['sw'].str.contains('Java', na=False)
df[filt2]


### for more str function, check out: https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html
  

