#Wap to find greatest number among has given four numbers without using (&&) logical and operator.
a=int(input("enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
d=int(input("Enter fourth number: "))
if a>b:
    if a>c:
        if a>d:
            print(f"{a} is greater")
    elif b>c:
        if b>d:
            print(f"{b} is greater")
    elif c>d:
        print(f"{c} is greater")
    else:
        print(f"{d} is greater")
elif b>c:
    if b>d:
        print(f"{b} is greater")
elif c>d:
    print(f"{c} is smaller")