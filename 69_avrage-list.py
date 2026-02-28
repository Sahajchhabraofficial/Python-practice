#Write a program to find the average of array elements.
lst=[]
for i in range(4):
    ele=int(input("Enter list elements: "))
    lst.append(ele)
avg=0
sum=0
for j in range(4):
    sum+=lst[j]
avg=sum/4
print("avrage of sum elements: ",avg)
