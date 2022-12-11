#exercise004.py
#prepare libraries and settings

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'verdana'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

data = {
    'movie' : ['Myeong', 'Guk', 'Sin', 'Guk', 'Geoi', 'Do', 'Chil', 'Am'],
    'year' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
    'audience' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (unit : 10K)
    'rate' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}
df = pd.DataFrame(data)


########## 1. Using movie data, create a bar chart with x-axis as movie title and y-axis as rate
plt.bar(df['movie'], df['rate'])


########## 2. Using the graph from 1, apply below details:
## add title: Top 8 Movie in Korea
## add x-label as 'movie' and rotate ticks(label) 90 degrees
## add y-label as 'rate'
plt.bar(df['movie'], df['rate'])
plt.title('Top 8 Movie in Korea')
plt.xlabel('Movie')
plt.xticks(rotation=90)
plt.ylabel('Rate')


########## 3. Create a line chart of rate change over time (year) 
## calculate average rate per year:
df_group = df.groupby('year').mean()

##1) My version
rate1 = df_group['rate']
year1 = df['year']                  #error note: plt.plot(df_group['year'], df_group['rate']) did not work. Why? Because year is index, not column.
                                                 #so I tried to obtain year separately via df['year']
year1 = list(dict.fromkeys(year1))  #error note: plt.plot(year1, rate1) gave another error as there are 8 items under year1, and 7 under rate1
                                                 # so I tried to match item numbers. With this code, I obtained unique item from year1
year1.sort()                        #error note: without sort(), unique list of year1 from prev line will not be ordered ASC
plt.plot(year1, rate1)

##2) Instructor's version
plt.plot(df_group.index, df_group['rate'])


########## 4. Using the graph from 3, add below details:
## add marker 'o'
## adjust x-ticks so that it can only show year as 2005, 2010, 2015, 2020
## adjust y-ticks so that it can only show from rate 7 to 10
plt.plot(df_group.index, df_group['rate'], marker='o')
plt.xticks([2005, 2010, 2015, 2020])
plt.ylim(7, 10)


########## 5.Create a pie chart showing the rate of movies above>= 9 
## add label to show which portion is above>= 9 
## show percentage for each portion
## add legend on the right side of the chart

##1) My version
above_9 = df.loc[df['rate']>=9, 'movie']
below_9 = df.loc[df['rate']<9, 'movie']
prate = [above_9.count(), below_9.count()]
lbs = ['Above Rate 9.0', 'Below Rate 9.0']
plt.pie(prate, labels=lbs, autopct='%.1f%%')
plt.legend(loc=(1.2, 0.3))
plt.show()

##2) Instructor's version
filt = df['rate'] >= 9.0
values = [len(df[filt]), len(df[~filt])]
lbs = ['Above Rate 9.0', 'Below Rate 9.0']
plt.pie(values, labels=lbs, autopct='%.1f%%')
plt.legend(loc=(1, 0.3))
plt.show()

  
