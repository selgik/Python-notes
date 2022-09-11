#note017_save_open_fies.py

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


########## 1. SAVE INTO CSV/TXT/XLSX
#1. Save into csv file 
df.to_csv('score.csv')
df.to_csv('score.csv', encoding = 'utf-8-sig')  # to prevent some characters from breaking down (i.e. Korean characters) can add encoding.
df.to_csv('score.csv', index = False)   # save without index 

#2. Save into txt file 
df.to_csv('score.txt', sep='₩t')  # separated with tab, tsv format

#3. Save into excel file 
df.to_excel('score.xlsx')


########## 2. READ(OPEN) CSV/TXT/XLSX
#1. Open csv file 
df = pd.read_csv('score.csv')
df = pd.read_csv('score.csv', skiprows=1)           # skip designated number of rows: 1. 
                                                    #   First row is header. Hence, header will be skipped.
                                                    #   From 'Chae Buk 197 90 85 100 95 85 Python' will show up.
df = pd.read_csv('score.csv', skiprows=[1,3,5])     # skip designated rows. Remember rows start from 0
                                                    #   Rows having name = Chae(1st), Song(3rd), Seo(5th) will be skipped. 
df = pd.read_csv('score.csv', nrows=4)              # bring 4 rows only
                                                    #   Rows having name = 'Chae', 'Jung', 'Song', 'Seo' will be shown.
df = pd.read_csv('score.csv', skiprows=2, nrows=4)  # skip first 2 rows and then bring next 4 rows
                                                    #   Rows having name = 'name', 'Chae' will be skipped. 
                                                    #   Rows having name = 'Jung' (becoming header), 'Song', 'Seo', 'Kang' 'Byun' will be shown.

#nrows will assume the 1st row as header, hence it will bring next n rows.

#2. Open txt file 
df = pd.read_csv('score.txt', sep='₩t')
df = pd.read_csv('score.txt', sep='₩t', index_col = 'app_name') # if you don't want to have 0-7 index, assing new index column.
df = pd.read_csv('score.txt', sep='₩t')   # this is just another way of setting an index
df.set_index('app_name', inplace=True)

#3. Open xlsx file 
df = pd.read_excle('score.xlsx')
df = pd.read_excel('score.xlsx', index_col = 'app_name')

  
