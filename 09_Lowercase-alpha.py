#Write a program to check whether a character lowercase alphabet or not.
alpha=input("enter a character: ")
if ord(alpha)>=97 and ord(alpha)<=122:
    print("Lowercase alphabet")
else:
    print("Uppercase alphabet")
