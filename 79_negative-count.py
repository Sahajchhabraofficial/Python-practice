#Write a program to count how many negative numbers are present in an array.
lst=[]
for i in range(4):
    ele=int(input("Enter a number: "))
    lst.append(ele)
count=0
for j in range(4):
    if lst[j]<0:
        count+=1
print("there are",count,"negative numbers")