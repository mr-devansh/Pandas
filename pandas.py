#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:





# In[2]:


d = pd.read_csv('car-sales.csv')
d


# ## ATTRIBUTES

# In[3]:


d.dtypes


# In[4]:


d.columns


# In[5]:


d.index


# In[ ]:





# ## FUNCTIONS

# In[6]:


d.describe()


# In[7]:


d.info()


# In[8]:


d.mean()


# In[9]:


d.sum()


# In[10]:


d["Doors"].sum()


# In[11]:


len(d)


# ## VIEWING AND SELECTION

# In[12]:


d.head()


# In[13]:


d.tail()


# In[14]:


animals = pd.Series(["a","b","c","d"],index=[2,4,2,8])
animals


# In[15]:


# index
animals.loc[2]


# In[16]:


# position
animals.iloc[3]


# In[17]:


animals.iloc[:3]


# In[18]:


d.loc[:3]


# In[19]:


# same thing as d.Make
# better
d["Make"]


# In[20]:


# same thing as d["Make"]
d.Make


# In[21]:


d[d["Make"]=="Toyota"]


# In[22]:


d[d["Odometer (KM)"]>100000]


# In[23]:


pd.crosstab(d["Make"], d["Doors"])


# In[27]:


d.groupby(["Make"]).mean()


# In[28]:


d["Odometer (KM)"].plot()


# In[29]:


d["Odometer (KM)"].hist()


# In[ ]:


# removing dollar sign and converting into int
d["Price"] = d["Price"].str.replace('[\$\,\.]', '').astype(int)


# In[36]:


d.head()


# In[37]:


d["Price"].hist()


# ## MANIPULATION

# In[41]:


# lowering string
d["Make"] = d["Make"].str.lower()
d


# In[46]:


# managing missing data
d_missing = pd.read_csv("car-sales-missing-data.csv")
d_missing


# In[55]:


# adding mean at the null values
d_missing["Odometer"].fillna(d_missing["Odometer"].mean(),inplace=True)
d_missing


# In[63]:


# to drop na rows from raw csv
d_missing = pd.read_csv("car-sales-missing-data.csv")
d_missing_dropped = d_missing.dropna()
d_missing_dropped


# In[64]:


# exporting csv 
d_missing_dropped.to_csv("car-sales-missing-dropped.csv")


# In[65]:


#adding column from series
seat_columns = pd.Series([5,5,5,5,5])
d["Seats"]=seat_columns
d


# In[67]:


d["Seats"].fillna(5, inplace=True)
d


# In[70]:


# adding column from list
fuel_economy = [7.5,9.2,5.0,9.6,8.7,4.7,6.6,3.0,4.5,1.0]
d["Average"] = fuel_economy
d


# In[75]:


d["total_fuel_used"] = d["Odometer (KM)"]/100 * d["Average"]
d


# In[77]:


#adding a column from a number
d["Wheels"]=4
d


# In[79]:


d["Insurance"]=True
d


# In[ ]:


# drop a column
d.drop("total_fuel_used", axis = 1, inplace = True)


# In[83]:


d


# In[94]:


# shuffling of data for sample collection
d_shuffled = d.sample(frac=1)
d_shuffled


# In[104]:


d_shuffled.sample(5)


# In[105]:


# back to inorder
d_shuffled.reset_index(drop=True)


# In[107]:


# apply lambda function 
d["Odometer (KM)"] = d["Odometer (KM)"].apply(lambda x:x/1.6)
d

