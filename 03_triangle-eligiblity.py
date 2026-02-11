#Write a program to check whether the triangle is valid or not if angles are given.
a1=int(input("enter angle 1:"))
a2=int(input("enter angle 2: "))
a3=int(input("enter angle 3: "))
if a1+a2+a3==180 and a1>0 and a2>0 and a3>0:
    print("It is a triangle")
else:
    print("It is something else")