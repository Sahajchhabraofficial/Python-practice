#Wap to find smallest number among has given four numbers without using (&&) logical and operator.
a=int(input("enter first num: "))
b=int(input("Enter second num: "))
c=int(input("Enter third num: "))
d=int(input("Enter fourth num: "))
if a<b:
    if a<c:
        if a<d:
            print(f"{a} is smaller")
        else:
            print(f"{d} is smaller")
    else:
        print(f"{c} is smaller")
elif b<c:
    if b<d:
        print(f"{b} is smaller")
    else:
        print(f"{d} is smaller")
elif c<d:
    print(f"{c} is smaller")
else:
    print(f"{d} is smaller")