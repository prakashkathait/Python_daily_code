# Exercise 13: Print multiplication table from 1 to 10

i =1
j= 1
for i in range(1,11):
    for j in range(1,11):
        print(f'{i * j}',end=" ")
    print('\t')