#!/usr/bin/env python
# coding: utf-8

# # Pandas
# Data analysis library in Python

# In[1]:


import pandas as pd


# # 1. Series
# 1 dimensional data (int, real, string)

# ## Create series object
# ex) Avg temperature from Jan to Apr (-20, -10, 10, 20)

# In[6]:


temp = pd.Series([-20, -10, 10, 20]) #using list, created 1 dim data
temp                                 #don't have to write as print(temp)


# In[7]:


temp[0] #Jan temp


# # Create series object (assign index)

# In[9]:


temp = pd.Series([-20, -10, 10, 20], index = ['Jan', 'Feb', 'Mar', 'Apr'])
temp


# In[11]:


temp['Jan'] #this is how we can check now: show data for index Jan


# In[14]:


# temp['May'] ---> this will give error as we don't have May index 

