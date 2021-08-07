#!/usr/bin/env python
# coding: utf-8


# 1.
# 
# 5 5 5 5 5 
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5 

# In[30]:


r = 5
n = r
# reverse for loop
for i in range(r, 0, -1):
    for j in range(0, i):
        print(n, end=' ')
    print("\r")


# 2.
# 
# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1 

# In[31]:


r = 5
for i in range(r, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")


# 3.
# 
# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9 

# In[32]:


r = 5
i = 1
while i <= r:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')


# 4.
# 
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 

# In[33]:


r = 6
for i in range(1, r):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")


# 5.
# 
# 1 
# 3 2 
# 6 5 4 
# 10 9 8 7

# In[34]:


stt = 1
stp = 2
c_n = stp
for r in range(2, 6):
    for col in range(stt, stp):
        c_n -= 1
        print(c_n, end=' ')
    print("")
    stt = stp
    stp += r
    c_n = stp


# 6.
# 
# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1 
# 1 5 10 10 5 1 
# 1 6 15 20 15 6 1 

# In[8]:


def print_pascal_triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()


def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

# set rows
rows = 7
print_pascal_triangle(rows)


# 7.
# 
# 1 2 3 4 5 
# 2 2 3 4 5 
# 3 3 3 4 5 
# 4 4 4 4 5 
# 5 5 5 5 5 

# In[35]:


r = 5
for i in range(1, r + 1):
    for j in range(1, r + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()


# 8.
# 
# 1  
# 2  4  
# 3  6  9  
# 4  8  12  16  
# 5  10  15  20  25  
# 6  12  18  24  30  36  
# 7  14  21  28  35  42  49  
# 8  16  24  32  40  48  56  64 

# In[36]:


r = 8
for i in range(1, r + 1):
    for j in range(1, i + 1):
        # multiplication current column and row
        square = i * j
        print(i * j, end='  ')
    print()


# 9.
# 
#         * * * * * * 
#          * * * * * 
#           * * * * 
#            * * * 
#             * * 
#              * 

# In[37]:


r = 5
k = 2 * r - 2
for i in range(r, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")


# 10.
# 
#             *   
#            *  *   
#           *  *  *   
#          *  *  *  *   
#         *  *  *  *  *   
#        *  *  *  *  *  *   
#       *  *  *  *  *  *  *   

# In[38]:


size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")


# 11.
# 
# *  
# * *  
# * * *  
# * * * *  
# * * * * *  
# * * * * * *  
#  
# * * * * * *  
# * * * * *  
# * * * *  
# * * *  
# * *  
# *  
#  
#  
# 

# In[39]:


r = 6
for i in range(0, r):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

print(" ")

for i in range(r + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")


# 12.
# 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# In[40]:


r = 5
for i in range(0, r):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(r, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")


# 13.
# 
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

# In[41]:


r = 5
i = 1
while i <= r:
    j = i
    while j < r:
        # display space
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = r
while i >= 1:
    j = i
    while j <= r:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1


# 14.
# 
# 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

# In[42]:


r = 5
i = 0
while i <= r - 1:
    j = 0
    while j < i:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= r - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = r - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= r - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1


# 15.
# 
# **************
# ******__******
# *****____*****
# ****______****
# ***________***
# **__________**
# *____________*
# 

# In[43]:


r = 14
print("*" * r, end="\n")
i = (r // 2) - 1
j = 2
while i != 0:
    while j <= (r - 2):
        print("*" * i, end="")
        print("_" * j, end="")
        print("*" * i, end="\n")
        i = i - 1
        j = j + 2
