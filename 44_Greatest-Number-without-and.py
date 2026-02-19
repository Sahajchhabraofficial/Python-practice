#Wap to find greatest number among has given three numbers without using (&&) logical and operator.
a=int(input("enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b:
    if a>c:
        print(f"{a} is greater")
    elif b>c:
        print(f"{b} is greater")
    else:
        print(f"{c} is greater")
elif b>c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")