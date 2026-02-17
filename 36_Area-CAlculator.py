#Write a program to make simple Area calculator 
# Press 1 to area of Circle 
# Press 2 to area of Reactangle 
# Press 3 to area of Tringle 
# Press 4 to area of Sqaure
print("=====WELCOME TO MY AREA CALCULATOR=====")
print("Press 1 to area of Circle")
print("Press 2 to area of Reactangle")
print("Press 3 to area of Tringle")
print("Press 4 to area of Sqaure")
choice=int(input("Enter your choice: "))
match choice:
    case 1:
        rad=int(input("Enter radius: "))
        print(f"Area of circle: {3.141*rad*rad}")
    case 2:
        len=int(input("Enter Length: "))
        Bred=int(input("Enter Breadth: "))
        print(f"Area of Rectangle: {len*Bred}")
    case 3:
        base=int(input("enter base: "))
        height=int(input("Enter height: "))
        print(f"Area of Rectangle: {(1/2)*base*height}")
    case 4:
        s=int(input("Enter Side: "))
        print(f"Area of square: {s*s}")
    case _:
        print("Invalid input!!")