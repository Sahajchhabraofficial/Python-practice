#Write a program to count how many even numbers are present in an array.
lst=[]
for i in range(4):
    ele=int(input("Enter a number: "))
    lst.append(ele)
count=0
for j in range(4):
    if lst[j]%2==0:
        count+=1
print("there are",count,"even numbers")