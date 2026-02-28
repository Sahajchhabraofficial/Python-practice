#Write a program to copy elements from one array to another
lst=[]
for i in range(4):
    ele=int(input("enter elements: "))
    lst.append(ele)
lst2=lst
print("your list: ",lst)
print("copy list: ",lst2)