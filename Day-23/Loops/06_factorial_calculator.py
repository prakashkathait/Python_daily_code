'''Factorial Calculator:
compute the factorial of a number using while loop'''

number = 5
factorial = 1 

while number > 0:
    factorial *= number 
    number -= 1
print(factorial)