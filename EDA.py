#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import warnings
import seaborn as sns
warnings.filterwarnings("ignore")


# In[2]:


df = pd.read_csv('covid19.csv')


# ## 1. Get an initial sniff of the data

# In[3]:


df.info()


# In[4]:


df.shape


# In[5]:


df.describe()


# In[6]:


df.head(2)


# In[7]:


df.isnull().any()


# ## 2. Initial cleaning up

# In[8]:


# check null values
df.isnull().sum()


# In[9]:


df.fillna(0, inplace=True)
df.head(5)


# In[10]:


# check negative values
df.index[df['new_cases'] < 0]


# In[11]:


df.index[df['new_deaths'] < 0]


# In[12]:


print(len(df.index[df['new_cases'] < 0]))
print(len(df.index[df['new_deaths'] < 0]))


# In[13]:


df[df['new_cases'] < 0] = 0
df[df['new_deaths'] < 0] = 0
df.head(5)


# ## 3. Visualizations

# In[14]:


fig, ax = plt.subplots(figsize=(10, 10))
sub_df = df[df.iso_code == 'USA']
sub_df['date'] = pd.to_datetime(sub_df['date'])

ax.scatter(sub_df.date, sub_df.new_cases)

# Setting title and labels
plt.title('New Covid Cases with time', size=20)
ax.set_xlabel('Date', size=15)
ax.set_ylabel('New Cases', size=15)
ax.xaxis.labelpad = 20

# Setting axis-ticks
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xticks(rotation=90)

# Removing top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()


# In[15]:


fig, ax = plt.subplots(figsize=(8, 8))
sns.heatmap(df.corr(), ax=ax, annot=True)
plt.title('Heatmap', size=20, pad=10)
plt.show()
