#Biggest of three numbers
a,b,c =input().split()
x=int(a)
y=int(b)
z=int(c)

if (x>y and x>z):
    print(x)
elif(y>z):
    print(y)
else:
    print(z)
