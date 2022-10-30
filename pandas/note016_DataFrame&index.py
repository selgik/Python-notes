#note016_DataFrame.py

########## 1. CREATE DATAFRAME 
#DataFrame: two dimensional data (group of Series)

#1) let's create dataset using dictinoary
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
data

#2) checking value for key
data['name']    #result: ['Chae', 'Jung', 'Song', 'Seo', 'Kang', 'Byun', 'Hwang', 'Yun']

#3) create DataFrame object 
import pandas as pd
df = pd.DataFrame(data)
df    #result: neatly organized table having name/school/height/kor/eng/math/phy/socio/sw columns.

#4) accessing data
df['name']

# result:
# 0     Chae
# 1     Jung
# 2     Song
# 3     Seo
# 4     Kang
# 5     Byun
# 6     Hwang
# 7     Yun

#5) assessing data for multiple columns
df [['name', 'height', 'school']]   # result: picked column's value will be shown.

#6) assessing data for multiple columns (can change order)
df = pd.DataFrame(data, columns = ['name', 'height', 'math'])
df    # result: same as above, picked column's value will be shown.

#7) difference between #5 and #6: 
# after running #6, df will have 3 columns (name, height, math)
# so if you run #5 after #6, you will see an error msg as there will no longer be a school column in df.


########## 2. CREATE DATAFRAME (ASSIGN INDEX)
#1) create DataFrame and assign index 
df = pd.DataFrame(data, index = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8'])
df                          # result: index column will be created and inserted before 'name' column.

#2) show index values
df.index                    #result: Index(['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8'])

#3) naming the index
df.index.name = 'N-order'
df                          #result: index column will have its name as N-order


########## 3. RESET_INDEX

#1) resetting index
df.reset_index()            #result: new index will be created numbered from 0 to 7.
                            #        old index has became a new/separate colummn.
  
#2) remove old index
df.reset_index(drop=True)   #result: old index (N-order) will be removed 
df                          #result: no change. Table still contains N-order column.
                            #        drop=True simply showcases, but does not make changes to original dataset.  

#3) remove old index with inplace=True
df.reset_index(drop=True, inplace=True)
df                          #result: N-order column will be gone.


########## 4. SET_INDEX
#1) setting up an index (set column as an index)
df.set_index('name')                #result: name column will become an index, but again original dataset won't be affected.
df.set_index('name', inplace=True)  #this will make changes to original dataset.


########## 5. SORT_INDEX
# sort values in the index in ASC/DESC order.

#1) sort ASC
df.sort_index()                     #result: dataset will be sorted out per name column's ASC order.

#2) sort DESC
df.sort_index(ascending=False)      #result: dataset will be sorted out per name column's DESC order.

# above again, won't make changes to the original dataset. 
# need to use inplace=True to make changes.

