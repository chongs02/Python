
# coding: utf-8

# In[27]:


from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[92]:


#6/20 - 7/20
num_page =[]
for i in range(550000,580993):
    num_page.append(i)


# In[95]:


url = 'https://www1.president.go.kr/petitions/'


# In[100]:



urls = []
for i in range(len(num_page)):
    url = 'https://www1.president.go.kr/petitions/'+str(num_page[i])
    urls.append(url)


# In[105]:


a =[]
for i in urls:
    page = urlopen(i)

    document = page.read()
    soup = BeautifulSoup(document, 'html5lib')
    div_tag=soup.find_all('div',class_='View_write')
    
    for title in div_tag:
        a.append(title.get_text())


# In[109]:


import pandas as pd
df = pd.DataFrame(a)

df.to_csv("filename.csv", mode='w')

