# note018_check_data.py

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
df = pd.DataFrame(data)
df.index.name = 'app_name'


########## 1. CHECKING DATAFRAME'S DATA 
#1) Get summary data: describe() provides summary of numeric data per column.
# result contains count/mean/std/min/25%/50%/75%/max value for height, kor, eng, math, phy, socio columns.
df.describe()   

#2) Get information of columns: info() provides RangeIndex, # of columns, column names, non-null count, datatype and memory usage.
# for Dtype, object is string values and int64 is integer value.
df.info()

#3) Get data for the first n rows (default is 5)
df.head()
df.head(7)

#4) Get data for the last n rows (default is 5)
df.tail()
df.tail(3)

#5) Get data per row (in the format of the list)
# result ex: array([['N1', 'Chae', 'Buk', 197, 90, 85, 100, 95, 85, 'Python'], ...])
df.values

#6) Get information about index
# result: Index(['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8'], dtype='object', name='app_name')
df.index

#7) Get information about the columns
# result: Index(['name', 'school', 'height', 'kor', 'eng', 'math', 'phy', 'socio', 'sw'], dtype='object')
df.columns

#8) Get size of the dataset
# result: (8,9) ---> 8 rows x 9 columns
df.shape


########## 2. CHECKING SERIES' DATA
#1) Get column's data using series
df['name']

#2) Get column's summary data
# if column's dtype is object, count/unique/top/freq will show up.
# if coulmn's dtype is int64(or float64), count/meanstd/min/25%/50%/75%/max will show up.  
df['name'].describe()

#3) Direclty check the column's statistic
df['height'].min()
df['height'].nlargest(3)  #show top3 data in height column
df['height'].sum()        #show sum of data in height column
df['sw'].count()          #count excluding null values. (ex. NaN: not a number, null value --> will be excluded)
df['school'].unique()     #unique value will show up --> result: array(['Buk', 'Nong'], dtype=object)
df['school'].nunique()    #number of unique value will show up

  
