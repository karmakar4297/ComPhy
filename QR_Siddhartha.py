#QR Decomposition
#Siddhartha
import numpy as np
A=np.array([[5, -2], [-2, 8]])
k=int(input('Enter large k (i.e number of iterations): '))
a=A
i=1
while(i<=k):
    q=np.linalg.qr(a)[0]
    r=np.linalg.qr(a)[1]
    a=np.matmul(r,q)
    i=i+1
print('Eigen values from QR decomposition: ', a[0,0], ' and ', a[1,1])
print('Eigen values from np.linalg.eigh: ',np.linalg.eigh(A)[0][0],' and ', np.linalg.eigh(A)[0][1])
