# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
A = set(map(int,input().split()))
n= int(input())
B = set(map(int,input().split()))

print(len(A|B))