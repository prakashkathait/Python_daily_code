'''Problem Statement: Movie tickets are priced based on the age group:
$12 for adults(18 and above)
$8 for children 
everyone gets a $2 discount on Wednesday
'''
age = int(input("Enter your Age:"))
day = "Wednesday"

price = 12 if age >=18 else 8
if day == "Wednesday":
    price -= 2
print("Ticket price for you is $",price)
