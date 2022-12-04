#note038_scatterplot.py
#prepare libraries and settings

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Batang'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

import pandas as pd
df = pd.read_excel('../Pandas/score.xlsx')

                   
########## 1. SYNTAX
plt.scatter(df['eng'], df['math'])      #result: scatterplot with eng column's data on the x-axis, math on y-axis
plt.xlabel('eng scores')
plt.ylabel('math scores')


########## 2. ASSIGN SIZE
#1) assign different sizes for the circle
#let's add grade column (1st grade, 2nd grade, 3rd grade) to the df to use it as a guide for sizes
df['grade'] = [3,3,2,1,1,3,2,2]
sizes = df['grade']*500                 #why *500? without it, size will be too small on the graph

plt.scatter(df['eng'], df['math'], s=sizes)
plt.xlabel('eng scores')
plt.ylabel('math scores')

#2) assign random sizes for the circle
import numpy as np
s2=np.random.rand(8)                    #result: random float number between 0-0.8
s2=np.random.rand(8)*1000               #why *1000, otherwise, size of circle on the graph will be too small

plt.scatter(df['eng'], df['math'], s=sizes)
plt.xlabel('eng scores')
plt.ylabel('math scores')


########## 3. ASSIGN COLOR
#reference for the color map = https://matplotlib.org/stable/tutorials/colors/colormaps.html

#1) assign colors 
plt.scatter(df['eng'], df['math'], s=sizes, c=df['grade'], cmap='viridis')
plt.xlabel('eng scores')
plt.ylabel('math scores')

#2) adjust transparency 
#so that overlapping shapes can be seen
plt.scatter(df['eng'], df['math'], s=sizes, c=df['grade'], cmap='viridis', alpha=0.3)
plt.xlabel('eng scores')
plt.ylabel('math scores')

#3) assigning colors can be particularly helpful when there are many datapoints on the graphs
#colors can be randomly assigned too
clrs = np.random.rand(8)
plt.scatter(df['eng'], df['math'], s=200, c=clrs, cmap='viridis', alpha=0.3)
plt.xlabel('eng scores')
plt.ylabel('math scores')


########## 4. ADD COLOR BAR
#1) add color bar (color legend)
plt.figure(figsize=(7,7))               #let's adjust size of graph
sizes=df['grade']*500
plt.scatter(df['eng'], df['math'], s=sizes, c=df['grade'], cmap='viridis', alpha=0.3)
plt.xlabel('eng score')
plt.ylabel('math score')
plt.colorbar()                          #colorbar will be created on the right side with the same height of graph with ticks of 0.25

#2) adjust ticks
plt.colorbar(ticks=[1,2,3], label='grade')

#3) adjust colorbar's height
plt.colorbar(ticks=[1,2,3], label='grade', shrink=0.5)    #colorbar will be half size (height and width)

#4) adjust orientation 
plt.colorbar(ticks=[1,2,3], label='grade', shrink=0.5, orientation = 'horizontal')    #colorbar will be placed under the graph

  
