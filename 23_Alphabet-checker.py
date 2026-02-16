#Write a program to check whether a character is uppercase alphabet or lowercase alphabet or not alphabet.
alpha=input("Enter a character: ")
if alpha>='a' and alpha<='z':
    print("It is a alphabet")
elif alpha>='A' and alpha<='Z':
    print("It is a alpha bet")
else:
    print("It is a special character")