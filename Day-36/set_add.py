# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s=set()
for i in range(n):
    country = input() #input taken from the user 
    s.add(country)

print(len(s))