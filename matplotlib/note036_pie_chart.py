#note036_pie_chart.py
#prepare libraries and settings

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Batang'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False


########## 1. PIE CHART BASIC
#1) syntax
values = [30, 25, 20, 13, 2, 10]    #values does not need to sum up 100. Pie chart will anyway be created proportionally.
lbs = ['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'ETC']
plt.pie(values, labels = lbs)       #labels will show up 
plt.show()

#2) add proportion %
plt.pie(values, labels = lbs, autopct = '%.1f')   #proportion will show up as: 25.0, 20.0, 13.0, 10.0, 2.0, 30.0
plt.pie(values, labels = lbs, autopct = '%.1f%%') #proportion will show up as: 25.0%, 20.0%, 13.0%, 10.0%, 2.0%, 30.0%
plt.pie(values, labels = lbs, autopct = '%.0f%%') #proportion in integer form as: 25%, 20%, 13%, 10%, 2%, 30%

#3) adding labels 
plt.pie(values, labels = lbs)    
plt.legend(loc = (1.2, 0.3))                      #label card will show on the right side of graph. Without loc, card will cover the graph.   

#4) adding titles 
plt.pie(values, labels = lbs)    
plt.title('Pie Chart for Computer Languages')      #adding title for the graph 
plt.legend(loc = (1.2, 0.3), title = 'Preference') #adding title for label card


########## 2. SETTING DIRECTION & SLICE EFFECT
#1) setting direction: first pie to start from 12 o'clock
values = [30, 25, 20, 13, 2, 10]   
lbs = ['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'ETC']

plt.pie(values, labels = lbs, startangle=90)      

#2) setting direction: show data clockwise
#without counterclock parameter, data show counterclockwise
plt.pie(values, labels = lbs, autopct = '%.1f%%', startangle=90, counterclock=False)   

#3) slice effect: to particular part
values = [30, 25, 20, 13, 2, 10]    
lbs = ['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'ETC']
expl = [0.2, 0.2, 0, 0, 0, 0]

plt.pie(values, labels = lbs, explode = expl)     #by adding explode parameter, Python and Java part will be separated (highlighted) from the rest. 

#4) slice effect: to every part
values = [30, 25, 20, 13, 2, 10]    
lbs = ['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'ETC']
expl = [0.05]*6                                   #all parts will be separated from each other

plt.pie(values, labels = lbs, explode = expl)    


########## 3. ASSIGNING COLORS 
#1) use color alis
values = [30, 25, 20, 13, 2, 10]    
lbs = ['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'ETC']
clos = ['b', 'g', 'r', 'c', 'm', 'y']

plt.pie(values, labels = lbs, autopct = '%.1f%%', startangle=90, counterclock=False, colors=clos)

#2) use HEX 
values = [30, 25, 20, 13, 2, 10]    
lbs = ['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'ETC']
clos = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', '#a0c4ff']   #pastel colors

plt.pie(values, labels = lbs, autopct = '%.1f%%', startangle=90, counterclock=False, colors=clos)


########## 4. USING DATAFRAME
import pandas as pd
df = pd.read_excel('../Pandas/score.xlsx')  #check README to view table
df.groupby('school').size()                 #result: Buk 5    Nong 3
grp = df.groupby('school')

values = [grp.size()['Buk'], grp.size()['Nong']]
lbs = ['Buk', 'Nong']

plt.pie(values, labels=lbs, startangle=90)
plt.title('School Information')
plt.show()                                  #result: Buk's portion showing 62.5% and Nong 37.5%

  
