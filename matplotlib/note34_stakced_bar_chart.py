#note34_stakced_bar_chart.py
#prepare libraries and settings

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Batang'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

import pandas as pd
df = pd.read_excel('../Pandas/score.xlsx')


########## 1. OVERLATPING BAR CHART
#1) overlaping bar chart
plt.bar(df['name'], df['kor'])
plt.bar(df['name'], df['eng'])    #result: orange bar in the front of blue bar (orange: eng / blue: kor)

#2) adjust width of bar on the front to easily read data
plt.bar(df['name'], df['kor'], label='kor')
plt.bar(df['name'], df['eng'], label='eng',width=0.5)  
plt.legend()                      #result: orange bar in the front is thinner. Both orange and blue are visible. 


########## 2. STACKED BAR CHART
#1) stacked bar chart
plt.bar(df['name'], df['kor'])
plt.bar(df['name'], df['eng'], bottom=df['kor'])   #result: stacked bar chart where kor data will be on the bottom.

#2) without bottom data?
plt.bar(df['name'], df['eng'], bottom=df['kor'])   #result: kor bar will be missing. It looks like stacked bar where bottom is white bar. 

#3) stacked bar chart with 2+ data
plt.bar(df['name'], df['kor'])
plt.bar(df['name'], df['eng'], bottom=df['kor'])
plt.bar(df['name'], df['math'], bottom=df['kor']+df['eng'])  #result: green, orange, blue stacked bar chart

#let's format
plt.bar(df['name'], df['kor'], label='kor')
plt.bar(df['name'], df['eng'], bottom=df['kor'], label='eng')
plt.bar(df['name'], df['math'], bottom=df['kor']+df['eng'], label='math')

plt.xticks(rotation=60)
plt.legend()

  
