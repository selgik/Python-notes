#note032_use_dataframe.py
#prepare libraries and settings

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Batang'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False


########## 1. READ EXCEL
#assume excel file exists in different folder. Tell system to go to parent folder -> go to Pandas folder -> read excel file
import pandas as pd
df = pd.read_excel('../Pandas/score.xlsx')    


########## 2. SELECT LABELS AND VALUES
plt.plot(df['app_name'], df['eng'])
plt.plot(df['app_name'], df['math'])

# result: line charts with two data 
   
