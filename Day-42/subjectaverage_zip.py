N,X = map(int,input().split())

marks = []
for i in range(X):
     marks.append(list(map(float,input().split())))
    
   
result = list(zip(*marks))


for j in result:

    final_result = sum(j)/len(j)
    print("{:.1f}".format(final_result))