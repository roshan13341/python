#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input())
while(n<10):
    print(n);
    n+=2;


# In[ ]:


n=int(input())
while(n>1):
    print(n);
    n-=1;


# In[ ]:


n=0;

sum=0;
while(n<=100):
      sum+=n;   
      n+=2; 
print(sum);


# In[ ]:


x=int(input("enter number"));
r=0;
while(x!=0):
    r=x%10;
    print(r);
    x=x//10;


# In[ ]:


n=int(input("enter the number"));

list=[];
while(n!=0):
    r=x%10;
    list[i]=r;
    print(r);
    x=x//10;
    i+=1;
    z=i;
i=0;
while(i<z):
    if(list[i]%2==0):
        print(list[i]);
        i+=1;
    


# In[ ]:


list=[1,2];
print(list[1]);


# In[ ]:


n=int(input("enter the number"));
sum=0;
while(n!=0):
    r=n%10;
    if(r%2==0):
        sum=sum+r;
    n=n//10;
    
print(sum);
       
    
    


# In[ ]:


x=int(input("enter number"));
r=0;
while(x!=0):
    r=x%10;
    if(r==1):
        print("one");
    elif(r==2):
        print("two");
    elif(r==3):
         print("three");
    elif(r==4):
        print("four");
    elif(r==5):
        print("five");
    elif(r==6):
         print("six");
    elif(r==7):
        print("seven");
    elif(r==8):
        print("eight");
    elif(r==9):
         print("nine");
    else:
        print("zero");
    x=x//10;


# In[ ]:


a=int(input());
b=int(input());
c=int(input());
t=0;
u=0;
list=[];
beat=[];
cet=[];
jet=[];
i=0;
j=0;
k=0;

while(a!=0):
    e=a%10;
    cet.append(e);
    k+=1;
    a=a//10;
x=cet[k-1];
print(x);
while(b!=0):
    r=b%10;
    list.append(r);
    i+=1;
    b=b//10;
    
z=list[i-1];
print(z);

while(c!=0):
    t=c%10;
    beat.append(t);
    j+=1;
    c=c//10;
y=beat[j-1];
print(y);
if(b<=c):
    l=b;
    while(l!=0):
        q=l%10;
        jet.append(q);
        l=l//10;
        u+=1;
        if(a==jet[u-1]):
            count+=1;
            print(count);
    b+=1;
    
    



# In[ ]:


def printnaturalnumber(n):
     cnt=1;
     while(cnt<=n):
            print(cnt,end=" ");
            cnt+=1;
     print()
     return 
    
printnaturalnumber(9)


# In[ ]:


def find(n):
    fact=1;
    while(n!=0):
        fact=fact*n;
        n=n-1;
    return fact;
print(find(5));


# In[ ]:


def even(n):
    m=n;
    if(n<=m):
        if(n%2==0):
            print(n);
    
print(even(8));


# In[ ]:


def printev(n):
    c=0;
    su=0;
    while(c!= n):
        if(cn%2==0):
            su=su+cn;
        cn+=1;
    return su;


print(printev(8));


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




