#note027_label&legend.py
#prepare libraries and settings

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Batang'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

x=[1,2,3]
y=[2,4,8]


########## 1. LABEL FOR TITLE
plt.plot(x,y)
plt.title('Line Chart', fontdict={'family':'DejaVu Sans', 'size':20})   #result: title size and style will be updated


########## 2. LABEL FOR AXIS
#1) adding label to x and y axis (default color=black, position: middle)
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')    

#2) change label color (either in word or HEX format)
plt.plot(x,y)
plt.xlabel('X-axis', color='red')
plt.ylabel('Y-axis', color='#00aa00')  # this will show as green color

#3) change lable location 
plt.plot(x,y)
plt.xlabel('X-axis', color='red', loc='right')    #option: left, center, right
plt.ylabel('Y-axis', color='#00aa00', loc='top')  #option: top, center, bottom

#4) assign ticks 
# by default: x-axis was showing as 1.0, 1.5, 2.0, 2.5, 3.0 and y-axis as 2,3,4,5,6,7,8
# after assignig ticket: x-axis will show 1,2,3 and y-axis as 3,6,9,12
plt.plot(x,y)
plt.xticks([1,2,3])
plt.yticks([3,6,9,12])
plt.show()


########## 3. LEGEND
#1) legend for the line
plt.plot(x,y, label='change over time')
plt.legend()  #without this, no legend will show 

#2) change legend's location (by default: best, usually upper-left)
#possible options: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
plt.plot(x,y, lable='change over time')
plt.legend(loc='upper right')

#3) assign legend's location manually (between 0-1)
# so in below example, legend will start in the exact middle and continue towards the upper-right side.
plt.plot(x,y, label='change over time')
plt.legend(loc=(0.5, 0.5))

   
