#note015_series.py

########## 1. SERIES
# Series: one dimensional data(ex. list)
# Pandas: data analysis library in Python

#1) Create Series object
# usingl list, create 1 dimensional data -> Series.
import pandas as pd
temp = pd.Series([-20, -10, 10, 20])
temp   # in Jupyter Notebook, you don't have to use print(temp)

#result:
# 0   -20
# 1   -10
# 2    10
# 3    20

# check value using index
temp[0]   #result is -20

#2) Creat Series object and assign index
temp = pd.Series([-20, -10, 10, 20], index = ['Jan', 'Feb', 'Mar', 'Apr'])

#result:
# Jan   -20
# Feb   -10
# Mar    10
# Apr    20

# check value using index
temp['Jan']  #result is -20

