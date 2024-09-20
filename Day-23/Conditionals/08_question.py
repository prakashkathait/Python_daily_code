'''Password strength Checker:
Problem: check if a password is "weak","medium","strong".
criteria:<6 chars(weak), 
6-10 chars(medium)
>10 chars (strong)'''

password = "Super@passaaa"

if len(password) <6:
    strength = "Weak"
elif len(password) < 11:
    strength = "medium"
elif len(password) > 10:
    strength = "Strong"

print("Your password strength is",strength)