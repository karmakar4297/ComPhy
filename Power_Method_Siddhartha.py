#Power Method
#Siddhartha
import numpy as np
import math
a=np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
f=0
etrue=max(np.linalg.eig(a)[0])
print(etrue)
x0=np.ones(3, dtype=float)
x=x0
count=0
while(f==0):
    #x=np.matmul(a,x)
    e1=np.matmul(np.matmul(a,x),x0)/np.matmul(x,x0)
    err=abs((etrue-e1)/e1)
    if(err<0.01):
        f=1
    #e=e1
    x=np.matmul(a,x)
    count=count+1
x=x/(math.sqrt(np.dot(np.transpose(x),x)))
print('Greatest eigen value = ',e)
print('Corresponding eigen vector: ',x)
print('Number of iteration: ',count)
