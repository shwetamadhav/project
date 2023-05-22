#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[6]:


df = pd.read_csv('Diwali Sales Data.csv', encoding = 'unicode_escape')


# In[7]:


df.shape


# In[8]:


df.head()


# In[9]:


df.info()


# In[12]:


#Drop unrelated/blank columns
df.drop(['Status','unnamed1'],axis=1, inplace=True)


# In[13]:


#checcking columns are droped or not
df.info()


# In[14]:


#check for null values
pd.isnull(df).sum()


# In[16]:


#Drop null values
df.dropna(inplace = True)


# In[19]:


#check null values droped or not
df.isnull().sum()


# In[20]:


#Chnage data type. ex- from float to integer
df['Amount'] = df['Amount'].astype ('int')


# In[21]:


#check data type changed
df['Amount'].dtypes


# In[22]:


#descirbe method returns the description of data
df.describe()


# In[23]:


#Use describe for specific columns
df[['Age','Orders','Amount']].describe()


# # EXPLORATORY DATA ANALYSIS

# In[25]:


df.columns


# # Gender

# In[28]:


ax = sns.countplot(x='Gender', data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[32]:


sales_gen = df.groupby(['Gender'], as_index= False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Gender', y='Amount', data = sales_gen)


# From the above graph we can see that most of the buyers are female and even the purchasing power of females are greater than male.

# # AGE

# In[35]:


ax = sns.countplot(x='Age Group', data=df, hue = 'Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[41]:


#Total amount vs age group
sales_age = df.groupby(['Age Group'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
ax = sns.barplot(x = 'Age Group', y = 'Amount', data = sales_age)


# From the above graph we can see that most of the buyers are of age group between 26-35 yrs female.

# # STATE

# In[42]:


df.columns


# In[51]:


# Total number of orders from top 10 states
sales_state = df.groupby(['State'], as_index = False) ['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(10)
sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x= 'State', y = 'Orders', data = sales_state)


# In[66]:


# Total amount of sales from top 10 states
sales_state = df.groupby(['State'], as_index = False) ['Amount'].sum().sort_values(by= 'Amount', ascending = False).head(10)
sns.set(rc={'figure.figsize':(15,6)})
sns.barplot(x = 'State', y= 'Amount', data= sales_state)


# From the above graph we can see that most of the total oders and total sale amount are from uttar pradesh, maharashtra and karnataka.

# # Marital Status

# In[53]:


df.columns


# In[62]:


ax = sns.countplot(x= 'Marital_Status', data = df)
sns.set(rc={'figure.figsize':(4,2)})
for bars in ax.containers :
    ax.bar_label(bars)


# In[63]:


sales_state = df.groupby(['Marital_Status','Gender'], as_index = False) ['Amount'].sum().sort_values(by = 'Amount', ascending= False)
sns.barplot(x='Marital_Status', y='Amount', hue = 'Gender', data = sales_state)


# From the above graph we can see that most of the buyers are married women and they have hight purchasing power.

# # OCCUPATION

# In[67]:


ax = sns.countplot(x= 'Occupation', data = df)
sns.set(rc={'figure.figsize':(4,2)})
for bars in ax.containers :
    ax.bar_label(bars)


# In[71]:


sales_state = df.groupby(['Occupation'], as_index = False) ['Amount'].sum().sort_values(by = 'Amount', ascending= False)
sns.set(rc={'figure.figsize':(12,8)})
sns.barplot(x='Occupation', y='Amount', data = sales_state)


# From the above graph we can see that most of the buyers are working in IT, Healthcare and avation sector.

# # Product category

# In[75]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(x= 'Product_Category', data = df)
for bars in ax.containers :
    ax.bar_label(bars)


# In[77]:


sales_state = df.groupby(['Product_Category'], as_index = False) ['Amount'].sum().sort_values(by = 'Amount', ascending= False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x='Product_Category', y='Amount', data = sales_state)


# From above graph we can see that most of the sold products are from food clothing and electronics.

# In[79]:


sales_state = df.groupby(['Product_ID'], as_index = False) ['Orders'].sum().sort_values(by = 'Orders', ascending= False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x='Product_ID', y='Orders', data = sales_state)


# # CONCLUSION

# Married womens age group 26-35 yrs from UP, Maharashtra and Karnataka working in IT, Healthcare and Aviation sector are more likely to buy productsfrom food, clothing and electronics category.
