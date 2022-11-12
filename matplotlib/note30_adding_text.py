#note30_adding_text.py
#prepare libraries and settings

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Batang'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

x=[1,2,3]
y=[2,4,8]


########## 1. ADD TEXT (BASIC)
#syntax: plt.text(x,y,s) where x, y = float values, position to place the text and s is string
plt.plot(x,y)
plt.text(2,4,'important', fontsize=8)   #result: text will appear in the place of x=2, y=4 with fontsize 8


########## 2. ENUMERATE
#1) scneario: I want to add text right next to the marker (where x value and y value meets)
plt.plot(x,y,marker='o')
for idx, txt in enumerate(y):
    plt.text(x[idx], y[idx], txt)       #result: 2,4,8 will apear right next to marker
  
#2) because text is not very visible (as it is covered by marker and line), let's move the text
plt.plot(x,y,marker='o')
for idx, txt in enumerate(y):
    plt.text(x[idx], y[idx]+0.3, txt, ha='center', color='blue')    #ha: horizontal alignment

#3) how looping in enumerate() works:
grocery = ['bread', 'milk', 'butter']
#3-1)
for item in enumerate(grocery):
    print(item)                          #result: (0, 'bread') (1, 'milk') (2, 'butter')         
#3-2)
for count, item in enumearte(grocery):
    print(count, item)                    #result: 1 bread  1 milk  2 butter
#3-3)
for count, item in enumerate(grocery,100):
    print(count, item)                    #result: 100 bread  101 mil   102 butter
    
    
# ref:https://www.programiz.com/python-programming/methods/built-in/enumerate

  
