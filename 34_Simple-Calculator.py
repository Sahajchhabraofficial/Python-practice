#Write a program to make simple calculator. 
# Press 1 to addition 
# Press 2 to subtraction 
# Press 3 to multiplication 
# Press 4 to division
print("=====WELCOME TO MY CALCULATOR=====")
print("Press 1 to add numbers")
print("Press 2 to subtract numbers")
print("Press 3 to multiply numbers")
print("Press 4 to devide numbers")
num=int(input("->>"))
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
match num:
    case 1:
        print(f"Addition: {a+b}")
    case 2:
        print(f"Subtraction: {a-b}")
    case 3:
        print(f"Multiplication: {a*b}")
    case 4:
        print(f"Division: {a/b}")
    case _:
        print("!!Invalid number!!")
