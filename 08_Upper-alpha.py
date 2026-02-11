#Write a program to check whether a character is uppercase alphabet or not.
char=input("enter a character: ")
if ord(char)>=65 and ord(char)<=90:
    print("Uppercase charcter")
else:
    print("Lowercase charcter")