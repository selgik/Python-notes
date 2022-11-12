#note31_multiple_data.py
#prepare libraries and settings

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Batang'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False


########## 1. MULTIPLE DATA 
#1) multiple data will result in multiple lines in the graph
days = [1,2,3]
bread = [2,4,8]
milk = [5,1,3]
butter = [1,2,5]

plt.plot(days, bread)
plt.plot(days, milk)
plt.plot(days, butter)

#result: three lines colored blue, green, orange in one graph.
#comment: it is hard to read as graph does not explain which one is reffering to which.

#2) adding legend to the chart for easier reference
plt.plot(days, bread, label='bread')
plt.plot(days, milk, label='milk', marker='o', ls='--')
plt.plot(days, butter, label='butter', marker='s', ls='-.')
plt.legend()

#result: legend on the top left cornder, one line per line. Line styles have been updated as well.
#comment: Imagine we have 4-5 more data to put. Legend will keep longer and it may cover the graph.

#3) editing legened so that we can utilize the empty space
plt.plot(days, bread, label='bread')
plt.plot(days, milk, label='milk', marker='o', ls='--')
plt.plot(days, butter, label='butter', marker='s', ls='-.')
plt.legend(ncol=3)  #ncol: how many columns do you want to show in the legend?

#result: all information about legend is in the 1 line.
#comment: no risk of legend covering graph.

  
