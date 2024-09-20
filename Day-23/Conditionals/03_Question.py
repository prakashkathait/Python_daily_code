'''Grade Calculator:
Assign a letter grade based on the student's score:
A (90-100)
B (80-89)
C (70-79)
D (60-69)
F (below 60)
'''
score = int(input("Enter your marks: "))
if score >=101:
    print("Please verify your Score carefully")
    exit()

if (score < 60):
    print("F")
elif (score < 70):
    print("D")
elif (score < 80):
    print("C")
elif (score < 90):
    print("B")
else:
    print("A")
