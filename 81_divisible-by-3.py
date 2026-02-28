#Write a program to count how many elements in an array are multiples of 3.
lst=[]
for i in range(4):
    ele=int(input("enter a elements: "))
    lst.append(ele)
count=0
for j in range(4):
    if lst[j]%3==0:
        count+=1
print("there are",count,"numbers divisible by 3")