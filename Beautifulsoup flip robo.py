#!/usr/bin/env python
# coding: utf-8

# In[ ]:


question 1


# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[4]:


page= requests.get('https://www.imdb.com/list/ls056092300/')
page


# In[5]:


datasoup = BeautifulSoup(page.content)
datasoup


# In[ ]:


hence the response is 403 - it refers to the status as client error response


# In[15]:


from bs4 import BeautifulSoup
import requests



# In[39]:


tit= datasoup.find('div',class_="ipc-title__text")
tit


# In[ ]:





# In[ ]:


Question 2


# In[17]:


page= requests.get('https://www.patreon.com/coreyms')
page


# In[18]:


from bs4 import BeautifulSoup
import requests


# In[19]:


soup = BeautifulSoup(page.content)
soup


# In[32]:


heading=soup.find('div',class_="sc-bBHxTw iloeMK")
heading


# In[37]:


heading


# In[40]:


date=soup.find('div',class_="sc-kfPuZi doifNG")


# In[43]:


date


# In[45]:


content= soup.find('div',class_="sc-cfnzm4-0 daxSFj")


# In[47]:


content


# In[48]:


likes= soup.find('div',class_="sc-jrQzAO SLZLB")


# In[49]:


likes


# In[ ]:





# In[ ]:


Question 3


# In[51]:


page= requests.get('https://www.nobroker.in/')
page


# In[52]:


soup = BeautifulSoup(page.content)
soup


# In[56]:


housetitle=soup.find('div',class_="overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full")
housetitle


# In[54]:


location= soup.find('div',class_="flex")
location


# In[57]:


emi=soup.find('div',class_="font-semi-bold heading-6")
emi

In this case the emi also triggers the area, price


# In[ ]:


Question 4


# In[60]:


page= requests.get('https://www.bewakoof.com/bestseller?sort=popular%20')
page


# In[ ]:


from bs4 import BeautifulSoup
import requests


# In[61]:


soup = BeautifulSoup(page.content)
soup


# In[65]:


product_name=soup.find('div',class_="productNaming bkf-ellipsis")
product_name


# In[76]:


price=soup.find('div',class_="productPriceBox d-flex align-items-end  false")
price


# In[70]:


imageurl= soup.find all('div',class_="productImg")


# In[72]:


imageurl


# In[ ]:


question 5


# In[77]:


page= requests.get('https://www.cnbc.com/world/?region=world')
page


# In[78]:


from bs4 import BeautifulSoup
import requests


# In[79]:


soup = BeautifulSoup(page.content)
soup


# In[80]:


heading= soup.find('div',class_="RiverPlusCard-cardLeft")
heading


# In[ ]:





# In[82]:


quicklink= soup.find('div',class_="QuickLinks-quickLink")
quicklink


# In[ ]:


question 6


# In[83]:


page= requests.get('https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/')
page


# In[87]:


papertitle= soup.find('div',class_="article-listing")
papertitle


# In[88]:


date= soup.find('div',class_="article-date")
date


# In[89]:


author= soup.find('div',class_="article-authors")
author


# In[ ]:




