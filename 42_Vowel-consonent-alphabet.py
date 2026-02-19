#Check whether a character is a vowel, consonant, or not an alphabet.
char=input("enter a character: ")
char=char.lower()
if char>='a' and char<='z':
    if char in "AEIOUaeiou":
        print("Character is a vowel")
    else:
        print("character is not a consonent")
else:
    print("Char is not a alphabet")