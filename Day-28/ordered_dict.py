# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())#total items 
from collections import OrderedDict
item_price = OrderedDict()
for i in range(N):
    #1. Receive the item 
    item,price = input().strip().rsplit(' ',1)
    price = int(price)
    
    #2. Adding items in ordered dictionary 
    if item in item_price:
        item_price[item] += price
    else:
        item_price[item] = price
for item,price in item_price.items():
    print(item,price)