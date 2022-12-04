#note026_line_chart.py


########## 1. MATPLOTLIB
# what is matplotlib: a library that allows data visualization through various types of graphs

#1) let's get library first: pyplot allows to draw graph using x, y axis
import matplotlib.pyplot as plt 

#2) let's assign x,y axis and get a line chart
x = [1,2,3]
y = [2,4,8]
plt.plot(x,y)   

#or simply:
plt.plot([1,2,3], [2,4,8])

#3) let's get description of the graph (+ line chart)
print(plt.plot(x,y))

#4) hide description, just show graph only
plt.plot(x,y)
plt.show()

#5) let's add title to the graph
plt.plot(x,y)
plt.title('Line Chart')


########## 2. FONT SETTING
#1) If you enter below, title will not show (will show as blank square as letters will be broken)
plt.plot(x,y)
plt.title('라인차트')

#2) If you need to use character different from English (ex. Korean),
# or, if you need to set font properties:
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  #setting font style
matplotlib.rcParams['font.size'] = 15                 #setting font size
matplotlib.rcParams['axes.unicode_minus] = False      #when minus sign is not showing on the axis, use this

#3) If you are not too sure what to use as font.family, check avaialble font list
import matplotlib.font_manager as fm
fm.fontManager.ttflist                     # result: long and wide list of font information; difficult to read
[f.name for f in fm.fontManager.ttflist]   # result: list of font name; easier to read

#4) once font is set, let's re-try. Korean title will show up.
plt.plot(x,y)
plt.title('라인 차트')

                    
