#Write a program to find the sum of all elements in an array.
lst=[]
for i in range(4):
    ele=int(input(f"enter {i+1} elements of array: "))
    lst.append(ele)
sum=0
for i in range(4):
    sum+=lst[i]
print(f"sum of list {sum}")