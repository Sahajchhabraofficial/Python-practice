#Write a program to display table of given number.
n=int(input("enter a number: "))
i=1
while i in range(1,11):
    print(f"{i} x {n} = {i*n}")
    i+=1