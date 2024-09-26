# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
N,M = map(int,input().split())

D=defaultdict(list)
for i in range(N):
    s=input().rstrip()
    D[s].append(i+1)
for j in range(M):
    s=input().rstrip()
    
    if s in D:
        print(' '.join(map(str,D[s])))
    else:
        print('-1')