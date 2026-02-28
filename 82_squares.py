#Write a program to print squares of all numbers present in a given array.
lst=[]
for i in range(4):
    ele=int(input("enter a element: "))
    lst.append(ele)

lst2=[num*num for num in lst]
print(lst2)