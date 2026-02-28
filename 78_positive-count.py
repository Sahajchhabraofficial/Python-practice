#Write a program to count how many positive numbers are present in an arraylst=[]
lst=[]
for i in range(4):
    ele=int(input("Enter a number: "))
    lst.append(ele)
count=0
for j in range(4):
    if lst[j]>0:
        count+=1
print("there are",count,"positive numbers")