#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[140]:


df = pd.read_csv(r'google_cleaned1.csv')


# In[141]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.shape


# In[10]:


# getting random sample

df.sample(5)


# In[11]:


df.info()


# In[13]:


df.isna().sum()


# In[15]:


df.describe().T


# In[16]:


df.describe(include='all')


# In[18]:


df.duplicated().sum()


# In[21]:


df[df.duplicated()]


# In[22]:


df.shape


# In[23]:


df = df.drop_duplicates()


# # 

# # Exploring the data

# segregate tha categorical and numeric feature

# In[26]:


numeric_features = [feature for feature in df.columns if df[feature].dtype != 'O']
categorical_features = [feature for feature in df.columns if df[feature].dtype == 'O']


# In[27]:


numeric_features


# In[35]:


num_df = df[numeric_features]


# In[38]:


num_df


# In[36]:


categorical_features


# In[39]:


cat_df = df[categorical_features]


# In[40]:


cat_df


# In[ ]:





# In[29]:


df['App'].value_counts()


# In[30]:


len(df['App'].value_counts())


# In[31]:


# to check in percentile

df['App'].value_counts(normalize=True)


# In[32]:


df['App'].value_counts(normalize=True)*100


# In[ ]:





# In[41]:


num_df


# check the distribition of nummeric veriables

# In[43]:


sns.kdeplot(num_df['Rating'])


# # checking the distribution of numeric feature ffor alll columns

# In[46]:




for feature in numeric_features:
    sns.kdeplot(num_df[feature])
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.title('Numercal Features')
    plt.show()


# In[53]:


plt.figure(figsize=(20,20))
plt.suptitle('Univariate Analysis of Numerical Features', fontsize=20, fontweight='bold', alpha=0.8, y=1)

for i in range(len(numeric_features)):
    plt.subplot(5,3,i+1)
    sns.kdeplot(x=df[numeric_features[i]],shade=True,color ='r')
    plt.xlabel(numeric_features[i])
    plt.tight_layout()


# In[54]:


########OBSERVATION


# In[ ]:





# In[55]:


cat_df


# In[58]:


cat_df['Type'].value_counts()


# In[61]:


cat_df[cat_df['Type']=='Paid']


# In[63]:


sns.countplot(cat_df['Type'])


# In[64]:


cat_df['Content Rating'].value_counts()


# In[65]:


sns.countplot(cat_df['Content Rating'])


# In[74]:


#categorical column

plt.figure(figsize=(8,8))
plt.suptitle('Univariate Analysis of Categorical Features', fontsize=20, fontweight='bold', alpha=0.8, y=1)
category = ['Type', 'Content Rating']

for i in range(0, len(category)):
    plt.subplot(2,2,i+1)
    sns.countplot(x=df[category[i]],palette='Set2')
    plt.xlabel(category[i])
    plt.xticks(rotation = 45)
    plt.tight_layout()


# # 

# which one is the most popular categories

# In[77]:


cat_df['Category'].value_counts()


# In[156]:


cat_df['Category'].value_counts().plot.pie(figsize = (40, 40), autopct='%1.1f%%', textprops={'fontsize': 20})


# # plot a pie chart on the besis of top 10 categories from Category columns

# In[83]:


cat_df['Category'].value_counts()


# In[85]:


category = pd.DataFrame(cat_df['Category'].value_counts())


# In[88]:


category.head(10)


# In[89]:


# changing column name Category 

category.rename(columns={'Category':'Count'},inplace=True)


# In[92]:


category.head(10)


# In[95]:


category.head(10).value_counts().plot.pie(figsize = (40, 40), autopct='%1.1f%%', textprops={'fontsize': 20})


# In[102]:


plt.figure(figsize=(20,10))

sns.barplot(x=category.index[:10], y='Count', data=category[:10])


# # 

# which categories has a largest nummber of installation 

# In[112]:




df.groupby(['Category'])['Installs'].sum().sort_values(ascending = False)


# In[113]:


df.groupby(['Category'])['Installs'].sum().nlargest()


# In[117]:


df.groupby(['Category'])['Installs'].sum().nlargest().plot.pie( autopct='%1.1f%%')


# In[116]:


df.groupby(['Category'])['Installs'].sum().nlargest().plot(kind = 'bar')


# # 

# How many Apps are there on google play store which get 5 ratings ?

# In[120]:


df['App'].value_counts()


# In[167]:


df['Rating'].value_counts()


# In[158]:


df[df['Rating']==5]


# In[182]:


apps_5_ratings = df[(df['Rating']==5)&(df['App'])]


# In[ ]:





# In[187]:


# filter the dataframe to only include rows where the rating is 5
apps_5_ratings = df[df['Rating'] == 5]

# group by the 'App' column and count the number of occurrences
counts = apps_5_ratings.groupby('App').count()['Rating']

# sort the counts in descending order and plot a bar chart
counts.sort_values(ascending=False).head().plot(kind='bar')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


does size of the application has any impact on its popularity

