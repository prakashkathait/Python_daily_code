# No! Idea Hackerrank Question::

n,m=list(map(int,input().split())) #n integers 
my_array = list(map(int,input().split()))
set_a = list(map(int,input().split()))
set_b = list(map(int,input().split()))

def calculate_happiness(n,m,my_array,set_a,set_b):   
    happ = 0

    for num in my_array:
        if num in set_a:
            happ += 1 
        elif num in set_b:
            happ -= 1
    return happ

print(calculate_happiness(n,m,my_array,set_a,set_b))