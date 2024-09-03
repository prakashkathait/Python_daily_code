#Checking if a string is palindrome or not
stri = str(input("Enter a string:"))
def palindrome(stri):
        if (stri == stri[::-1]):
            return "String is Palindrome"
        else:
            return "Not a palindrome"
print(palindrome(stri))