#Write a program to find smallest number among has given four numbers
a=int(input("enter a number: "))
b=int(input("Enter another number: "))
c=int(input("enter another another number: "))
d=int(input("enter another another another number: "))
if a<b and a<c and a<d:
    print(a, "is smaller")
elif b<c and b<d:
    print(b,"is smaller")
elif c<d:
    print(c,"is smaller")
else:
    print(d,"is smaller")