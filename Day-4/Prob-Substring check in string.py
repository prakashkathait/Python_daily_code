# Exercise: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

str_x = "Emma is good developer. Emma is a writer"
def count_emma(str_x):
    cnt =0
    for i in range(len(str_x)-1):
        if str_x[i:i+4] == 'Emma':
            cnt +=1
    return cnt
count = count_emma(str_x)
print("Emma appeared",count,"times")