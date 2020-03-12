#Conjugate Gradient
#Siddhartha
import numpy as np
import math
a = np.array([[0.2, 0.1, 1, 1, 0], [0.1, 4, -1, 1, -1], [1, -1, 60, 0, -2], [1, 1, 0, 8, 4], [0, -1, -2, 4, 700]])
b = np.array([1, 2, 3, 4, 5])
xtrue=np.array([7.859713071, 0.422926408, -0.073592239, -0.540643016, 0.010626163])
x=np.zeros(5, dtype=float)
f=0
count = 0
g=b-np.dot(a,x)
r=g
rsold=np.dot(np.transpose(g),g)
while(f==0):
    ar=np.dot(a,r)
    alpha=rsold/(np.dot(np.transpose(r),ar))
    x=x+alpha*r
    g=g-alpha*ar
    rsnew=np.dot(np.transpose(g),g)
    r=g+(rsnew/rsold)*r
    rsold=rsnew
    f=1
    for i in range(5):
        if(abs(xtrue[i]-x[i])>0.01):
            f=0
    count=count+1
print('Solution: \n',x)
print('Number of iterations: ',count)
    
