'''Reverse a string using Loop'''

str = input("Enter the string:")
reversed_str =""

for char in str:
    print(char)
    reversed_str = char + reversed_str
print(reversed_str) 