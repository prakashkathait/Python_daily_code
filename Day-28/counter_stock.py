x = int(input()) #no of shoes
stock = list(map(int,input().split(' '))) #shoes sizes 
# print(stock)
from collections import Counter
Dict = Counter(stock)
x = int(input()) #no of customers
p= 0
for i in range(x):
    size,price = map(int,input().split(' '))
    
    if Dict[size]:
        Dict[size] -= 1
        p = p+price
        
print(p)