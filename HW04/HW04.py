
# coding: utf-8

# # Q1. 寫一個九九乘法表！

# In[4]:


def mulit(p,q):

    for i in range(1,10) :
      for j in range(p,q+1):
        print(j, 'X', i, '=', i*j ,end= "\t")
      print()
    print()



# In[5]:


mulit(2,5)
mulit(6,9)


# # Q2. 寫一個可以產生金字塔的函式！

# In[3]:


def sin(n):
    for a in range(int(n)):
        for b in range(int(n)- a - 1):
            print(" ",end="")
        for c in range(a + 1):
            print("* ", end = "" )
        print()                # 換行


# In[4]:


print (sin(10))


# In[5]:


sin(10)


# # Q3. 將 Q1 跟 Q2 的函式寫入一個模組，並呼叫模組裡面的函式來使用。

# In[5]:


import HW04


# In[6]:


HW04.sin(10)


# In[ ]:


HW04.mulit(2,5)
HW04.mulit(6,9)

