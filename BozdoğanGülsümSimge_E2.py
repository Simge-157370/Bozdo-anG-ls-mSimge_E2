#!/usr/bin/env python
# coding: utf-8

# Exercise 4.1

# a)

# In[2]:


List1=["Ahmet","Mehmet","Ali"]
print(List1)


# b)

# In[3]:


List1.reverse()
print(List1)   


# c)

# In[9]:


def functionLen(Listx):
    i=0
    numberOfList=0
    for i in List1:
        numberOfList+=1
    return numberOfList
print(functionLen(List1))


# Exercise4.2

# a)

# In[10]:


ListA=[1,2,3,4]


# b)

# In[12]:


ListB=ListA


# c)

# In[19]:


ListB[1]=6
print(ListA)


# d)

# ListA[1] also changed to 6 

# e)

# In[26]:


ListC = ListA[:]


# f)

# In[27]:


ListC[1]=9
print(ListA)


# g)

# ListA didnt changed.

# In[30]:


def set_first_elem_to_zero(Listx):
    Listx[0]=0
    return Listx
print(set_first_elem_to_zero(ListA))


# ListA changed.

# Exercise 4.4

# In[32]:


def changeOfIndex(listx,indexA):
    listx[indexA]=0
    return listx
print(changeOfIndex(ListA,2))


# Exercise4.5

# In[ ]:




