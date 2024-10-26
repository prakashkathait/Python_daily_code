def superset(A,B):
    if A.issuperset(B):
        return True
    else:
        return False

if __name__ =="__main__":
    
    A = set(map(int,input().split()))
    N = int(input())
    
    for i in range(N):
        B = set(map(int,input().split()))
        result = superset(A,B)
        if result == False:
            break
    print(result)