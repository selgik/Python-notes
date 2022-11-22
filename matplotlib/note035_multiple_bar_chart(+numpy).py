#note035_multiple_bar_chart(+numpy).py
#prepare libraries and settings

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Batang'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

import pandas as pd
df = pd.read_excel('../Pandas/score.xlsx')


########## 1. NUMPY
#1) basic concept
import numpy as np
np.arange(5)        #result: array([0,1,2,3,4])
np.arange(3,6)      #result: array([3,4,5])

#2) define variable and use in calculation
arr = np.arange(5)
arr+5               #result: array([5,6,7,8,9])
arr*2               #result: array([0,2,4,6,8])

#3) so why we are talking about numpy when drawing multiple bar chart?
# because we will need to manually assign x(or y) axis position to put multiple bars like below:
plt.bar(x-1, y)
plt.bar(x, y)
plt.bar(x+1, y)


########## 2. MULTIPLE BAR CAHRT
#1) prepare data, find how many rows# and columns# are there for score.xlsx
df.shape()          #result: (8, 10) meaniing, there are 8 rows and 10 columns
df.shape(0)         #result: 8

N=df.shape(0)
index=np.arange(N)  #result: array([0,1,2,3,4,5,6,7])

#2) let's draw:
w=0.25
plt.bar(index-w, df['kor'])           #result: 8 bars will show up

#3) let's draw further:
w=0.25
plt.bar(index-w, df['kor']) 
plt.bar(index, df['eng']) 
plt.bar(index+w, df['math'])          #result: bars with three colors overlaping partially; very difficult to read

#4) let's adjust:
w=0.25
plt.bar(index-w, df['kor'], width=w) 
plt.bar(index, df['eng'], width=w) 
plt.bar(index+w, df['math'], width=w)  #result: multiple bar chart (thinner in shape) placed next to each other

#5) final touch:
plt.figure(figsize=(10, 5))
plt.title('student score')

w=0.25
plt.bar(index-w, df['kor'], width=w, label='kor') 
plt.bar(index, df['eng'], width=w, label='eng') 
plt.bar(index+w, df['math'], width=w, label='math')
plt.legend(ncol=3)

plt.xticks(index, df['name'], rotation=60)
plt.show()

   
