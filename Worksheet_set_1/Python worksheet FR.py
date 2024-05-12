#!/usr/bin/env python
# coding: utf-8

# In[2]:


10%3


# In[1]:


2//3


# In[3]:


6<<2


# In[4]:


6&2


# In[5]:


6|2


# In[ ]:


Question 11


# In[6]:


def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
num = int(input("Enter a number: "))
if num <0:
    print ("Factorial cannot be found for negative numbers")
elif num ==0:
    print ("Factorial of 0 is 1")
else:
    print ("Factorial of ",num, "is",factorial(num))
    


# In[ ]:


Question 12


# In[12]:


def prime(num):
    if num<2:
        return false
    for i in range(2,int(num**0.5),+1):
        if num % i ==0:
            return false
        return true
    num = int(input("Enter a numb: "))
if prime(num):
    print(num,"is a prime number")
else:
    print(num,"is a composite number")
        


# In[13]:


def a_palindrome(x):
    x=x.lower().replace(" ","")
    return x== x[::-1]
string= input("Enter a string")
if a_palindrome(string):
    print("String is palindrome")
else:
    print("not a palindrome")


# In[ ]:




