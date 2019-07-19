#checking vowel or not
vowels=['a','e','i','o','u']
consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
ch=input()
a=ch.lower()
if a in vowels:
    print("Vowel")
elif(a in consonants):
    print("Consonant")
else:
    print("invalid")
