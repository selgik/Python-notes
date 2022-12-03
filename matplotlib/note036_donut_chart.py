#note036_donut_chart.py
#prepare libraries and settings

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Batang'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False


########## 1. DONUT CHART BASIC
#1) start from pie chart -> add wedgeprops parameter -> donut chart is created
values = [30, 25, 20, 13, 2, 10]    
lbs = ['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'ETC']
wgp = {'width': 0.2}      #this is ring's size. 0.2 --> thinner ring than 0.6
plt.pie(values, labels = lbs, autopct = '%.1f%%', startangle=90, counterclock=False, explode=expl, wedgeprops = wgp)


########## 2. PROBLEM WITH DONUT CHART
#1) problem 
#a. part's portion does not seem to match (height mismatch)
#b. labels overlap with each other
#c. labels are placed near the circle's line

#2) solution to a.
#instead of using explode parameter, assign color border to white color to hide border mismatch issue
wgp = {'width': 0.6, 'edgecolor':'w', 'linewidth':2}    #adjust linewidth depending on how far you want to place parts 
plt.pie(values, labels = lbs, autopct = '%.1f%%', startangle=90, counterclock=False, wedgeprops = wgp)

#3) solution to b.
#create a function to show only meaningful labels (ex. higher than 10%) 
def custom_pct(pct):
  return ('%.1f%%' % pct) if pct >= 10 else ''          #based on pct info, return %.1f%%

plt.pie(values, labels=lbs, autopct = custom_pct, startangle=90, counterclock=False, wedgeprops = wgp)

#same function but written differently:
def custom_pct(pct):
  return '{:.1f}%' .format(pct) if pct >+10 else

plt.pie(values, labels=lbs, autopct = custom_pct, startangle=90, counterclock=False, wedgeprops = wgp)

#4) solution to c.
#add pctdistance parameter
def custom_pct(pct):
  return ('%.0f%%' % pct) if pct >= 10 else ''    

plt.pie(values, labels=lbs, autopct = custom_pct, startangle=90, counterclock=False, wedgeprops = wgp, pctdistance=0.7)

  
