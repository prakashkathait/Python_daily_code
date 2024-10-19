def update(setA,s,command):
    if command == "update":
        setA.update(s)
    elif command == "intersection_update":
        setA.intersection_update(s)
    elif command == "difference_update":
        setA.difference_update(s)
    else:
        setA.symmetric_difference_update(s)
    return setA

N = int(input())
setA = set(map(int,input().split()))

for i in range(int(input())):
    command,len_of_set = input().split()
    s = set(map(int,input().split()))
    setA = update(setA,s,command)

print(sum(setA))