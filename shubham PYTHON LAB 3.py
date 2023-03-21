#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=int(input("Enter your number"))

while(num>=0):

    print(num)

    num=num-1


# In[2]:


a = 1

for b in range(2, 11):
    print(f"{a}/{b} :", a/b)


# In[7]:


n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print ("The number isn't palindrome!")


# In[1]:



num = int(input("Enter a number: "))


sum = 0


temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# In[2]:


sum=0
count_pos=0
count_neg=0
while(True):
    i=float(input("enter an integer(0 to end):"))
    if i==0:
        break
    sum+=i
    if i>0:
        count_pos+=1
    elif i<0:
        count_neg+=1
    avg=sum/(count_pos+count_neg)
print("The total number of positive numbers:",count_pos)
print("The total number of negative numbers:",count_neg)
print("the total sum:",sum)
print("the avg:",avg)


# In[3]:


total_student=int(input("enter no of students:"))
highest=0
for i in range(total_student):
    marks=int(input("enter the marks:"))
    if marks>highest:
        highest=marks
print("highest marks is:",highest)


# In[5]:


n1=int(input("enter first integer:"))
n2=int(input("enter second integer:"))
gcd=1
k=2
while(k<=n1 and k<=n2):
    if n1%k==0 and n2%k==0:
        gcd=k
    k=k+1
print("the greatest common divisor of",n1,"and",n2,"is",gcd)


# In[6]:


num=int(input("enter number:"))
space=" "

for i in range(1,num+1):
    for num_of_spaces in range(i+1,1,-num):
        x=(i-1)
        spaces = space*(num-x)
        print(spaces,end="")
    for inv_rec in range(i,1,-1):
        print(inv_rec,end="")
    for rec in range(1,i+1):
        print(rec,end="")
    print("")


# In[ ]:




