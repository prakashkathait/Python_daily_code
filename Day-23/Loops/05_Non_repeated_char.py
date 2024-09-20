'''Find the First non-repeated character from a string
'''
# input_str = input("Enter a Character")
input_str = "teesteracacd"
for char in input_str:
    if input_str.count(char) == 1:
        print("Char is:", char)
        break