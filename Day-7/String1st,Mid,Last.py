# Exercise 3: Create a new string made of the first, middle, and last characters of each input string

s1 = "America"
s2 = "Japan"

x = s1[0]
x = x+s2[0]
i = int(len(s1)/2)
j = int(len(s2)/2)
x = x+s1[i]
x = x+s2[j]
x= x+s1[-1]
x= x+s2[-1]
print("New string will be after concatenation",x)
#Method2
def mix_string(s1,s2):
    fir = s1[0]+s2[0]
    mid = s1[int(len(s1)/2):int(len(s1)/2)+1] + s2[int(len(s2)/2):int(len(s2)/2)+1]
    lst = s1[-1]+s2[-1]
    res = fir+mid+lst
    print("character will be",res)