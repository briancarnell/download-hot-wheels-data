#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_html("https://hotwheels.fandom.com/wiki/List_of_2022_Hot_Wheels")


# In[10]:


df = (df[0])


# In[11]:


df


# In[12]:


df.columns


# In[ ]:




