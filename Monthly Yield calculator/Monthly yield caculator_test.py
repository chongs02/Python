
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import xlrd
import os
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_html(r"C:\Users\chongs\Monthly Yield calculator\V6\Z_SGS_ANALYSIS_PATTERN.html", skiprows = 2)[0]

col_name = pd.read_html(r"C:\Users\chongs\Monthly Yield calculator\V6\Z_SGS_ANALYSIS_PATTERN.html")[2]

col1 = col_name.iloc[0,:]
col2 = col_name.iloc[1,:]
col2.iloc[4:] = col1.shift(+2)   
df.columns = col2.values
df = df.astype(str).apply(lambda x: x.str.replace(".","").str.replace(",","."))
df.iloc[:,4:] = df.iloc[:,4:].convert_objects(convert_numeric=True)
df


# In[155]:


df.iloc[:,9]=df.iloc[:,9].astype(float)


# In[137]:


cl = ['R024Glass Cons. in F.P','R124Good Prod.','Qual. Prod.','Q122Rework A', 'Scraps', 'Scrap Float','Scraps rework','Labour hours', 'C005Working Hours', 'C10xDowntime Hours']
dfp = df.pivot_table(values=cl, index=['Workcenter','Window family'], aggfunc=np.sum).reindex(cl,axis = 1)


# In[139]:


df_back = dfp.xs('backlite',level='Window family')[['R024Glass Cons. in F.P','R124Good Prod.','Qual. Prod.','Q122Rework A', 'Scraps', 'Scrap Float','Scraps rework','Labour hours', 'C005Working Hours', 'C10xDowntime Hours']]
df_roof = dfp.xs('multi-panels 2 (back',level='Window family')[['R024Glass Cons. in F.P','R124Good Prod.','Qual. Prod.','Q122Rework A', 'Scraps', 'Scrap Float','Scraps rework','Labour hours', 'C005Working Hours', 'C10xDowntime Hours']]


# In[142]:


def total_input(a, b):
    try :
        ans = (-1)*a - b
    
    except:
        
        ans = None
        print('error occured')
    return ans

   
df_back['Total_input'] = df_back.apply(lambda row: total_input(row['R024Glass Cons. in F.P'], row['Scrap Float']), axis=1)


def prod_q(a, b, c):
    try:
        ans = a-b-c
        
    except:
        ans = None
        print('error occured')
        
    return ans

df_back['Current_q'] = df_back.apply(lambda row: prod_q(row['Qual. Prod.'], row['Q122Rework A'], row['Scraps rework']), axis = 1)
df_back['Good_q'] = df_back['Current_q']*75/100


# In[143]:


df_back


# In[144]:


#Backlite yield Dataframe

