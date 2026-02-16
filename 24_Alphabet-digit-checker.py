#Write a program to check whether a character is an alphabet, digit or special character.
character=input("enter a char: ")
if character>='a' and character<='z' or character>='A' and character<='Z':
    print("It is a alphabet")
elif character>='0' and character<='1':
    print("It is a digit")
else:
    print("It is a special character")
