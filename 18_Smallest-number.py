#Write a program to find smallest number among has given three numbers.
a=int(input("enter a number: "))
b=int(input("Enter another number: "))
c=int(input("enter another another number: "))
if a<b and a<c:
    print(f"{a} is smaller")
elif b<c:
    print(f"{b} is smaller")
else:
    print(f"{c} is smaller")