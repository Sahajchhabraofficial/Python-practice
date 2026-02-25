#Write a program to display multiple of 7 between given range
n=int(input("enter a range: "))
i=1
while i in range(1,n+1):
    if i%7==0:
        print(i,end=" ")
    i+=1