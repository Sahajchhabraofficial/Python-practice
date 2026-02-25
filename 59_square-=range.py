#Write a program to display number square 1 to n (given number).
n=int(input("enter a range: "))
i=1
while i in range(1,n+1):
    print(i*i,end=" ")
    i+=1