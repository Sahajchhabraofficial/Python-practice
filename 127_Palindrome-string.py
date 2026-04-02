#wap to check if a string is palindrome or not.
text=input("Enter a string: ")
text=text.lower()
if text==text[::-1]:
    print("String is Palindrome")
else:
    print("String is not palindrome")
