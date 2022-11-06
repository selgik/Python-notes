#note028_style.py
#prepare libraries and settings

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Batang'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

x=[1,2,3]
y=[2,4,8]


########## 1. MARKER
#marker: datapoint
#marker shape options: https://matplotlib.org/stable/api/markers_api.html

#1) types of marker
plt.plot(x,y, marker='o')     #marker will show circle
plt.plot(x,y, marker='v')     #marker will show triangle, similarly looking as an arrow

#2) markersize
plt.plot(x,y, marker='X', markersize=10)  #marker size will be bigger

#3) markeredgecolor (marker's surrounding color)
plt.plot(x,y, marker='o', markersize=10, markeredgecolor='red')

#4) markerfacecolor (marker's filling color)
plt.plot(x,y, marker='o', makersize=10, markeredgecolor='red', markerfacecolor='yellow')


########## 2. LINE 
#line style options:https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html

#1) linewidth 
plt.plot(x,y, linewidth=5)        #line is thicker

#2) no line
plt.plot(x,y, marker='o', linestyle='None') #no line but marker only

#3) linestyle
plt.plot(x,y, linestyle =':')     #instead of default line, dot will show 
plt.plot(x,y, linestyle ='--')    #instead of default line, -- style line will show
plt.plot(x,y, linestyle ='-.')    #instead of default line, -. style line will show
plt.plot(x,y, linestyle ='-')     #if you want default line, use this or simply remove linestyle part

#4) color
#blue is dafault line color
#color options: https://matplotlib.org/stable/gallery/color/named_colors.html

plt.plot(x,y, color='pink')
plt.plot(x,y, color='#ff0000')    #HEX format works
plt.plot(x,y, color='b')          #assigned color alias also works


########## 3. GRAPH: OPACITY, COLOR
#1) change opacity: this will apply to both line and marker
#when to use: if there are many lines and you want to emphasize one out of others
plt.plot(x,y, marker='o', alpha=0.3)  

#2) background color
plt.figure(facecolor='yellow')
plt.plot(x,y)

#google HEX color and add
plt.figure(facecolor='#03c2fc')
plt.plot(x,y)


########## 4. GRAPH: SIZE, DPI
#1) change graph size
plt.figure(figsize=(10,5))    #width:10, height:5
plt.plot(x,y)

#2) as-if-zoom effect: dpi, dots per inches
plt.figure(figsize=(10,5), dpi=200)
plt.plot(x,y)


########## 5.FORMAT
#adding various arguments may end up in long code. There are alias.
#1) color marker linestyle
plt.plot(x,y,'ro--')             #result: red line with circle marker, -- line
plt.plot(x,y,'bv:')              #result: blue line with triangle shape marker, dot line
plt.plot(x,y,'go')               #result: green line with circle marker. No linestyle

#2) alias
#find alias: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

plt.plot(x,y, marker='o', mfc='red', ms=10, mec='blue', ls=':')
#mfc: markerfacecolor, ms: markersize, mec: markeredgecolor, ls: linestyle


