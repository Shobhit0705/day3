#!/usr/bin/env python
# coding: utf-8

# In[12]:


#1: Which of the following are valid number data types in Python 3? Select all that apply:
a = 3
print( "a is", type(a))
b = 5.9 
print("b is", type(b))
c = "5"
print("c is", type(c))

#Answer: B)Float, D) Int, C) str


# In[16]:


#2. What’s the name of the function for rounding numbers in Python?
#Answer: round()
print(round(3.14))
round(5.9)


# In[17]:


#3. How do you get the absolute value of a number in Python?
#Answer: A) abs(-3.14)
abs(-3.14)


# In[19]:


|-3.14|


# In[22]:


#4. What is the output of the following round() function call?
#Answer: c) 100.256 & 100.0
print(round(100.2563, 3))
print(round(100.000056, 3))


# In[25]:


#5. What is the output of the following number conversion
#Answer: b. Value Error: Missing an imaginary part of a complex number
z = complex(1.25)


# In[27]:


#6. What is the output of print(abs(-45.300))
#Answer: a. 45.3
print(abs(-45.300))


# In[28]:


#7. What is the output of the following math function
#Answer: c. 253 & 252

import math
print(math.ceil(252.4))
print(math.floor(252.4))


# In[5]:


#8. Select all correct float numbers
#Answer: a,b,c,d

a = 10.1256 
print("a", type(a))
b = -10.5
print("b", type(b))
c = 42e3
print("c",type(c))
d = -68.7e100
print("d",type(d))


# In[6]:


#9. What is the output of the following code
#Answer: c. 2
print(int(2.999))


# In[8]:


#10 .Which Data Type represents a whole number?
#Answer: b. Integer 
print(type(1))
a = 1
print(type(a))


# In[9]:


#11. What data type to store the pi=3.14
#Answer: c. float
pi = 3.14
type(pi)


# In[10]:


#12. What data type for a variable called numberOfLives in a game?
#Answer: a. string 
a = 'numberOfLives'
type(a)


# In[11]:


#13. What is the correct definition for a VARIABLE?
#Answer: a. changeable value, such as a score in a computer game.


# In[16]:


#The value 1.73 rounded to one decimal place using the “rounding up” strategy is...
#Answer: a. 1.7
round(1.73,1)


# In[17]:


#15. The value -2.961 rounded to two decimal places using the “rounding down” strategy is...
#Answer:d. -2.96
round(-2.961,2)


# In[18]:


#16. Which of the following is not a complex number?
#Answer: b. k = complex(2,3)


# In[19]:


#17.What will be the output of the following code :print (type(type(int))).
#Answer: b. type 'type'
print (type(type(int)))


# In[20]:


#18. Which of the following functions is a built-in function in python?
#Answer: d.print()
print("this is built in")


# In[22]:


#19. What will be the output of the following Python expression?
#Answer: b. 5
round(4.576)


# In[23]:


#20. What will be the output of the following Python function?
#Answer: b. False
min(max(False,-3,-4), 2,7)


# In[28]:


#21. Which of the following is the use of id() function in python?
#Answer: b. Id() returns the identity of the object.

id(print)


# In[29]:


#22. If we change one data type to another, then it is called
#Answer: A. Type conversion


# In[30]:


#23. type() function in python is
#Answer: predefined


# In[31]:


#24. What is the output of the following function print(type(3))
#Anwer: a. int
print(type(3))


# In[33]:


#25. What is the type of inf?
#Answer: float.inf


# In[ ]:




