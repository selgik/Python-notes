#note029_save_image.py
#prepare libraries and settings

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Batang'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

x=[1,2,3]
y=[2,4,8]


########## 1. SAVEFIG
#1) file will be saved under jupyter notebook
plt.plot(x,y)
plt.savefig('graph.png')


########## 2. DPI
#1) dpi can be assigned for saved file
plt.plot(x,y)
plt.savefig('graph.png', dpi=100)

#2) if dpi was set before saving, size/dpi will be inherited to saved file
plt.figure(dpi=200)
plt.plot(x,y)
plt.savefig('graph_200.png')

#3) show with dpi A, but saved with dpi B
plt.figure(dpi=200)
plt.plot(x,y)
plt.savefig('graph_200.png', dpi=100)

  
