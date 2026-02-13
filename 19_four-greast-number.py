#Write a program to find greatest number among has given four numbers.
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter another another number: "))
d=int(input("Enter another another another number: "))
if a>b and a>c and a>d:
    print(f"{a} is greater")
elif b>c and b>d:
    print(f"{b} is greater")
elif c>d:
    print(f"{c} is greater")
else:
    print(f"{d} is greater")