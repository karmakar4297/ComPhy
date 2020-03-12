#SVD
#Siddhartha
import numpy as np
import time
#a=np.array([[0, 1, 1], [0, 1, 0], [1, 1, 0], [0, 1, 0], [1, 0, 1]])
m=int(input('Enter #row: '))
n=int(input('Enter #column: '))
a=np.zeros((m,n),dtype=float)
print('Enter elements row-wise')
for i in range(m):
    for j in range(n):
        a[i,j]=float(input())
start_time1=time.time()
ev,u=np.linalg.eigh(np.dot(a,np.transpose(a)))
#print(ev)
sev1=ev.argsort()[::-1]
#print(sev1)
u=u[:,sev1]

ev2,v=np.linalg.eigh(np.dot(np.transpose(a),a))
sev2=ev2.argsort()[::-1]
v=v[:,sev2]

s=np.dot(np.dot(np.transpose(u),a),v)
stop_time1=time.time()
print('U:\n',u,'\n S:\n',s,'\n V:\n',v)
print('Time required = ',(time.time()-start_time1))
start_time2=time.time()
U,S,V=np.linalg.svd(a)
stop_time2=time.time()
print('\nSVD form using np.linalg.svd: \n')
print('U: \n',U,'\nS: \n',S,'\nV: \n',V)
print('Time required: ',(time.time()-start_time2))
