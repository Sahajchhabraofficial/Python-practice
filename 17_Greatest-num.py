#Write a program to find greatest number among has given three numbers.
a=int(input("Enter a number: "))
b=int(input("Enter another number:"))
c=int(input("enter another another number: "))
if a>b and a>c:
    print(f"{a} is greater")
elif b>c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")