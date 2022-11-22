#note33_bar_chart.py
#prepare libraries and settings

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Batang'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False


########## 1. BAR CHART
#label: x-axis
#value: y-axis
#of course, you can name the list as x and y:

#1) basic
labels=['Kang', 'Seo', 'Jeong']
values=[190,187, 184]
plt.bar(labels, values)             #result: vertical bar chart where x-axis=labels and y-axis is values
plt.barh(labels, values)            #result: horizontal bar chart where x-axis=labels and y-axis is values

#2) add color to the bar
plt.bar(labels, values, color='g')  #result: bar color will be chaanged from blue to green

#3) assign different color to each bar
colors=['r', 'g', 'b']
plt.bar(labels, values, color=colors, alpha=0.5)    #bar colored in red, green, blue each

#4) re-shape so that bar is thinner
plt.bar(labels, values, width=0.5)

#5) setting hatch (fill bar with patterns)
#hatch library ref: https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_style_reference.html
bar=plt.barh(labels, values)
bar[0].set_hatch('/')   # result: Kang's bar will be filled with /// pattern
bar[1].set_hatch('x')   # result: Seo's bar will be filled with xxx pattern
bar[2].set_hatch('..')  # result: Jeong's bar will be filled with ... pattern


########## 2. AXIS: LIMIT, TICKS, LABELS
#1) limit the range in axis so that difference in data can be easily spotted 
plt.bar(labels, values, color=colors, alpha=0.5)
plt.ylim(175, 195)      #instead of y-axis showing 0-200, limit and show from 175 to 195. This is for veritcal bar chart 
plt.xlim(175, 195)      #same as above, for horizontal bar chart

#2) rotate axis label (assume the scenario where data is too many and labels would overlap to each other)
plt.bar(labels, values, width=0.3)  #obviously, width may need to be adjusted to have all bars visible
plt.xticks(rotation=45)
plt.yticks(rotation=45)             #result: x-axis and y-axis' labels will be rotated by 45 degrees

#3) override label names
l=['Kang', 'Seo', 'Jeong']
v=[190,187, 184]
n=['n1', 'n2', 'n3']

plt.bar(l,v)
plt.xticks(l,n)                     #instead of showing l as x-axis, show n data. Result: n1, n2, n3 will show in x-axis

  
########## 3. ADD TEXT WITH ENUMERATE()
#reference on enumerate(): note30_adding_text.py
#what am I looking for: I want 190, 187, 184 to be printed right above the bar

bar=plt.bar(labels, values)
plt.ylim(175,195)
for idx, rect in enumerate(values):
    plt.text(idx, rect.get_height()+0.5, values[idx], ha='center', color='blue')   #get_height(): get height of rectangular=bar
    #       x-axis       y-axis       which data to show
    #plt.text(): need x-axis, y-axis, which data to show?

#result: 190, 187, 184 will show above the bar

     
