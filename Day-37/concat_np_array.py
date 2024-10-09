import numpy as np 

N,M,P = list(map(int,input().split()))

array_1 = []
array_2 = []

for i in range(N):
    lst1 = list(map(int,input().split()))
    array_1.append(lst1)
for j in range(M):
    lst2 = list(map(int,input().split()))
    array_2.append(lst2)

arr1=np.array(array_1)
arr2=np.array(array_2)

print(np.concatenate((arr1,arr2),axis=0))