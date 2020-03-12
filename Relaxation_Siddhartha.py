#Relaxation Method
#Siddhartha
import numpy as np
import math
a = np.array([[0.2, 0.1, 1, 1, 0], [0.1, 4, -1, 1, -1], [1, -1, 60, 0, -2], [1, 1, 0, 8, 4], [0, -1, -2, 4, 700]])
b = np.array([1, 2, 3, 4, 5])
x=np.zeros(5, dtype=float)
xt=np.zeros((5,5), dtype=float)
r=np.zeros((5,5), dtype=float)
f=0
count=0
temp=np.zeros(5, dtype=float)
w=1.25
while(f==0):
    i=0
    while(i<=4):
        j=0
        while(j<=i-1):
            xt[i,j]=temp[j]
            j=j+1
        j=i
        while(j<=4):
            xt[i,j]=x[j]
            j=j+1
        r[i]=b-np.matmul(a,xt[i])
        temp[i]=x[i]+w*r[i,i]/a[i,i]
        #print(temp, 'hey')
        i=i+1
    diff=temp-x
    check=np.matmul(diff,diff)
    check=math.sqrt(check)
    if(check<0.01):
        f=1
    count=count+1
    m=0
    while(m<=4):
        x[m]=temp[m]
        m=m+1
print('Solution',x)
print('Number of iterations',count)
        

            
            
    
