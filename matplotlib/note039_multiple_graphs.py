#note039_multiple_graphs.py
#prepare libraries and settings

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Batang'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

import pandas as pd
df = pd.read_excel('../Pandas/score.xlsx')

                   
########## 1. SUBPLOTS
#ref: Creating multiple subplots using plt.subplots -> stacking subplots in two directions
#link: https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html 

#1)creating mulitple subplots
#2,3 will generate 2x3=6 graphs: 2 in row level and 3 in column level
fig, axs = plt.subplots(2,3, figsize=(15,10))
fig.subtitle('Creating multiple graphs')

#2)which one is which?
fig, axs = plt.subplots(2,2, figsize=(15,10))
fig.subtitle('Creating multiple graphs')
#a. axs[0,0]: top left graph
#b. axs[0,1]: top right graph
#c. axs[1,0]: bottom left graph
#d. axs[1,1]: bottom right graph


########## 2. ADDING GRAPHS TO EACH SECTIONS
fig, axs = plt.subplots(2,2, figsize=(15,10))
fig.subtitle('Creating multiple graphs')

#1st graph: bar chart
axs[0,0]. bar(df['name'], df['kor'], label='kor score')
axs[0,0]. legend()                                      #this is still needed for legend to be shown
axs[0,0]. set_title('1st graph')                        #plt.title() will not work for subplot()
axs[0,0]. set(xlabel='name', ylabel='score')            #x-axis' and y-axis' label 
axs[0,0]. set_facecolor('lightyellow')
axs[0,0]. grid(linestyle='--', linewidth=0.5)          

#2nd graph: multiple line chart
axs[0,1]. plot(df['name'], df['math'], label='math score')
axs[0,1]. plot(df['name'], df['eng'], label='eng score')
axs[0,1]. legend()

#3rd graph: horizontal bar chart
axs[1,0]. barh(df['name'], df['height'])

#4th graph: line chart
axs[1,1]. plot(df['name'], df['socio'], color='green', alpha=0.5)

    
