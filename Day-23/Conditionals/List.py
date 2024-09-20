h1=[1,2,3]
h2=h1[:]
print(h1)
h1[0]=55
print(h1)
print(h2)  #In h2 still we have the same referance of h1, actually we have created the copy of h1

