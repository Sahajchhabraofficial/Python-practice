#Wap to find smallest number among has given three numbers without using (&&) logical and operator.
a=int(input("enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a<b:
    if a<c:
        print(f"{a} is smaller")
    elif b<c:
        print(f"{b} is smaller")
    else:
        print(f"{c} is smaller")
elif b<c:
    print(f"{b} is smaller")
else:
    print(f"{c} is smaller")