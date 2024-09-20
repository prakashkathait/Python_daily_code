''''Multiplication Table Printer 
Problem: Print the multiplication table of number up to 10, 
but skip the fifth iteration'''

num = int(input("Enter the Number:"))

for i in range(1,11):
    if i == 5:
        continue
    print(f"{num}x{i}={num*i}")
    

