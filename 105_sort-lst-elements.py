#Write a program to arrange (sort) array elements in ascending or descending order.
lst=[]
for i in range(4):
    ele=int(input("enter a number: "))
    lst.append(ele)

lst.sort()
print("Acending sorting: ",lst)
lst.sort(reverse=True)
print("Decending sorting: ",lst)