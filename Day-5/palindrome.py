#Exercise 9: Check Palindrome Number

# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

print("Enter a number :")
num = int(input())
temp = num
rev = 0
def palindrome_num(num):
    while (num>0):
        dig = num%10
        rev = rev*10+dig
        num = num//10
if temp == rev:
        print("Number is Palindrome")
else:
        print("Number is not a plindrome")