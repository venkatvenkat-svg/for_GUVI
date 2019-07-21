#check Alphabet or not
string="abcdefghijklmnopqrstuvwxyz"
alpha=list(string)#creating a list of alphabets

ch=input() #assign the input to "ch"
b=ch.lower()
if ch in alpha:
    a=ord(b)
    if a in range(a,a+25):
        print("Alphbet")
    else:
        print("No")
else:
    print("No")
