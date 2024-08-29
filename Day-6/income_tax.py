# Exercise 12: Calculate income tax for the given income by adhering to the rules below
# first 10000,tax =0
#next 10k,tax = 10%
#remaining,tax =20%

income = 56000
tax = 0
if income<=10000:
    tax = 0
elif income<=20000:
    x = income-10000
    tax = (x*10)/100
else:
    tax =0
    tax =10000*10/100
    tax += (income-20000)*20/100
print("Taxable amount is", tax)