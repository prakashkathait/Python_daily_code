# printing all factors of a number

def factors(n):
    res=[]
    for i in range(1,n+1):
        if n%i==0:
            res.append(i)
    return res

n = int(input("Enter the number: "))
print(factors(n))