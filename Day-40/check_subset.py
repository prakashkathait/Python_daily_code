T = int(input()) #no. of test cases

for i in range(0,T):
    temp = 0
    a = int(input()) #no. of elements in setA
    setA = set(map(int,input().split()))
    b = int(input()) #no. of elements in setB
    setB = set(map(int,input().split()))
    
    for j in setA:
        if j in setB:
            temp +=1
            continue
        else:
            print("False")
            break
    
    if (temp == a):
        print("True")