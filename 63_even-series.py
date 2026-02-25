#Write a program to display even number series
num=int(input("Enter a range: "))
i=1
while i in range(1,num+1):
    if i%2==0:
        print(i,end=" ")
    i+=1