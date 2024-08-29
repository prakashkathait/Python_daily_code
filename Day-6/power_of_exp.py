# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
base = int(input("Enter the base value: "))
exp = int(input("Enter the exponent value: "))
def exponent(base,exp):
    print(f'{base} raises to the power of {exp} :{pow(base,exp)}')
exponent(base,exp)