#GAUSS-SEIDEL
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
        s1=0
        s2=0
        j=0
        while(j<=i-1):
            s1=s1+a[i,j]*temp[j]
            j=j+1
        j=i+1
        while(j<=4):
            s2=s2+a[i,j]*x[j]
            j=j+1
        temp[i]=(b[i]-s2-s1)/a[i,i]
        i=i+1
    diff=temp-xtrue
    f=1
    for k in range(5):
        if(abs(diff[k])>0.01):
            f=0
    count=count+1
    m=0
    x=temp
print('Solution: \n',x)
print('Number of iterations: ',count)
    
