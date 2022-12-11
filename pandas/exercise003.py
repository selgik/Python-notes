#exercise003.py 

import pandas as pd
data = {
  'title' = ['Mong', 'Kuk', 'Sin', 'Kuk', 'Qui', 'Do', 'Chil', 'Am']
  'year' = [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015]
  'audience' = [1761, 1636, 1441, 1426, 1301, 1298, 1281, 1270]
  'score' = [8.88, 9.2, 8.73, 9.16, 8.62, 7.64, 8.83, 9.1]
}
df = pd.DataFrame(data)
df

#1) Return title data
df['title']

#2) Return title and score data
df[['title', 'score']]

#3) Return title and year data where year >= 2015
filt=df['year']>=2015
df.loc[filt, ['title', 'year']]
#or below:
df.loc[df['year']>=2015, ['title', 'year']] # row selection first, and then column selection

#4) Add column named 'recommendation' based on the calculation below:
# recoommendation = (audience * score)//100
df['recommendation'] = df['audience'] * df['audience'] // 100 # this will show calculated values as integer format (xxx.0)
df['recommendation'] = df['audience'] * df['audience'] / 100  # this will show caculated values till 4th decimal places

#5) Order data by year DESC
df.sort_values('year', ascending = False)


   
