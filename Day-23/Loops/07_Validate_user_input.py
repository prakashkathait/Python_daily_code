'''Validate User Input: 
Keep asking User will input a number between 1 to 10 only'''

while True:
    number = int(input("Enter a number between 1 and 10: "))
    if 1 <= number <=10:
        print("Thanks")
        break
    else:
        print("Invalid number please try again later")