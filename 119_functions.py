def Add(a,b):
    return a+b
def Sub(a,b):
    return a-b
def Mult(a,b):
    return a*b
def Div(a,b):
    return a//b

a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
print("   Press 1 for addition")
print("   press 2 for subtraction")
print("   Press 3 for multiplication")
print("   Press 4 for division")
val=int(input("->>"))
match val:
    case 1:
        print(f"{a} + {b} = {Add(a,b)}")
    case 2:
        print(f"{a} - {b} = {Sub(a,b)}")
    case 3:
        print(f"{a} x {b} = {Mult(a,b)}")
    case 4:
        print(f"{a} ∻ {b} = {Div(a,b)}")
    case _:
        print("Please enter a value 1-4!")