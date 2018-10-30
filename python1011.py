#!/usr/bin/env python
# coding: utf-8

# In[26]:


#練習1
num=int(input("數字:"))
count=0
for i in range(1, num+1):
    count = count + i 
if(count%2==0):
    print("歐巴")
else:
    print("歐逆")


# In[25]:


message="string yo"
size=9487
percentage=0.9999
momis="TRUE"

print(float(size), str(momis), int(percentage), bool(message))


# In[27]:


def getweight(weight):
    weight = weight + 1
    weight = weight * 3
    return weight
print(getweight(5))


# In[20]:


#Homework
def kosh(num):
    for i in num:
        count=0
        for j in range(1, i+1):
            count = count + j
        if(count%2==0):
            print(count,end="\n")
            print("歐巴")
        else:
            print(count,end="\n")
            print("歐逆")
    return count
print(kosh([3,10,13]))


# In[17]:


# for迴圈片取陣列數字 再進行運算
# count([3,4,5])
def kosh(num):
    num=[int(input("數字1:")),int(input("數字2:")),int(input("數字3:"))]
    for i in num:
        count=0
        for j in range(1, i+1):
            count = count + j
        if(count%2==0):
            print(count,end="\n")
            print("歐巴")
        else:
            print(count,end="\n")
            print("歐逆")
    return count
print(kosh(num))


# In[2]:


for i in range(100, 150):
    if(i%2==0):
        print(i,"2倍數")
    elif(i%3==0):
        print(i,"3倍數")
    elif(i%5==0):
        print(i,"5倍數")
    elif(i%7==0):
        print(i,"7倍數")
    elif(i%11==0):
        print(i,"11倍數")
    else:
        print(i,"質數!!!")


# In[3]:


for i in range(100, 200):
    if(i%2==0):
        print(i,"2倍數")
    elif(i%3==0):
        print(i,"3倍數")
    elif(i%5==0):
        print(i,"5倍數")
    elif(i%7==0):
        print(i,"7倍數")
    elif(i%11==0):
        print(i,"11倍數")
    elif(i%13==0):
        print(i,"13倍數")
    else:
        print(i,"質數!!!")


# In[34]:


for j in range(1, 10):
    for i in range(10 - j - 1):
        print(" ",end="")
    print("* " * j ) 
print(end="\n")


# In[1]:


num1 = int(input("num1:"))
num2 = int(input("num2:"))
while(num1>0 and num2>0):
    if(num1>num2):
        num1 = num1 % num2 #輾轉相除法
    else:
        num2 = num2 % num1 #第二數變餘數 進入第一式
if(num1==0):
    print(num2) #剛好整除 所以等於第二個數
else:
    print(num1) #餘數即為最大公因數


# 52%39

# In[4]:


num1 = int(input("num1:"))
num2 = int(input("num2:"))
while(num1>0 and num2>0):
    if(num1>num2):
        num1 = num1 % num2 #輾轉相除法
    else:
        num2 = num2 % num1 #第二數變餘數 進入第一式
if(num1==0):
    print(num2) #剛好整除 所以等於第二個數


# In[ ]:




