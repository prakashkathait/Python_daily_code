x,k = map(int,input().split())
y = input() #expression given by the user to check the p(x)=k or not 
z = eval(y) 
print('True' if int(z)  == int(k) else 'False')