#!/usr/bin/env python
# coding: utf-8

# # Midterm
# 
# Fernando Abarca & Ryan Caro
# 
# November 3, 2020
# 
# UP 206A

# This is a description of what we are going to do

# In[1]:


#import pandas
import pandas as pd


# In[2]:


#import our data
df18 = pd.read_csv('Data/2018_Data.csv', dtype=
    {
        'Geo_FIPS':str,
        'Geo_STATE':str,
        'Geo_COUNTY': str,
        'Geo_TRACT' : str
    })


# In[3]:


#import 2010 data with help from Stack Overflow
#https://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python
df10 = pd.read_csv('Data/2010_Data.csv', encoding = "ISO-8859-1", dtype=
    {
        'Geo_FIPS':str,
        'Geo_STATE':str,
        'Geo_COUNTY': str,
        'Geo_TRACT': str
    })


# In[4]:


df18.head()


# In[5]:


df10.head()


# The encoding error might be becuase of the super long numbers in the first column. We're not sure. We're glad it works.

# In[6]:


#look at data
df18.info()


# In[7]:


#look at data
df10.info()


# In[8]:


#drop all columns where all data = n/a
df18 = df18.dropna(axis=1,how="all")
df10 = df10.dropna(axis=1,how="all")


# In[9]:


df18.info()


# In[10]:


df10.info()


# In[11]:


columns_to_drop18 = ['Geo_GEOID','Geo_STUSAB','Geo_SUMLEV','Geo_GEOCOMP','Geo_FILEID','Geo_LOGRECNO','SE_A09005_001',
                  'SE_A09005_002','SE_A09005_009',  'SE_A09005_010',  'SE_A09005_003', 'SE_A09005_004',  
                  'SE_A09005_005', 'SE_A09005_006', 'SE_A09005_007', 'SE_A09005_008', 'PCT_SE_A09005_002',
                   'PCT_SE_A09005_009','PCT_SE_A09005_010','PCT_SE_A09005_004','PCT_SE_A09005_005',
                   'PCT_SE_A09005_006','PCT_SE_A09005_007','PCT_SE_A09005_008']


# In[12]:


df18 = df18.drop(columns_to_drop18, axis = 1)


# In[13]:


columns_to_drop10 = ['Geo_GEOID','Geo_STUSAB','Geo_SUMLEV','Geo_GEOCOMP','Geo_FILEID','Geo_LOGRECNO','SE_A09005_001',
                  'SE_A09005_002','SE_A09005_009',  'SE_A09005_010',  'SE_A09005_003', 'SE_A09005_004',  
                  'SE_A09005_005', 'SE_A09005_006', 'SE_A09005_007', 'SE_A09005_008', 'PCT_SE_A09005_002',
                   'PCT_SE_A09005_009','PCT_SE_A09005_010','PCT_SE_A09005_004','PCT_SE_A09005_005',
                   'PCT_SE_A09005_006','PCT_SE_A09005_007','PCT_SE_A09005_008', 'Geo_COUSUB', 'Geo_PLACE', 'Geo_PLACESE']


# In[14]:


df10 = df10.drop(columns_to_drop10, axis = 1)


# In[15]:


df18.head()


# In[16]:


df10.head()


# We need to fix the 2010 FIPS so that it is composed of State, County, and Tract concatenated

# In[17]:


df10['Geo_FIPS'] = df10['Geo_STATE'] + df10['Geo_COUNTY'] + df10['Geo_TRACT']


# In[18]:


df10.head()


# In[ ]:




