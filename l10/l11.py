#!/usr/bin/env python
# coding: utf-8

# In[1]:


## dictionaries key value pair


# In[2]:


d = {'key1':'abc', 'key2':1243, 'key3':'value'}


# In[3]:


d


# In[4]:


d[key1]


# In[5]:


d['key1']


# In[6]:


d[]


# In[10]:


d['key2'][0]


# In[11]:


d['key1'][1]


# In[15]:


d={'k1':[1,2,3]}


# In[16]:


d['k1']


# In[17]:


d['k1'][1]


# In[18]:


d = {'k1':{'innerKey':[1,2,3]}}


# In[19]:


d


# In[20]:


d['k1']['innerKey'][2]


# In[21]:


d={'k1':{'innerKey1': ['a','b','c'],'innerkey2':[5,6,9,0]}}


# In[22]:


d


# In[23]:


d['innerKey2'][2]


# In[25]:


d['k1']['innerkey2'][1]


# In[26]:


## boolean 


# In[27]:


true


# In[28]:


True


# In[29]:


False


# In[30]:


## Tuples


# In[31]:


## we use parentheses in stead of square brackets in list


# In[32]:


## tuples are immutable while lists are 


# In[33]:


## that means re assiging is possible in list but not in tuples


# In[34]:


t = ('a', 'b', 'c')


# In[35]:


t[0
]


# In[36]:


t[0]= 'd'


# In[37]:


## Set is a collection of unique elemts


# In[38]:


{1,2,1,3,4,1,23,5,2,3,5,2}


# In[39]:


set([1,2,4,2,3,124,2,4,23,2,4,23,5,233,45])


# In[40]:


s = {1,2,4}


# In[41]:


s.add(5
    )


# In[42]:


s


# In[43]:


1>2


# In[44]:


1<2


# In[45]:


2 == 2


# In[46]:


1 == 2


# In[47]:


1 != 3


# In[48]:


'hi' == 'bye'


# In[49]:


# combining logical operators


# In[ ]:





# # 1 < 2 and 2 < 3

# In[51]:


1 < 2 or 3 > 4


# In[52]:


2 < 1 and 3 < 5


# In[53]:


True and True


# In[54]:


True or False 


# In[55]:


True and True or False 


# In[56]:


## if elif statements


# In[57]:


if 1<2:
    print('yep1')


# In[58]:


if 1 == 2:
    print("first")
else:
    print("second")


# In[60]:


if 1!=2:
    print("thats right")


# In[62]:


if 1 == 2:
    print('first')
elif 3 == 3:
    print('second')
elif 5 == 5:
    print('third')
else:
    print('last')


# In[64]:


## NOTE: IT executes only one true statement and finishes the if statements. wont execute another true statement
## nomatter how many are there


# In[ ]:




