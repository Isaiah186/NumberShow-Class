#!/usr/bin/env python
# coding: utf-8

# In[7]:


class NumberShow:
    def __init__(self):
        pass
    
    def showNumbers(self,limit):
        
        for i in range(0, limit):
            if i % 2 ==0:
                print(f"This {i} is an even #")
            
            else:
                print(f"This {i} is an odd #")


# In[8]:


p1 = NumberShow()


# In[9]:


p1.showNumbers(10)


# In[ ]:




