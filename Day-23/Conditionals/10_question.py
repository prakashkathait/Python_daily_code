'''Pet food Recommendation:
problem: Recommend a type of pet food based on the pet's species and age.
(e.g., Dog: <2 years- Puppy food, Cat: >5 years - Senior cat food)
'''

Pet = "Cat"
age = 8

if Pet == "Dog":
    if age < 3:
        food ="Puppy food"
    else:
        food = "Senior dog food"
if Pet == "Cat":
    if age > 5:
        food = "Senior cat food"
    else:
        food = "Junior cat food"
print("Recommended food for your",Pet,"is",food)
