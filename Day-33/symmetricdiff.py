# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input()) #size of the first set 
a = set(map(int,input().split()))
N = int(input()) #size of the second set
b = set(map(int,input().split()))

symmetricdifferance = sorted(a^b)

for x in symmetricdifferance:
    print(x)