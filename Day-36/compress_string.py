# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import * 
n = input()

# for i,j in groupby(n):
#     print(i, end=" ")
#     for k in j:
#         print(k,end=" ")
#     print()
    
for i,j in groupby(n):
    print(tuple([len(list(j)),int(i)]),end=" ")