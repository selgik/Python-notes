#note32_bar_chart.py
#prepare libraries and settings

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Batang'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False


########## 1. LABEL AND VALUE
#label: x-axis
#value: y-axis
#of course, you can name the list as x and y:

#1) basic
labels=['Kang', 'Seo', 'Jeong']
values=[190,187, 184]
plt.bar(labels, values)             #result: bar chart where x-axis=labels and y-axis is values

#2) add color to the bar
plt.bar(labels, values, color='g')  #result: bar color will be chaanged from blue to green

#3) assign different color to each bar
colors=['r', 'g', 'b']
plt.bar(labels, values, color=colors, alpha=0.5)    #bar colored in red, green, blue each

#4) re-shape so that bar is thinner
plt.bar(labels, values, width=0.5)


########## 2. AXIS: LIMIT, TICKS, LABELS
#1) limit the range in axis so that difference in data can be easily spotted 
plt.bar(labels, values, color=colors, alpha=0.5)
plt.ylim(175, 195)      #instead of y-axis showing 0-200, limit and show from 175 to 195

#2) rotate axis label (assume the scenario where data is too many and labels would overlap to each other)
plt.bar(labels, values, width=0.3)  #obviously, width may need to be adjusted to have all bars visible
plt.xticks(rotation=45)
plt.yticks(rotation=45)             #result: x-axis and y-axis' labels will be rotated by 45 degrees

#3) override label names
l=['Kang', 'Seo', 'Jeong']
v=[190,187, 184]
n=['n1', 'n2', 'n3']

plt.bar(l,v)
plt.xticks(l,n) #instead of showing l as x-axis, show n data. Result: n1, n2, n3 will show in x-axis

  
