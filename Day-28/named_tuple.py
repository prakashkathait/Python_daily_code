# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
total_marks =0 
fields= input().split()
for student in range(n):
    students = namedtuple('student',fields)
    MARKS,CLASS,NAME,ID = input().split()
    student = students(MARKS,CLASS,NAME,ID)
    total_marks += int(student.MARKS)
print(f'{total_marks/n}')

