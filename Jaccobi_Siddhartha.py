#JACOBI METHOD
#Siddhartha
import numpy as np
import math
a = np.array([[0.2, 0.1, 1, 1, 0], [0.1, 4, -1, 1, -1], [1, -1, 60, 0, -2], [1, 1, 0, 8, 4], [0, -1, -2, 4, 700]])
b = np.array([1, 2, 3, 4, 5])
xtrue=np.array([7.859713071, 0.422926408, -0.073592239, -0.540643016, 0.010626163])
x=np.zeros(5, dtype=float)
f=0
count=0
temp=np.zeros(5, dtype=float)
while(f==0):
    i=0
    while(i<=4):
        s=0
        j=0
        while(j<=4):
            if(j!=i):
                s=s+a[i,j]*x[j]
            j=j+1
        temp[i]=(b[i]-s)/a[i,i]
        i=i+1
    diff=temp-xtrue
    f=1
    for k in range(5):
        if(abs(diff[k])>0.01):
           f=0
    count=count+1
    m=0
    while(m<=4):
        x[m]=temp[m]
        m=m+1
print('Solution: \n',x)
print('Number of iterations: ',count)
    
