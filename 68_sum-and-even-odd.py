#Write a program to find sum of array elements & check sum is even or odd
lst=[]
for i in range(4):
    ele=int(input("Enter a element of list: "))
    lst.append(ele)
sum=0
for i in range(4):
    lst[i]+=sum

if sum%2==0:
    print("sum is even!")
else:
    print("sum is odd")
