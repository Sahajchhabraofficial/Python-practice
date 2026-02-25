#Write a program to display odd number series
n=int(input("enter a range: "))
i=1
while i in range(1,n+1):
    if i%2==1 :
        print(i,end=" ")
    i+=1
