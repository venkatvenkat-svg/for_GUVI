#Biggest of three numbers
a,b,c =input().split()

if (a>b and a>c):
    print(a)
elif(b>c):
    print(b)
else:
    print(c)
