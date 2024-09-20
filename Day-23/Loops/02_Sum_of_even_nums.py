'''Sum of Even numbers
Problem: Calculate the sum of even numbers up to a given number n'''

n = 10 
even_number = 0

for i in range(1,n+1):
    if i%2 == 0:
        even_number += 1
print("Sum of Even numbers is:",even_number)