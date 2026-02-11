#Write a program to compute the sum of the two input values. If the two values are the same, then return triple their sum.
val1=int(input("enter 1st number: "))
val2=int(input("enter 2nd number: "))
if val1==val2:
    print("triple of their sum=",3*(val1+val2))
else:
    print("sum of two numbers=",val1+val2)