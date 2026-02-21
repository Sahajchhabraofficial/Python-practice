#Write a program to check whether a character is uppercase or lowercase alphabet or not a alphabet.
char=input("enter a alphabet: ")
if char.isalpha():
    if char>='a' and char<='z':
        print("Given character is a lowercase alphabet")
    elif char>='A' or char<='Z':
        print("Given character is a uppercase alphabet")
else:
    print("It is not a alphabet")