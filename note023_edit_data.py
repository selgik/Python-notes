#note023_edit_data.py

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


########## 1. EDIT VALUES UNDER THE COLUMN
#1) replace values
df['school'].replace({'Buk':'Sang', 'Nong':'Rand'})   #result: changes will be shown but if you run df again, values will be back to original. 
df['school'].replace({'Buk':'Sang'}, inplace=True)    #result: Buk under school will be changed to Sang

#2) add string values to existing data
df['school'] = df['school']+'_High' # values under school columns will be added _High

#3) change to upper/lower case
df['sw'].str.upper()              #temporal change view will be shown, updating values to upper cases
df['sw'].str.lower()              #temporal change view will be shown, updating values to lower cases
df['sw'] = df['sw'].str.lower()   #direct changes will be made


########## 2. ADD COLUMNS
df['sum'] = df['kor'] + df['eng'] + df['math'] + df['phy'] + df['socio']    # create new column sum, using existing values
df['result'] = 'Fail'                     #let's create a new column result and fill in with 'Fail' data
df.loc[df['sum']>400, 'result'] = 'Pass'  #from filtered data where sum>400, update result value to 'Pass'


########## 3. REMOVE COLUMNS
df.drop(columns='sum')
df.drop(columns='sum', inplace=True)  #only with this, data frame will be permanently updated
df.drop(columns=['sum', 'result'])


########## 4. REMOVE ROWS
#1) removing values referencing index
df.drop(index='N4')  

#2) if index# is unclear, find it step by step
filt=df['math']<80              #create filter to set criteria for removing data
df[filt]                        #apply filter to the data frame
df[filt].index                  #find index for filtered data
df.drop(index=df[filt].index)   #remove rows having relevant index


########## 5. ADD ROWS
df.loc['N9'] = ['Lee', 'Hae', 184, 90, 90, 90, 90, 90, 'Kotlin', 450, 'Pass']   #add as list


########## 6. EDIT CELL
df.loc['N4', 'sw'] = 'Python'
df.loc['N5', ['school', 'sw']] = ['Nong', 'C']


########## 7. CHANGE COLUMN'S ORDER
# Let's say, I want to see 'result' column right next to the index for easier reference.

#1) let's first check the column's order
cols = list(df.columns)
cols 

#2) I want 'result' column in the form of the list
[cols[-1]]                       #result: ['result']

#3) let's reorganize columns' order
df = df[[cols[-1] + cols[0:-1]]   #result: data frame with 'result' columns right next to the index with rest columns per original order.
        

########## 8. CHANGE COLUMN'S NAME
df.columns    #result: Index(['result', 'name', 'school', ...'sum'], dtype='object')
df.columns = ['P/F', 'name', 'school', ...'sum']

        
